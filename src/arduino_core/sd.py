from typing import Any
from src.arduino_core.definitions import byte

SD_CARD_TYPE_SD1: int = 0
SD_CARD_TYPE_SD2: int = 1
SD_CARD_TYPE_SDHC: int = 2

LS_R: int = 0
LS_DATE: int = 1
LS_SIZE: int = 2

FILE_READ: int = 0
FILE_WRITE: int = 1

class File:
    def print(self, data: Any) -> None:
        pass

    def println(self, data: Any) -> None:
        pass

    def close(self) -> None:
        pass

    def read(self) -> byte:
        return 0

    def available(self) -> bool:
        return True

    def openNextFile(self) -> "File":
        return File()

    def name(self) -> str:
        return ""

    def isDirectory(self) -> bool:
        return True

    def size(self) -> int:
        return 0

    def availableForWrite(self) -> bool:
        return True

    def write(self, data: Any, size: int) -> None:
        pass

class SD:
    @staticmethod
    def begin(pin: int) -> bool:
        return True

    @staticmethod
    def open(path: Any, operation: int = FILE_READ) -> File:
        return File()

    @staticmethod
    def exists(path: str) -> bool:
        return True

    @staticmethod
    def remove(path: str) -> None:
        pass

class Sd2Card:
    def init(self, spi_speed: int, chip_select: int) -> bool:
        return True

    def type(self) -> int:
        return 0

class SdVolume:
    def init(self, card: Sd2Card) -> bool:
        return True

    def clusterCount(self) -> int:
        return 0

    def blocksPerCluster(self) -> int:
        return 0

    def fatType(self) -> int:
        return 0

class SdFile:
    def openRoot(self, volume: SdVolume) -> None:
        pass

    def ls(self, flags: int) -> None:
        pass
