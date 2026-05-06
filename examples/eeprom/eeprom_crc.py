import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def eeprom_crc() -> int:
        crc_table: List[unsigned_long] = [0x00000000, 0x1db71064, 0x3b6e20c8, 0x26d930ac, 0x76dc4190, 0x6b6b51f4, 0x4db26158, 0x5005713c, 0xedb88320, 0xf00f9344, 0xd6d6a3e8, 0xcb61b38c, 0x9b64c2b0, 0x86d3d2d4, 0xa00ae278, 0xbdbdf21c]

        crc: unsigned_long = ~0

        for index in range(EEPROM.length()):
            crc = crc_table[(crc ^ EEPROM[index]) & 0x0F] ^ (crc >> 4)
            crc = crc_table[(crc ^ (EEPROM[index] >> 4)) & 0x0f] ^ (crc >> 4)
            crc = ~crc

        return crc

    def setup() -> None:
        Serial.begin(9600)

        Serial.print("EEPROM length: ")
        Serial.println(EEPROM.length())

        Serial.print("CRC of EEPROM data: 0x")
        Serial.println(eeprom_crc(), HEX)
        Serial.print("\n\nDone!")

    def loop() -> None:
        pass
