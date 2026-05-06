import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def receive_event(how_many: int) -> None:
        while Wire.available():
            c: char = Wire.read()
            Serial.print(c)

        x: int = Wire.read()
        Serial.println(x)

    def setup() -> None:
        Wire.begin(8)
        Wire.onReceive(receive_event)
        Serial.begin(9600)

    def loop() -> None:
        delay(100)
