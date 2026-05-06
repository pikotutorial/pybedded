"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/MultiSerialMega
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.MEGA, upload=upload_sketch):
    def setup() -> None:
        Serial.begin(9600)
        Serial1.begin(9600)

    def loop() -> None:
        if Serial1.available():
            in_byte: int = Serial1.read()
            Serial1.write(in_byte)

        if Serial.available():
            in_byte: int = Serial.read()
            Serial.write(in_byte)
