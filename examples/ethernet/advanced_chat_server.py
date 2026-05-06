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
    clients: List[EthernetClient] = [] # size=8

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
        new_client: EthernetClient = server.accept()

        if new_client:
            for i in range(8):
                if not clients[i]:
                    Serial.print("We have a new client #")
                    Serial.println(i)

                    new_client.print("Hello, client number: ")
                    new_client.println(i)

                    clients[i] = new_client
                    break

        for i in range(8):
            if clients[i] and clients[i].available():
                buffer: List[byte] = [] # size=80
                count: int = clients[i].read(buffer, 80)

                for j in range(8):
                    if j != i and clients[j].connected():
                        clients[j].write(buffer, count)

        for i in range(8):
            if clients[i] and not clients[i].connected():
                Serial.print("Disconnect client #")
                Serial.println(i)
                clients[i].stop()
