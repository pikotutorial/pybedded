from dataclasses import dataclass
from typing import List, Any
from src.arduino_core.definitions import byte

# hardware status
EthernetNoHardware: int = 0
EthernetW5100: int = 1
EthernetW5200: int = 2
EthernetW5500: int = 3

# link status
Unknown: int = 0
LinkON: int = 1
LinkOFF: int = 2

# UDP
UDP_TX_PACKET_MAX_SIZE: int = 0

@dataclass
class IPAddress:
    first_octet: int
    second_octet: int
    third_octet: int
    fourth_octet: int

    def __getitem__(self, item):
        pass

class Ethernet:
    @staticmethod
    def init(cs_pin: int) -> None:
        pass

    @staticmethod
    def begin(mac: List[byte], ip: IPAddress = None, dns: IPAddress = None, gateway: IPAddress = None,
              subnet: IPAddress = None) -> int:
        return 1

    @staticmethod
    def hardwareStatus() -> int:
        return 0

    @staticmethod
    def linkStatus() -> int:
        return 0

    @staticmethod
    def localIP() -> IPAddress:
        return IPAddress(1, 2, 3, 4)

    @staticmethod
    def maintain() -> int:
        return 0

class EthernetClient:
    def print(self, message: Any) -> None:
        pass

    def println(self, message: Any) -> None:
        pass

    def available(self) -> int:
        return 1

    def read(self, buffer: List[byte], size: int) -> int:
        return 1

    def read(self) -> int:
        return 1

    def flush(self) -> None:
        pass

    def write(self, buffer: List[byte], size: int) -> None:
        pass

    def connected(self) -> bool:
        return True

    def stop(self) -> None:
        pass

    def readStringUntil(self, character: str) -> str:
        return ""

    def connect(self, address: IPAddress, port: int) -> bool:
        return True

class EthernetServer:
    def __init__(self, port: int):
        pass

    def begin(self) -> None:
        pass

    def accept(self) -> EthernetClient:
        return EthernetClient()

    def available(self) -> EthernetClient:
        return EthernetClient()

    def write(self, data: byte) -> None:
        pass

    def print(self, message: Any) -> None:
        pass

    def println(self, message: Any) -> None:
        pass

    def flush(self) -> None:
        pass

class EthernetUDP:
    def begin(self, port: int) -> None:
        pass

    def parsePacket(self) -> int:
        return 0

    def read(self, buffer: List[Any], size: int) -> None:
        pass

    def beginPacket(self, address: Any, port: int) -> None:
        pass

    def write(self, address: List[Any], size: int = 0) -> None:
        pass

    def endPacket(self) -> None:
        pass

    def remoteIP(self) -> IPAddress:
        pass

    def remotePort(self) -> int:
        return 0
