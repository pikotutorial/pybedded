"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/PhysicalPixel
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    incoming_byte: int = 0

    def setup() -> None:
        Serial.begin(9600)
        pinMode(LED_BUILTIN, OUTPUT)

    def loop() -> None:
        global incoming_byte

        if Serial.available():
            incoming_byte = Serial.read()

            if incoming_byte == 'H':
                digitalWrite(LED_BUILTIN, HIGH)
            if incoming_byte == 'L':
                digitalWrite(LED_BUILTIN, LOW)
