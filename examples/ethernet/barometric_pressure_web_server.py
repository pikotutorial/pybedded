import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]
    ip: IPAddress = IPAddress(192, 168, 1, 20)
    server: EthernetServer = EthernetServer(80)
    PRESSURE: int = 0x1F
    PRESSURE_LSB: int = 0x20
    TEMPERATURE: int = 0x21
    DATA_READY_PIN: int = 6
    CHIP_SELECT_PIN: int = 7

    temperature: float = 0.0
    pressure: int = 0
    last_reading_time: long = 0

    def get_data() -> None:
        global temperature, pressure

        Serial.println("Getting reading")

        temp_data: int = read_register(0x21, 2)
        temperature = temp_data/20.0
        pressure_data_high: byte = read_register(0x1F, 1)
        pressure_data_high &= 0b00000111
        pressure_data_low: unsigned_int = read_register(0x20, 2)
        pressure = ((pressure_data_high << 16) | pressure_data_low) / 4

        Serial.print("Temperature: ")
        Serial.print(temperature)
        Serial.println(" degrees C")
        Serial.print("Pressure: ")
        Serial.print(pressure)
        Serial.println(" Pa")

    def listen_for_ethernet_clients() -> None:
        client: EthernetClient = server.available()

        if client:
            Serial.println("Got a client")

            current_link_is_blank: bool = True

            while client.connected():
                if client.available():
                    c: int = client.read()

                    if c == '\n' and current_link_is_blank:
                        client.println("HTTP/1.1 200 OK")
                        client.println("Content-Type: text/html")
                        client.println("")

                        client.print("Temperature: ")
                        client.print(temperature)
                        client.print(" degrees C")
                        client.println("<br />")
                        client.print("Pressure: ")
                        client.print(pressure)
                        client.print(" Pa")
                        client.println("<br />")
                        break
                    if c == '\n':
                        current_link_is_blank = True
                    elif c != '\r':
                        current_link_is_blank = False

        delay(1)
        client.stop()

    def write_register(register_name: byte, register_value: byte) -> None:
        register_name <<= 2
        register_name |= 0b00000010

        digitalWrite(CHIP_SELECT_PIN, LOW)
        SPI.transfer(register_name)
        SPI.transfer(register_value)
        digitalWrite(CHIP_SELECT_PIN, HIGH)

    def read_register(register_name: byte, num_bytes: int) -> unsigned_int:
        register_name <<= 2
        register_name &= 0b11111100

        digitalWrite(CHIP_SELECT_PIN, LOW)
        SPI.transfer(register_name)
        in_byte: byte = SPI.transfer(0x00)
        result: unsigned_int = in_byte

        if num_bytes > 1:
            result = in_byte << 8
            in_byte = SPI.transfer(0x00)
            result = result | in_byte

        digitalWrite(CHIP_SELECT_PIN, HIGH)
        return result

    def setup() -> None:
        Ethernet.init(10)
        Ethernet.begin(mac, ip)

        Serial.begin(9600)
        while not Serial:
            pass

        if Ethernet.hardwareStatus() == EthernetNoHardware:
            Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(")
            while True:
                delay(1)

        if Ethernet.linkStatus() == LinkOFF:
            Serial.println("Ethernet cable is not connected.")

        server.begin()

        pinMode(DATA_READY_PIN, INPUT)
        pinMode(CHIP_SELECT_PIN, OUTPUT)

        write_register(0x02, 0x2D)
        write_register(0x01, 0x03)
        write_register(0x03, 0x02)

        delay(1000)

        write_register(0x03, 0x0A)

    def loop() -> None:
        global last_reading_time

        if millis() - last_reading_time > 1000:
            if digitalRead(DATA_READY_PIN) == HIGH:
                get_data()
                last_reading_time = millis()

        listen_for_ethernet_clients()
