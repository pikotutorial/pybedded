import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    val: byte = 0

    def setup() -> None:
        Wire.begin()

    def loop() -> None:
        global val

        Wire.beginTransmission(44)
        Wire.write(byte(0x00))
        Wire.write(val)
        Wire.endTransmission()

        val += 1

        if val == 64:
            val = 0

        delay(500)
