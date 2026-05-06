import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    STEPS: int = 100
    stepper: Stepper = Stepper(STEPS, 8, 9, 10, 11)
    previous: int = 0

    def setup() -> None:
        stepper.setSpeed(30)

    def loop() -> None:
        global previous

        val: int = analogRead(0)
        stepper.step(val - previous)

        previous = val
