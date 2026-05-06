import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    myservo: Servo = Servo()
    pos: int = 0

    def setup() -> None:
        myservo.attach(9)

    def loop() -> None:
        for pos in range(180):
            myservo.write(pos)
            delay(15)
        for pos in range(180, 0, -1):
            myservo.write(pos)
            delay(15)
