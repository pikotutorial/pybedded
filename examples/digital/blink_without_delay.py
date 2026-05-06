"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/BlinkWithoutDelay
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    led_pin: int = LED_BUILTIN
    led_state: int = LOW
    previous_millis: unsigned_long = 0
    interval: long = 1000

    def setup() -> None:
        pinMode(led_pin, OUTPUT)

    def loop() -> None:
        global previous_millis, led_state

        current_millis: unsigned_long = millis()

        if current_millis - previous_millis >= interval:
            previous_millis = current_millis

            if led_state == LOW:
                led_state = HIGH
            else:
                led_state = LOW

            digitalWrite(led_pin, led_state)
