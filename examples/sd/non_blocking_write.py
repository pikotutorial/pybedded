import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    filename: List[char] = ["demo.txt"]
    txt_file: File = File()
    buffer: str = ""
    last_millis: unsigned_long = 0

    def setup() -> None:
        global txt_file

        Serial.begin(9600)
        while not Serial:
            pass

        buffer.reserve(1024)
        pinMode(LED_BUILTIN, OUTPUT)

        if not SD.begin(4):
            Serial.println("Card failed or not present")
            while True:
                pass

        txt_file = SD.open(filename, FILE_WRITE)

        if not txt_file:
            Serial.print("Error opening ")
            Serial.println(filename)

            while True:
                pass

        txt_file.println("")
        txt_file.println("Hello world!")

    def loop() -> None:
        global buffer, last_millis

        now: unsigned_long = millis()

        if now - last_millis >= 10:
            buffer += "Hello "
            buffer += now
            buffer += "\r\n"

            last_millis = now

        chunk_size: unsigned_int = txt_file.availableForWrite()

        if chunk_size and buffer.length() >= chunk_size:
            digitalWrite(LED_BUILTIN, HIGH)
            txt_file.write(buffer.c_str(), chunk_size)
            digitalWrite(LED_BUILTIN, LOW)

            buffer.remove(0, chunk_size)
