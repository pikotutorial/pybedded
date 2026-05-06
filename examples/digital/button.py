"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/Button
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    BUTTON_PIN: int = 2
    LED_PIN: int = 13

    button_state: int = 0

    def setup() -> None:
        pinMode(LED_PIN, OUTPUT)
        pinMode(BUTTON_PIN, INPUT)

    def loop() -> None:
        global button_state

        button_state = digitalRead(BUTTON_PIN)

        if button_state == HIGH:
            digitalWrite(LED_PIN, HIGH)
        else:
            digitalWrite(LED_PIN, LOW)
