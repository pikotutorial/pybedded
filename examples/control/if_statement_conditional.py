import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    analog_pin: int = A0
    led_pin: int = 13
    threshold: int = 400

    def setup() -> None:
        pinMode(led_pin, OUTPUT)
        Serial.begin(9600)

    def loop() -> None:
        analog_value: int = analogRead(analog_pin)

        if analog_value > threshold:
            digitalWrite(led_pin, HIGH)
        else:
            digitalWrite(led_pin, LOW)

        Serial.println(analog_value)
        delay(1)
