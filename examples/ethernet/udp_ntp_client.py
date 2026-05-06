import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    NTP_PACKET_SIZE: int = 48

    mac: List[byte] = [0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED]
    local_port: unsigned_int = 8888
    time_server: List[char] = ["time.nist.gov"]
    packet_buffer: List[byte] = [] # size=NTP_PACKET_SIZE
    udp: EthernetUDP = EthernetUDP()

    def sendNTPpacket(address: List[char]) -> None:
        memset(packet_buffer, 0, NTP_PACKET_SIZE)

        packet_buffer[0] = 0b11100011
        packet_buffer[1] = 0
        packet_buffer[2] = 6
        packet_buffer[3] = 0xEC

        packet_buffer[12] = 49
        packet_buffer[13] = 0x4E
        packet_buffer[14] = 49
        packet_buffer[15] = 52

        udp.beginPacket(address, 123)
        udp.write(packet_buffer, NTP_PACKET_SIZE)
        udp.endPacket()

    def setup() -> None:
        Serial.begin(9600)
        while not Serial:
            pass

        if Ethernet.begin(mac) == 0:
            Serial.println("Failed to configure Ethernet using DHCP")

            if Ethernet.hardwareStatus() == EthernetNoHardware:
                Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(")
            elif Ethernet.linkStatus() == LinkOFF:
                Serial.println("Ethernet cable is not connected.")

            while True:
                delay(1)

        udp.begin(local_port)

    def loop() -> None:
        sendNTPpacket(time_server)
        delay(1000)

        if udp.parsePacket():
            udp.read(packet_buffer, NTP_PACKET_SIZE)

            high_word: unsigned_long = word(packet_buffer[40], packet_buffer[41])
            low_word: unsigned_long = word(packet_buffer[42], packet_buffer[43])
            secs_since_1900: unsigned_long = high_word << 16 | low_word

            Serial.print("Seconds since Jan 1 1900 = ")
            Serial.println(secs_since_1900)
            Serial.print("Unix time = ")

            seventy_years: unsigned_long = 2208988800
            epoch: unsigned_long = secs_since_1900 - seventy_years

            Serial.println(epoch)

            Serial.print("The UTC time is ")
            Serial.print((epoch % 86400) / 3600)
            Serial.print(':')

            if ((epoch % 3600) / 60) < 10:
                Serial.print('0')

            Serial.print((epoch % 3600) / 60)
            Serial.print(':')

            if (epoch % 60) < 10:
                Serial.print('0')

            Serial.println(epoch % 60)

        delay(10000)
        Ethernet.maintain()
