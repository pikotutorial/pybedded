import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    sensor_pin: int = A0
    led_pin: int = 9
    indicator_led_pin: int = 13
    button_pin: int = 2

    sensor_min: int = 1023
    sensor_max: int = 0
    sensor_value: int = 0

    def calibrate() -> None:
        global sensor_value, sensor_min, sensor_max

        digitalWrite(indicator_led_pin, HIGH)
        sensor_value = analogRead(A0)

        if sensor_value > sensor_max:
            sensor_max = sensor_value
        if sensor_value < sensor_min:
            sensor_min = sensor_value

    def setup() -> None:
        pinMode(indicator_led_pin, OUTPUT)
        pinMode(led_pin, OUTPUT)
        pinMode(button_pin, INPUT)

    def loop() -> None:
        global sensor_value

        while digitalRead(button_pin) == HIGH:
            calibrate()

        digitalWrite(indicator_led_pin, LOW)
        sensor_value = analogRead(A0)
        sensor_value = map(sensor_value, sensor_min, sensor_max, 0, 255)
        sensor_value = constrain(sensor_value, 0, 255)

        analogWrite(led_pin, sensor_value)
