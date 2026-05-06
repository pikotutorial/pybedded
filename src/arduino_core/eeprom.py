from typing import Any
from src.arduino_core.definitions import byte

class EEPROM:
    @staticmethod
    def length() -> int:
        return 0

    @staticmethod
    def write(address: int, value: int) -> None:
        pass

    @staticmethod
    def get(address: int, placeholder: Any) -> None:
        pass

    @staticmethod
    def put(address: int, placeholder: Any) -> None:
        pass

    @staticmethod
    def read(address: int) -> byte:
        pass

    @staticmethod
    def update(address: int, value: Any) -> None:
        pass
