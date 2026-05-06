"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/analog/Smoothing
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    NUM_READINGS: int = 10

    readings: List[int] = [] # size=NUM_READINGS
    read_index: int = 0
    total: int = 0
    average: int = 0
    input_pin: int = A0

    def setup() -> None:
        Serial.begin(9600)

        for this_reading in range(NUM_READINGS):
            readings[this_reading] = 0

    def loop() -> None:
        global total, read_index, average

        total = total - readings[read_index]
        readings[read_index] = analogRead(input_pin)
        total = total + readings[read_index]
        read_index = read_index + 1

        if read_index >= NUM_READINGS:
            read_index = 0

        average = total / NUM_READINGS
        Serial.println(average)
        delay(1)
