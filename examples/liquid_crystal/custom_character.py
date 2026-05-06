"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/BareMinimum
"""
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

    heart: List[byte] = [0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000]
    smiley: List[byte] = [0b00000, 0b00000, 0b01010, 0b00000, 0b00000, 0b10001, 0b01110, 0b00000]
    frownie: List[byte] = [0b00000, 0b00000, 0b01010, 0b00000, 0b00000, 0b00000, 0b01110, 0b10001]
    arms_down: List[byte] = [0b00100, 0b01010, 0b00100, 0b00100, 0b01110, 0b10101, 0b00100, 0b01010]
    arms_up: List[byte] = [0b00100, 0b01010, 0b00100, 0b10101, 0b01110, 0b00100, 0b00100, 0b01010]

    def setup() -> None:
        lcd.begin(16, 2)

        lcd.createChar(0, heart)
        lcd.createChar(1, smiley)
        lcd.createChar(2, frownie)
        lcd.createChar(3, arms_down)
        lcd.createChar(4, arms_up)

        lcd.setCursor(0, 0)

        lcd.print("I ")
        lcd.write(byte(0))
        lcd.print(" Arduino! ")
        lcd.write(byte(1))

    def loop() -> None:
        sensor_reading: int = analogRead(A0)
        delay_time: int = map(sensor_reading, 0, 1023, 200, 1000)

        lcd.setCursor(4, 1)
        lcd.write(3)
        delay(delay_time)

        lcd.setCursor(4, 1)
        lcd.write(4)
        delay(delay_time)
