import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        Serial.begin(9600)
        Keyboard.begin()

    def loop() -> None:
        if Serial.available():
            in_char: char = Serial.read()
            Keyboard.write(in_char + 1)
