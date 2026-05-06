"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/basics/ReadAnalogVoltage
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        Serial.begin(9600)

    def loop() -> None:
        sensor_value: int = analogRead(A0)
        voltage: float = sensor_value * (5.0 / 1023.0)

        Serial.println(voltage)
