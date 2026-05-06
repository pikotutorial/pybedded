"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/DigitalReadSerial
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    push_button: int = 2

    def setup() -> None:
        Serial.begin(9600)
        pinMode(push_button, INPUT)

    def loop() -> None:
        button_state: int = digitalRead(push_button)
        Serial.println(button_state)
        delay(1)
