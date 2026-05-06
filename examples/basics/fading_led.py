"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/Fade
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    led: int = 9
    brightness: int = 0
    fade_amount: int = 5

    def setup() -> None:
        pinMode(led, OUTPUT)

    def loop() -> None:
        global brightness, fade_amount

        analogWrite(led, brightness)
        brightness = brightness + fade_amount

        if brightness <= 0 or brightness >= 255:
            fade_amount = -fade_amount

        delay(30)
