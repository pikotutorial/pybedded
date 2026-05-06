"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    x: byte = 0

    def setup() -> None:
        Wire.begin()

    def loop() -> None:
        global x

        Wire.beginTransmission(8)
        Wire.write("x is ")
        Wire.write(x)
        Wire.endTransmission()

        x += 1
        delay(500)
