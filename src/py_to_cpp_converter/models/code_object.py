from dataclasses import dataclass
from typing import List


@dataclass
class CodeObject:
    content: List["CodeObject"]
