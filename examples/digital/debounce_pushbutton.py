"""
The C++ equivalent is available at https://docs.arduino.cc/built-in-examples/digital/Debounce
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    BUTTON_PIN: int = 2
    LED_PIN: int = 13

    led_state: int = HIGH
    button_state: int = LOW
    last_button_state: int = LOW

    last_debounce_time: unsigned_long = 0
    debounce_delay: unsigned_long = 50

    def setup() -> None:
        pinMode(BUTTON_PIN, INPUT)
        pinMode(LED_PIN, OUTPUT)

        digitalWrite(LED_PIN, led_state)

    def loop() -> None:
        global last_debounce_time, button_state, led_state, last_button_state

        reading: int = digitalRead(BUTTON_PIN)

        if reading != last_button_state:
            last_debounce_time = millis()

        if (millis() - last_debounce_time) > debounce_delay:
            if reading != button_state:
                button_state = reading

                if button_state == HIGH:
                    led_state = not led_state

        digitalWrite(LED_PIN, led_state)
        last_button_state = reading
