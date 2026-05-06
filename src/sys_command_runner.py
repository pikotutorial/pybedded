import subprocess
import logging

from subprocess import CompletedProcess

LOGGER = logging.getLogger("SysCommandRunner")


class SysCommandRunner:
    @staticmethod
    def run_command(command: str, show_output: bool) -> CompletedProcess:
        LOGGER.info(f"Running command: {command}")

        ret_val: CompletedProcess = subprocess.run(command, shell=True, capture_output=not show_output)
        SysCommandRunner.__check_ret_val(ret_val)

        return ret_val

    @staticmethod
    def __check_ret_val(ret_val: CompletedProcess) -> None:
        if ret_val.returncode != 0:
            raise RuntimeError(f'Failed to execute command {ret_val.args}!\n'
                               f'Error:\n{ret_val.stderr}\n{ret_val.stdout}')
