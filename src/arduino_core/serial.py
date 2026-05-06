from typing import Any
from src.arduino_core.definitions import byte, DEC


class Serial:
    @staticmethod
    def begin(baudrate: int) -> None:
        pass

    @staticmethod
    def available() -> bool:
        return True

    @staticmethod
    def print(message: Any, format: int = DEC) -> None:
        pass

    @staticmethod
    def println(message: Any, format: int = DEC) -> None:
        pass

    @staticmethod
    def read() -> Any:
        return 0

    @staticmethod
    def write(data: byte) -> None:
        pass

    @staticmethod
    def parseInt() -> int:
        return 0
    
    @staticmethod
    def availableForWrite() -> int:
        return 0
    
    @staticmethod
    def end() -> None:
        pass

    @staticmethod
    def find(target: str) -> int:
        return 0
    
    @staticmethod
    def findUntil(target: str, terminator: str) -> int:
        return 0
    
    @staticmethod
    def flush() -> None:
        pass

    @staticmethod
    def parseFloat() -> float:
        return 0.0
    
    @staticmethod
    def peek() -> int:
        return 0
    
    @staticmethod
    def readBytes(buffer: bytearray, length: int) -> int:
        return 0
    
    @staticmethod
    def readBytesUntil(terminator: str, buffer: bytearray, length: int) -> int:
        return 0
    
    @staticmethod
    def readString() -> str:
        return ""
    
    @staticmethod
    def readStringUntil(terminator: str) -> str:
        return ""
    
    @staticmethod
    def setTimeout(timeout: int) -> None:
        pass

    @staticmethod
    def serialEvent() -> None:
        pass

class Serial1(Serial):
    pass

class Serial2(Serial):
    pass

class String:
    def __init__(self, value: Any):
        pass

    def __str__(self):
        return ""
