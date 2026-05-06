import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        Ethernet.init(10)
        Serial.begin(9600)

    def loop() -> None:
        link: int = Ethernet.linkStatus()
        Serial.print("Link status: ")

        if link == Unknown:
            Serial.println("Unknown")
        elif link == LinkON:
            Serial.println("ON")
        elif link == LinkOFF:
            Serial.println("OFF")

        delay(1000)
