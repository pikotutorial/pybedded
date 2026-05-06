from enum import Enum
from typing import Any, List

# types
long = int
unsigned_long = int
unsigned_int = int
byte = int
char = str

# pin modes
OUTPUT: int = 0
INPUT: int = 1
INPUT_PULLUP: int = 2

# pin states
LOW: int = 0
HIGH: int = 1

# analog pins IDs
A0 = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
A5 = 5

# boards
class Board(Enum):
    UNO = "arduino:avr:uno"
    NANO = "arduino:avr:nano"
    NANO_OLD_BOOTLOADER = "arduino:avr:nano:cpu=atmega328old"
    MEGA = "arduino:avr:mega"

# other
LED_BUILTIN: int = 0
DEC: int = 0
HEX: int = 1
BIN: int = 2

def word(range_1: Any, range_2: Any) -> unsigned_long:
    return 0

def memset(buffer: List[byte], value: int, size: int) -> None:
    pass

def sizeof(obj: Any) -> int:
    return 0

def IFDEF(condition: str) -> None:
    pass

def IFNDEF(condition: str) -> None:
    pass

def ENDIF() -> None:
    pass
