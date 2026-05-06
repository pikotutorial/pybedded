import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    port_one: SoftwareSerial = SoftwareSerial(10, 11)
    port_two: SoftwareSerial = SoftwareSerial(8, 9)

    def setup() -> None:
        Serial.begin(9600)
        while not Serial:
            pass

        port_one.begin(9600)
        port_two.begin(9600)

    def loop() -> None:
        port_one.listen()
        Serial.println("Data from port one:")

        while port_one.available():
            in_byte: byte = port_one.read()
            Serial.write(in_byte)

        Serial.println("")

        port_two.listen()
        Serial.println("Data from port two:")

        while port_two.available():
            in_byte: byte = port_two.read()
            Serial.write(in_byte)

        Serial.println("")
