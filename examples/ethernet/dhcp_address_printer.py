import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]

    def setup() -> None:
        Ethernet.init(10)

        Serial.begin(9600)

        Serial.println("Initialize Ethernet with DHCP:")
        if Ethernet.begin(mac) == 0:
            Serial.println("Failed to configure Ethernet using DHCP")
            if Ethernet.hardwareStatus() == EthernetNoHardware:
                Serial.println("Ethernet shield was not found.Sorry, can't run without hardware. :(")
            elif Ethernet.linkStatus() == LinkOFF:
                Serial.println("Ethernet cable is not connected")

            while True:
                delay(1)

        Serial.print("My IP address: ")
        Serial.println(Ethernet.localIP())

    def loop() -> None:
        if Ethernet.maintain() == 1:
            Serial.println("Error: renewed fail")
        elif Ethernet.maintain() == 2:
            Serial.println("Renewed success")
            Serial.print("My IP address: ")
            Serial.println(Ethernet.localIP())
        elif Ethernet.maintain() == 3:
            Serial.println("Error: rebind fail")
        elif Ethernet.maintain() == 4:
            Serial.println("Rebind success")
            Serial.print("My IP address: ")
            Serial.println(Ethernet.localIP())
        else:
            pass
