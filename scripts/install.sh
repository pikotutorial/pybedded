#!/bin/bash

set -e

SCRIPTS_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPO_DIR="$SCRIPTS_DIR/.."
VENV_DIR="$REPO_DIR/venv"
INTERPRETER_PATH="$REPO_DIR/venv/bin/python3"

echo "Creating Python virtual environment"
python3 -m venv $VENV_DIR
$INTERPRETER_PATH -m pip install -r $REPO_DIR/requirements.txt

echo "Installing arduino-cli"
sudo snap install arduino-cli

echo "Configuring arduino-cli (connected Arduino required)"
sudo snap connect arduino-cli:raw-usb
sudo snap set system experimental.hotplug=true
sudo systemctl restart snapd
sudo snap connect arduino-cli:serial-port

echo "Installing Arduino boards"
arduino-cli core install arduino:avr

echo "Installing Arduino libraries"
arduino-cli lib install Servo
arduino-cli lib install LiquidCrystal
arduino-cli lib install SD
arduino-cli lib install Stepper
arduino-cli lib install Ethernet
arduino-cli lib install Keyboard

echo "Done"
