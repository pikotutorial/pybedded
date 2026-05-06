import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    RS: int = 12
    EN: int = 11
    D4: int = 5
    D5: int = 4
    D6: int = 3
    D7: int = 2

    lcd: LiquidCrystal = LiquidCrystal(RS, EN, D4, D5, D6, D7)

    def setup() -> None:
        lcd.begin(16, 2)
        lcd.print("Hello, world!")

    def loop() -> None:
        lcd.noBlink()
        delay(3000)

        lcd.blink()
        delay(3000)
