import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    PRESSURE: int = 0x1F
    PRESSURE_LSB: int = 0x20
    TEMPERATURE: int = 0x21
    READ: byte = 0b11111100
    WRITE: byte = 0b00000010

    DATA_READY_PIN: int = 6
    CHIP_SELECT_PIN: int = 7

    def write_register(this_register: byte, value: byte) -> None:
        this_register = this_register << 2
        data_to_send: byte = this_register | WRITE

        digitalWrite(CHIP_SELECT_PIN, LOW)

        SPI.transfer(data_to_send)
        SPI.transfer(value)

        digitalWrite(CHIP_SELECT_PIN, HIGH)

    def read_register(this_register: byte, bytes_to_read: int) -> unsigned_int:
        Serial.print(this_register, BIN)
        Serial.print("\t")

        this_register = this_register << 2
        data_to_send: byte = this_register & READ
        Serial.println(this_register, BIN)

        digitalWrite(CHIP_SELECT_PIN, LOW)
        SPI.transfer(data_to_send)
        result: unsigned_int = SPI.transfer(0x00)

        bytes_to_read -= 1

        if bytes_to_read > 0:
            result = result << 8
            in_byte: byte = SPI.transfer(0x00)
            result = result | in_byte
            bytes_to_read -= 1

        digitalWrite(CHIP_SELECT_PIN, HIGH)

        return result

    def setup() -> None:
        Serial.begin(9600)
        SPI.begin()

        pinMode(DATA_READY_PIN, INPUT)
        pinMode(CHIP_SELECT_PIN, OUTPUT)

        write_register(0x02, 0x2D)
        write_register(0x01, 0x03)
        write_register(0x03, 0x02)

        delay(100)

    def loop() -> None:
        write_register(0x03, 0x0A)

        if digitalRead(DATA_READY_PIN) == HIGH:
            temp_data: int = read_register(0x21, 2)
            real_temp: float = temp_data/20.0
            Serial.print("Temp[C]=")
            Serial.print(real_temp)

            pressure_data_high: byte = read_register(0x1F, 1)
            pressure_data_high &= 0b00000111

            pressure_data_low: unsigned_int = read_register(0x20, 2)
            pressure: long = ((pressure_data_high << 16) | pressure_data_low) / 4

            Serial.println("\tPressure [Pa]=" + String(pressure))
