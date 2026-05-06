import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src import *

upload_sketch: bool = not (len(sys.argv) == 2 and sys.argv[1] == "--no-upload")

with ArduinoBoard("/dev/ttyUSB0", Board.UNO, upload=upload_sketch):
    card: Sd2Card = Sd2Card()
    volume: SdVolume = SdVolume()
    root: SdFile = SdFile()

    CHIP_SELECT: int = 4

    def setup() -> None:
        Serial.begin(9600)

        while not Serial:
            pass

        Serial.print("\nInitializing SD card...")

        if not card.init(SPI_HALF_SPEED, CHIP_SELECT):
            Serial.println("initialization failed. Things to check:")
            Serial.println("* is a card inserted?")
            Serial.println("* is your wiring correct?")
            Serial.println("* did you change the chipSelect pin to match your shield or module?")

            while 1:
                pass
        else:
            Serial.println("Wiring is correct and a card is present.")

        Serial.println("")
        Serial.print("Card type:         ")

        if card.type() == SD_CARD_TYPE_SD1:
            Serial.println("SD1")
        elif card.type() == SD_CARD_TYPE_SD2:
            Serial.println("SD2")
        elif card.type() == SD_CARD_TYPE_SDHC:
            Serial.println("SDHC")
        else:
            Serial.println("Unknown")

        if not volume.init(card):
            Serial.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card")

            while 1:
                pass

        Serial.print("Clusters:          ")
        Serial.println(volume.clusterCount())
        Serial.print("Blocks x Cluster:  ")
        Serial.println(volume.blocksPerCluster())

        Serial.print("Total Blocks:      ")
        Serial.println(volume.blocksPerCluster() * volume.clusterCount())
        Serial.println("")

        Serial.print("Volume type is:    FAT")
        Serial.println(volume.fatType(), DEC)

        volume_size: int = volume.blocksPerCluster()
        volume_size *= volume.clusterCount()
        volume_size /= 2

        Serial.print("Volume size (Kb):  ")
        Serial.println(volume_size)
        Serial.print("Volume size (Mb):  ")
        volume_size /= 1024
        Serial.println(volume_size)

        Serial.println("\nFiles found on the card (name, date and size in bytes): ")
        root.openRoot(volume)
        root.ls(LS_R | LS_DATE | LS_SIZE)

    def loop() -> None:
        pass
