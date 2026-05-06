from dataclasses import dataclass

from src.py_to_cpp_converter.models.code_object import CodeObject


@dataclass
class VariableDefinition(CodeObject):
    name: str
    type: str
    value: str
    is_compile_time: bool
    is_array: bool
    array_size: str
    array_content: str
