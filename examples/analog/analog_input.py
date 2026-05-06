"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/AnalogInput
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    sensor_pin: int = A0
    led_pin: int = 13
    sensor_value: int = 0

    def setup() -> None:
        pinMode(led_pin, OUTPUT)

    def loop() -> None:
        global sensor_value

        sensor_value = analogRead(sensor_pin)
        digitalWrite(led_pin, HIGH)
        delay(sensor_value)

        digitalWrite(led_pin, LOW)
        delay(sensor_value)
