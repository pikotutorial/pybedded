import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    myservo: Servo = Servo()

    potpin: int = A0
    val: int = 0

    def setup() -> None:
        myservo.attach(9)

    def loop() -> None:
        global val

        val = analogRead(potpin)
        val = map(val, 0, 1023, 0, 180)
        myservo.write(val)
        delay(15)
