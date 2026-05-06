import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]

    ip: IPAddress = IPAddress(192, 168, 1, 177)
    my_dns: IPAddress = IPAddress(192, 168, 1, 1)
    gateway: IPAddress = IPAddress(192, 168, 1, 1)
    subnet: IPAddress = IPAddress(255, 255, 0, 0)

    server: EthernetServer = EthernetServer(23)
    already_connected: bool = False

    def setup() -> None:
        Ethernet.init(10)
        Ethernet.begin(mac, ip, my_dns, gateway, subnet)

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

        Serial.print("Chat server address:")
        Serial.println(Ethernet.localIP())

    def loop() -> None:
        global already_connected

        client: EthernetClient = server.available()

        if client:
            if not already_connected:
                client.flush()

                Serial.println("We have a new client")
                client.println("Hello, client!")
                already_connected = True

            if client.available():
                this_char: byte = client.read()
                server.write(this_char)
                Serial.write(this_char)
