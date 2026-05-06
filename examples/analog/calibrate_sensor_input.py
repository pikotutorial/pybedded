"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/Calibration
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    SENSOR_PIN: int = A0
    LED_PIN: int = 9

    sensor_value: int = 0
    sensor_min: int = 1023
    sensor_max: int = 0

    def setup() -> None:
        global sensor_value, sensor_max, sensor_min

        pinMode(13, OUTPUT)
        digitalWrite(13, HIGH)

        while millis() < 5000:
            sensor_value = analogRead(SENSOR_PIN)

            if sensor_value > sensor_max:
                sensor_max = sensor_value
            if sensor_value < sensor_min:
                sensor_min = sensor_value

        digitalWrite(13, LOW)

    def loop() -> None:
        global sensor_value

        sensor_value = analogRead(SENSOR_PIN)
        sensor_value = constrain(sensor_value, sensor_min, sensor_max)
        sensor_value = map(sensor_value, sensor_min, sensor_max, 0, 255)

        analogWrite(LED_PIN, sensor_value)
