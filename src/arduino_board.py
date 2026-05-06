import inspect
import logging
import os.path
import shutil

from inspect import FrameInfo
from typing import Tuple, List

from src.py_to_cpp_converter.py_2_cpp_converter import Py2CppConverter
from src.sys_command_runner import SysCommandRunner
from src.arduino_core.definitions import Board

LOGGER = logging.getLogger("ArduinoBoard")

FilePath = str
LineNumber = int

class ArduinoBoard:
    def __init__(self, port: str, board: Board, verbose: bool = False, compile: bool = True, upload: bool = True,
                 clean_up: bool = True):
        self.__port: str = port
        self.__board: Board = board
        self.__verbose: bool = verbose
        self.__compile_code: bool = compile
        self.__upload_code: bool = upload
        self.__clean_up_workspace: bool = clean_up

        if self.__verbose:
            logging.basicConfig(format='[%(levelname)s][%(name)s] %(message)s',
                                level=logging.DEBUG)

    def __enter__(self):
        LOGGER.info("--- Program start ---")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        LOGGER.info("--- Program end ---")
        LOGGER.info(f"Starting Python-to-Arduino conversion")

        file_path, start_line = self.__get_callers_properties()
        python_code: List[str] = self.__load_arduino_python_code(file_path, start_line)
        cpp_code: str = Py2CppConverter.convert(python_code)
        arduino_project_path: str = self.__create_arduino_project(file_path, cpp_code)

        if self.__compile_code:
            print("Compiling...")
            self.__compile(arduino_project_path)
        if self.__upload_code:
            print("Uploading...")
            self.__upload(arduino_project_path)
        if self.__clean_up_workspace:
            self.__clean_up(arduino_project_path)

        print("Done")

    def __get_callers_properties(self) -> Tuple[FilePath, LineNumber]:
        LOGGER.info("Getting properties of the Python script with Arduino code")

        frame: FrameInfo = inspect.stack()[2]
        file_path: str = frame.filename
        start_line: int = frame.lineno

        LOGGER.debug(f"Python code available in {file_path}, starting at line {start_line}")

        return frame.filename, frame.lineno

    def __load_arduino_python_code(self, script_path: FilePath, python_code_start_line: LineNumber) -> List[str]:
        LOGGER.info(f"Loading Python Arduino code from {script_path} starting at {python_code_start_line}")

        with open(script_path) as file:
            return file.readlines()[python_code_start_line:]

    def __create_arduino_project(self, script_path: str, cpp_code: str) -> FilePath:
        LOGGER.info(f"Creating Arduino project")

        file_name: str = os.path.basename(script_path).rstrip(".py")
        dir_path: str = os.path.join(os.path.dirname(script_path), file_name)

        if os.path.exists(dir_path):
            LOGGER.warning(f"Project directory with the same name already exists - deleting...")
            shutil.rmtree(dir_path)

        LOGGER.debug(f"Creating project directory: {dir_path}")
        os.mkdir(dir_path)

        LOGGER.debug(f"Creating .ino file and saving C++ code")
        with open(os.path.join(dir_path, f"{file_name}.ino"), 'w') as file:
            file.write(cpp_code)

        LOGGER.debug(f"Arduino project created")

        return dir_path

    def __compile(self, arduino_project_path: FilePath) -> None:
        LOGGER.info(f"Compiling C++ code")

        SysCommandRunner.run_command(f"arduino-cli compile --fqbn {self.__board.value} {arduino_project_path}",
                                     show_output=self.__verbose)

        LOGGER.debug(f"Compilation done")

    def __upload(self, arduino_project_path: FilePath) -> None:
        LOGGER.info(f"Flashing Arduino board")

        SysCommandRunner.run_command(f"arduino-cli upload -p {self.__port} --fqbn {self.__board.value} {arduino_project_path}",
                                     show_output=self.__verbose)

        LOGGER.debug(f"Flashing done")

    def __clean_up(self, arduino_project_path: str) -> None:
        LOGGER.info(f"Cleaning up the workspace")

        if os.path.exists(arduino_project_path):
            LOGGER.info(f"Removing Arduino project folder {arduino_project_path}")
            shutil.rmtree(arduino_project_path)

        LOGGER.debug(f"Clean up done")
