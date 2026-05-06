import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    STEPS_PER_REVOLUTION: int = 200
    my_stepper: Stepper = Stepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11)
    step_count: int = 0

    def setup() -> None:
        Serial.begin(9600)

    def loop() -> None:
        global step_count

        my_stepper.step(1)
        Serial.print("steps:")
        Serial.println(step_count)
        step_count += 1
        delay(500)
