import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    STEPS_PER_REVOLUTION: int = 200
    my_stepper: Stepper = Stepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11)

    def setup() -> None:
        pass

    def loop() -> None:
        sensor_reading: int = analogRead(A0)
        motor_speed: int = map(sensor_reading, 0, 1023, 0, 100)

        if motor_speed > 0:
            my_stepper.setSpeed(motor_speed)
            my_stepper.step(STEPS_PER_REVOLUTION / 100)
