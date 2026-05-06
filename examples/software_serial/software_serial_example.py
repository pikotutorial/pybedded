import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    my_serial: SoftwareSerial = SoftwareSerial(10, 11)

    def setup() -> None:
        Serial.begin(57600)
        while not Serial:
            pass

        Serial.println("Goodnight moon!")

        my_serial.begin(4800)
        my_serial.println("Hello, world?")

    def loop() -> None:
        if my_serial.available():
            Serial.write(my_serial.read())
        if Serial.available():
            my_serial.write(Serial.read())
