import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]

    ip: IPAddress = IPAddress(192, 168, 1, 177)
    server: IPAddress = IPAddress(1, 1, 1, 1)
    client: EthernetClient = EthernetClient()

    def setup() -> None:
        Ethernet.init(10)

        Serial.begin(9600)
        while not Serial:
            pass

        if Ethernet.hardwareStatus() == EthernetNoHardware:
            Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(")
            while True:
                delay(1)

        while Ethernet.linkStatus() == LinkOFF:
            Serial.println("Ethernet cable is not connected.")
            delay(500)

        delay(1000)
        Serial.println("connecting...")

        if client.connect(server, 10002):
            Serial.println("connected")
        else:
            Serial.println("connection failed")

    def loop() -> None:
        if client.available():
            c: byte = client.read()
            Serial.print(c)

        while Serial.available():
            in_char: byte = Serial.read()

            if client.connected():
                client.print(in_char)

        if not client.connected():
            Serial.println("")
            Serial.println("disconnecting")
            client.stop()

            while True:
                delay(1)
