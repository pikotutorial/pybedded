import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        Wire.begin()
        Serial.begin(9600)

    def loop() -> None:
        Wire.requestFrom(8, 6)

        while Wire.available():
            c: char = Wire.read()
            Serial.print(c)

        delay(500)
