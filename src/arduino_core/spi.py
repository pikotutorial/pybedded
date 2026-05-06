from dataclasses import dataclass
from src.arduino_core.definitions import byte, unsigned_int, long

SPI_HALF_SPEED: int = 0
MSBFIRST: int = 0
LSBFIRST: int = 1
SPI_MODE0: int = 0
SPI_MODE1: int = 1
SPI_MODE2: int = 2
SPI_MODE3: int = 3

@dataclass
class SPISettings:
    speedMaximum: long
    dataOrder: int
    dataMode: int

class SPI:
    @staticmethod
    def begin() -> None:
        pass

    @staticmethod
    def transfer(data: byte) -> unsigned_int:
        return 0
    
    @staticmethod
    def beginTransaction(settings: SPISettings) -> None:
        pass

    @staticmethod
    def endTransaction() -> None:
        pass

    @staticmethod
    def end() -> None:
        pass

    @staticmethod
    def setBitOrder(order: int) -> None:
        pass

    @staticmethod
    def setClockDivider(divider: int) -> None:
        pass

    @staticmethod
    def setDataMode(mode: int) -> None:
        pass

    @staticmethod
    def usingInterrupt(interruptNumber: int) -> None:
        pass
