import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]

    ip: IPAddress = IPAddress(192, 168, 1, 177)
    local_port: unsigned_int = 8888
    packet_buffer: List[char] = [] # size=UDP_TX_PACKET_MAX_SIZE
    reply_buffer: List[char] = ["acknowledged"]
    udp: EthernetUDP = EthernetUDP()

    def setup() -> None:
        Ethernet.begin(mac, ip)

        Serial.begin(9600)
        while not Serial:
            pass

        if Ethernet.hardwareStatus() == EthernetNoHardware:
            Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(")
            while True:
                delay(1)
        elif Ethernet.linkStatus() == LinkOFF:
            Serial.println("Ethernet cable is not connected.")

        udp.begin(local_port)

    def loop() -> None:
        packet_size: int = udp.parsePacket()

        if packet_size:
            Serial.print("Received packet of size")
            Serial.println(packet_size)
            Serial.print("From ")
            remote: IPAddress = udp.remoteIP()

            for i in range(4):
                Serial.print(remote[i], DEC)

                if i < 3:
                    Serial.print(".")

            Serial.print(", port ")
            Serial.println(udp.remotePort())

            udp.read(packet_buffer, UDP_TX_PACKET_MAX_SIZE)
            Serial.println("Contents:")
            Serial.println(packet_buffer)

            udp.beginPacket(udp.remoteIP(), udp.remotePort())
            udp.write(reply_buffer)
            udp.endPacket()

        delay(10)
