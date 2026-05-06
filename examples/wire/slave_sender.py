"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def request_event() -> None:
        Wire.write("hello ")

    def setup() -> None:
        Wire.begin(8)
        Wire.onRequest(request_event)

    def loop() -> None:
        delay(100)
