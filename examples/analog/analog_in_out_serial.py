"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/AnalogInOutSerial
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    ANALOG_IN_PIN: int = A0
    ANALOG_OUT_PIN: int = 9

    sensor_value: int = 0
    output_value: int = 0

    def setup() -> None:
        Serial.begin(9600)

    def loop() -> None:
        global sensor_value, output_value

        sensor_value = analogRead(ANALOG_IN_PIN)
        output_value = map(sensor_value, 0, 1023, 0, 255)

        analogWrite(ANALOG_OUT_PIN, output_value)

        Serial.print("sensor = ")
        Serial.print(sensor_value)
        Serial.print("\t output = ")
        Serial.println(output_value)

        delay(2)
