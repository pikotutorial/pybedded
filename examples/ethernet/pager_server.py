import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]

    ip: IPAddress = IPAddress(192, 168, 1, 177)

    server: EthernetServer = EthernetServer(2323)

    def setup() -> None:
        Serial.begin(9600)
        while not Serial:
            pass

        Serial.println("Initialize Ethernet with DHCP:")
        if Ethernet.begin(mac) == 0:
            Serial.println("Failed to configure Ethernet using DHCP")

            if Ethernet.hardwareStatus() == EthernetNoHardware:
                Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(")
                while True:
                    delay(1)

            if Ethernet.linkStatus() == LinkOFF:
                Serial.println("Ethernet cable is not connected.")

            Ethernet.begin(mac, ip)
        else:
            Serial.print("  DHCP assigned IP ")
            Serial.println(Ethernet.localIP())

        server.begin()

        ip: IPAddress = Ethernet.localIP()
        Serial.println("")
        Serial.print("To access the server, connect with Telnet client to ")
        Serial.print(ip)
        Serial.println(" 2323")

    def loop() -> None:
        client: EthernetClient = server.available()

        if client:
            s: str = client.readStringUntil('\n')
            s.trim()
            Serial.println(s)
            client.print("echo: ")
            server.println(s)

            IFNDEF("ARDUINO_ARCH_SAM")
            server.flush()
            ENDIF()
