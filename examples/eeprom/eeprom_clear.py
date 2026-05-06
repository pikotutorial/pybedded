import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        pinMode(13, OUTPUT)

        for i in range(EEPROM.length()):
            EEPROM.write(i, 0)

        digitalWrite(13, HIGH)

    def loop() -> None:
        pass
