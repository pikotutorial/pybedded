"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/communication/Dimmer
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    LED_PIN: int = 9

    def setup() -> None:
        Serial.begin(9600)
        pinMode(LED_PIN, OUTPUT)

    def loop() -> None:
        if Serial.available():
            brightness: byte = Serial.read()
            analogWrite(LED_PIN, brightness)
