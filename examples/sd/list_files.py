import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    root: File = File()

    def print_directory(dir: File, num_tabs: int) -> None:
        while True:
            entry: File = dir.openNextFile()

            if not entry:
                break

            for i in range(num_tabs):
                Serial.print("\t")
            Serial.print(entry.name())

            if entry.isDirectory():
                Serial.println("/")
                print_directory(entry, num_tabs + 1)
            else:
                Serial.print("\t\t")
                Serial.println(entry.size(), DEC)

            entry.close()

    def setup() -> None:
        global root

        Serial.begin(9600)
        while not Serial:
            pass

        Serial.println("Initializing SD card...")

        if not SD.begin(4):
            Serial.println("Initialization failed!")
            while True:
                pass

        Serial.println("Initialization done.")

        root = SD.open("/")

        print_directory(root, 0)

        Serial.println("Done!")

    def loop() -> None:
        pass
