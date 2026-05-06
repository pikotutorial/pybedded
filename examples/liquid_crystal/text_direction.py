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
    this_char: char = 'a'

    def setup() -> None:
        lcd.begin(16, 2)
        lcd.cursor()

    def loop() -> None:
        global this_char

        if this_char == 'm':
            lcd.rightToLeft()

        if this_char == 's':
            lcd.leftToRight()

        if this_char > 'z':
            lcd.home()
            this_char = 'a'

        lcd.write(this_char)
        delay(1000)
        this_char += 1
