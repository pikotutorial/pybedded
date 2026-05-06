import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    timer: int = 100

    def setup() -> None:
        for this_pin in range(2, 8):
            pinMode(this_pin, OUTPUT)

    def loop() -> None:
        for this_pin in range(2, 8):
            digitalWrite(this_pin, HIGH)
            delay(timer)
            digitalWrite(this_pin, LOW)

        for this_pin in range(7, 2, -1):
            digitalWrite(this_pin, HIGH)
            delay(timer)
            digitalWrite(this_pin, LOW)
