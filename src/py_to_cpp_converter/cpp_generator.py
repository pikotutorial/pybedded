import logging
from typing import List

from src.py_to_cpp_converter.models.code_object import CodeObject
from src.py_to_cpp_converter.models.elif_statement import ElifStatement
from src.py_to_cpp_converter.models.else_block import ElseBlock
from src.py_to_cpp_converter.models.for_loop import ForLoop
from src.py_to_cpp_converter.models.function_call import FunctionCall
from src.py_to_cpp_converter.models.function_definition import FunctionDefinition
from src.py_to_cpp_converter.models.if_statement import IfStatement
from src.py_to_cpp_converter.models.preprocessor_directive import PreprocessorDirective
from src.py_to_cpp_converter.models.return_statement import ReturnStatement
from src.py_to_cpp_converter.models.variable_modification import VariableModification
from src.py_to_cpp_converter.models.variable_definition import VariableDefinition
from src.py_to_cpp_converter.models.while_loop import WhileLoop

LOGGER = logging.getLogger("CppGenerator")


def adjust_condition(condition: str) -> str:
    return (condition
            .replace(" AND ", " && ")
            .replace(" OR ", " || ")
            .replace(" NOT ", " !")
            .replace("NOT ", "!")
            .replace("TRUE", "true")
            .replace("FALSE", "false"))

def adjust_type(type: str) -> str:
    return (type
            .replace("STRING", "String")
            .replace("unsigned_long", "unsigned long")
            .replace("unsigned_int", "unsigned int"))


class CppGenerator:
    @staticmethod
    def generate(model: CodeObject, depth: int) -> str:
        LOGGER.info(f"Generating C++ code out of the following mode: {model}")

        cpp_code: str = ""
        indentation: str = " " * depth * 4

        for code_object in model.content:
            if isinstance(code_object, FunctionDefinition):
                LOGGER.debug(f"Given model is a function definition")

                args = ""

                for arg in code_object.arguments:
                    args += f"{adjust_type(arg.type)} {arg.name}, "

                code_object.return_type = adjust_type(code_object.return_type)

                cpp_code += f"{indentation}{code_object.return_type} {code_object.name}({args.rstrip(", ")}) {{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, ForLoop):
                LOGGER.debug(f"Given model is a for loop")

                cpp_code += (f"{indentation}for (int {code_object.iter_var_name}={code_object.start_index}; "
                             f"{code_object.iter_var_name}{'>=' if code_object.step.startswith('-') else '<'}{code_object.end_index}; "
                             f"{code_object.iter_var_name} += {code_object.step}) {{\n")
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, ElifStatement):
                LOGGER.debug(f"Given model is an elif statement")

                cpp_code += f"{indentation}else if ({adjust_condition(code_object.condition)}) {{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, IfStatement):
                LOGGER.debug(f"Given model is an if statement")

                cpp_code += f"{indentation}if ({adjust_condition(code_object.condition)}) {{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, WhileLoop):
                LOGGER.debug(f"Given mode is a while loop")

                cpp_code += f"{indentation}while ({adjust_condition(code_object.condition)}) {{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, FunctionCall):
                LOGGER.debug(f"Given model is a function call")
                cpp_code += f"{indentation}{code_object.call};\n"
            elif isinstance(code_object, VariableDefinition):
                code_object.value = adjust_condition(code_object.value)

                if code_object.is_compile_time:
                    LOGGER.debug(f"Given model is a #define directive")
                    cpp_code += f"#define {code_object.name} {code_object.value}\n"
                else:
                    LOGGER.debug(f"Given model is a variable definition")

                    code_object.type = adjust_type(code_object.type)

                    if code_object.is_array:
                        if code_object.array_size:
                            cpp_code += f"{indentation}{code_object.type} {code_object.name}[{code_object.array_size}];\n"
                        else:
                            cpp_code += f"{indentation}{code_object.type} {code_object.name}[] = {{{code_object.array_content}}};\n"
                    else:
                        cpp_code += f"{indentation}{code_object.type} {code_object.name} = {code_object.value};\n"
            elif isinstance(code_object, VariableModification):
                LOGGER.debug(f"Given model is a variable modification")

                code_object.value = adjust_condition(code_object.value)

                cpp_code += f"{indentation}{code_object.name} {code_object.operator}{code_object.value};\n"
            elif isinstance(code_object, ElseBlock):
                LOGGER.debug(f"Given model is an else block")

                cpp_code += f"{indentation}else {{\n"
                cpp_code += CppGenerator.generate(code_object, depth + 1)
                cpp_code += f"{indentation}}}\n"
            elif isinstance(code_object, ReturnStatement):
                LOGGER.debug(f"Given model is a return statement")

                cpp_code += f"{indentation}return {code_object.return_expression};\n"
            elif isinstance(code_object, PreprocessorDirective):
                LOGGER.debug(f"Given model is a preprocessor directive")

                directive: str = (code_object.directive
                                  .replace("IFNDEF", "ifndef")
                                  .replace("IFDEF", "ifdef")
                                  .replace("ENDIF", "endif"))
                cpp_code += f"#{directive} {code_object.expression}\n"

        return cpp_code

    @staticmethod
    def generate_headers(dependencies: List[str]) -> str:
        headers: str = ""

        for dependency in dependencies:
            headers += f"#include <{dependency}.h>\n"

        return headers
