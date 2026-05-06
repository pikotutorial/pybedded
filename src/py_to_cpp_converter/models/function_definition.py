from dataclasses import dataclass
from typing import List

from src.py_to_cpp_converter.models.code_object import CodeObject


@dataclass
class FunctionArgument:
    name: str
    type: str

@dataclass
class FunctionDefinition(CodeObject):
    name: str
    arguments: List[FunctionArgument]
    return_type: str
