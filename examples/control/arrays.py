import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    timer: int = 100
    led_pins: List[int] = [2, 7, 4, 6, 5, 3]
    pin_count: int = 6

    def setup() -> None:
        for this_pin in range(pin_count):
            pinMode(led_pins[this_pin], OUTPUT)

    def loop() -> None:
        for this_pin in range(pin_count):
            digitalWrite(led_pins[this_pin], HIGH)
            delay(timer)
            digitalWrite(led_pins[this_pin], LOW)

        for this_pin in range(pin_count - 1, 0, -1):
            digitalWrite(led_pins[this_pin], HIGH)
            delay(timer)
            digitalWrite(led_pins[this_pin], LOW)
