from dataclasses import dataclass

from src.py_to_cpp_converter.models.code_object import CodeObject


@dataclass
class IfStatement(CodeObject):
    condition: str
