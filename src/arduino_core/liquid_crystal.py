from typing import Any, List
from src.arduino_core.definitions import byte


class LiquidCrystal:
    def __init__(self, rs: int, en: int, d4: int, d5: int, d6: int, d7: int):
        self.__id: str = f"{rs}/{en}/{d4}/{d5}/{d6}/{d7}"

    def begin(self, columns: int, rows: int) -> None:
        pass

    def setCursor(self, column: int, row: int) -> None:
        pass

    def print(self, character: Any) -> None:
        pass

    def autoscroll(self) -> None:
        pass

    def noAutoscroll(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def noBlink(self) -> None:
        pass

    def blink(self) -> None:
        pass

    def noCursor(self) -> None:
        pass

    def cursor(self) -> None:
        pass

    def createChar(self, id: int, character: List[byte]) -> None:
        pass

    def write(self, id: Any) -> None:
        pass

    def noDisplay(self) -> None:
        pass

    def display(self) -> None:
        pass

    def scrollDisplayLeft(self) -> None:
        pass

    def scrollDisplayRight(self) -> None:
        pass

    def rightToLeft(self) -> None:
        pass

    def leftToRight(self) -> None:
        pass

    def home(self) -> None:
        pass
