"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/InputPullupSerial
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    def setup() -> None:
        Serial.begin(9600)
        pinMode(2, INPUT_PULLUP)
        pinMode(13, OUTPUT)

    def loop() -> None:
        sensor_val: int = digitalRead(2)
        Serial.println(sensor_val)

        if sensor_val == HIGH:
            digitalWrite(13, LOW)
        else:
            digitalWrite(13, HIGH)
