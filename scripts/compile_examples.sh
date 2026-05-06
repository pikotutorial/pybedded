#!/bin/bash

set -e

SCRIPTS_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPO_DIR="$SCRIPTS_DIR/.."
VENV_DIR="$REPO_DIR/venv"
INTERPRETER_PATH="$VENV_DIR/bin/python3"

echo "---------- Compiling analog examples ----------"
echo "Compiling analog_in_out_serial"
$INTERPRETER_PATH $REPO_DIR/examples/analog/analog_in_out_serial.py --no-upload
echo "Compiling analog_input"
$INTERPRETER_PATH $REPO_DIR/examples/analog/analog_input.py --no-upload
echo "Compiling analog_write_arduino_mega"
$INTERPRETER_PATH $REPO_DIR/examples/analog/analog_write_arduino_mega.py --no-upload
echo "Compiling analog_in_outcalibrate_sensor_input_serial"
$INTERPRETER_PATH $REPO_DIR/examples/analog/calibrate_sensor_input.py --no-upload
echo "Compiling smoothing_readings_from_analog_input"
$INTERPRETER_PATH $REPO_DIR/examples/analog/smoothing_readings_from_analog_input.py --no-upload

echo "---------- Compiling basics examples ----------"
echo "Compiling analog_read_serial"
$INTERPRETER_PATH $REPO_DIR/examples/basics/analog_read_serial.py --no-upload
echo "Compiling bare_minimum_code_needed"
$INTERPRETER_PATH $REPO_DIR/examples/basics/bare_minimum_code_needed.py --no-upload
echo "Compiling blink"
$INTERPRETER_PATH $REPO_DIR/examples/basics/blink.py --no-upload
echo "Compiling digital_read_serial"
$INTERPRETER_PATH $REPO_DIR/examples/basics/digital_read_serial.py --no-upload
echo "Compiling fading_led"
$INTERPRETER_PATH $REPO_DIR/examples/basics/fading_led.py --no-upload
echo "Compiling read_analog_voltage"
$INTERPRETER_PATH $REPO_DIR/examples/basics/read_analog_voltage.py --no-upload

echo "---------- Compiling communication examples ----------"
echo "Compiling led_dimmer"
$INTERPRETER_PATH $REPO_DIR/examples/communication/led_dimmer.py --no-upload
echo "Compiling physical_pixel"
$INTERPRETER_PATH $REPO_DIR/examples/communication/physical_pixel.py --no-upload
echo "Compiling read_ascii_string"
$INTERPRETER_PATH $REPO_DIR/examples/communication/read_ascii_string.py --no-upload
echo "Compiling using_multiple_serials_on_mega"
$INTERPRETER_PATH $REPO_DIR/examples/communication/using_multiple_serials_on_mega.py --no-upload

echo "---------- Compiling control examples ----------"
echo "Compiling arrays"
$INTERPRETER_PATH $REPO_DIR/examples/control/arrays.py --no-upload
echo "Compiling for_loop_iteration"
$INTERPRETER_PATH $REPO_DIR/examples/control/for_loop_iteration.py --no-upload
echo "Compiling if_statement_conditional"
$INTERPRETER_PATH $REPO_DIR/examples/control/if_statement_conditional.py --no-upload
echo "Compiling while_statement_conditional"
$INTERPRETER_PATH $REPO_DIR/examples/control/while_statement_conditional.py --no-upload

echo "---------- Compiling digital examples ----------"
echo "Compiling blink_without_delay"
$INTERPRETER_PATH $REPO_DIR/examples/digital/blink_without_delay.py --no-upload
echo "Compiling button"
$INTERPRETER_PATH $REPO_DIR/examples/digital/button.py --no-upload
echo "Compiling debounce_pushbutton"
$INTERPRETER_PATH $REPO_DIR/examples/digital/debounce_pushbutton.py --no-upload
echo "Compiling input_pullup_serial"
$INTERPRETER_PATH $REPO_DIR/examples/digital/input_pullup_serial.py --no-upload
echo "Compiling state_change_detection"
$INTERPRETER_PATH $REPO_DIR/examples/digital/state_change_detection.py --no-upload

echo "---------- Compiling eeprom examples ----------"
echo "Compiling eeprom_clear"
$INTERPRETER_PATH $REPO_DIR/examples/eeprom/eeprom_clear.py --no-upload
echo "Compiling eeprom_crc"
$INTERPRETER_PATH $REPO_DIR/examples/eeprom/eeprom_crc.py --no-upload

echo "---------- Compiling ethernet examples ----------"
echo "Compiling advanced_chat_server"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/advanced_chat_server.py --no-upload
echo "Compiling barometric_pressure_web_server"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/barometric_pressure_web_server.py --no-upload
echo "Compiling chat_server"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/chat_server.py --no-upload
echo "Compiling dhcp_address_printer"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/dhcp_address_printer.py --no-upload
echo "Compiling dhcp_chat_server"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/dhcp_chat_server.py --no-upload
echo "Compiling link_status"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/link_status.py --no-upload
echo "Compiling pager_server"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/pager_server.py --no-upload
echo "Compiling telnet_client"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/telnet_client.py --no-upload
echo "Compiling udp_ntp_client"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/udp_ntp_client.py --no-upload
echo "Compiling udp_send_receive_string"
$INTERPRETER_PATH $REPO_DIR/examples/ethernet/udp_send_receive_string.py --no-upload

#echo "---------- Compiling keyboard examples ----------"
#echo "Compiling serial"
#$INTERPRETER_PATH $REPO_DIR/examples/keyboard/serial.py --no-upload

echo "---------- Compiling liquid_crystal examples ----------"
echo "Compiling autoscroll"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/autoscroll.py --no-upload
echo "Compiling blink"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/blink.py --no-upload
echo "Compiling cursor"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/cursor.py --no-upload
echo "Compiling custom_character"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/custom_character.py --no-upload
echo "Compiling display"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/display.py --no-upload
echo "Compiling scroll"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/scroll.py --no-upload
echo "Compiling serial_display"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/serial_display.py --no-upload
echo "Compiling text_direction"
$INTERPRETER_PATH $REPO_DIR/examples/liquid_crystal/text_direction.py --no-upload

echo "---------- Compiling sd examples ----------"
echo "Compiling card_info"
$INTERPRETER_PATH $REPO_DIR/examples/sd/card_info.py --no-upload
echo "Compiling data_logger"
$INTERPRETER_PATH $REPO_DIR/examples/sd/data_logger.py --no-upload
echo "Compiling dump_file"
$INTERPRETER_PATH $REPO_DIR/examples/sd/dump_file.py --no-upload
echo "Compiling files"
$INTERPRETER_PATH $REPO_DIR/examples/sd/files.py --no-upload
echo "Compiling list_files"
$INTERPRETER_PATH $REPO_DIR/examples/sd/list_files.py --no-upload
echo "Compiling non_blocking_write"
$INTERPRETER_PATH $REPO_DIR/examples/sd/non_blocking_write.py --no-upload
echo "Compiling read_write"
$INTERPRETER_PATH $REPO_DIR/examples/sd/read_write.py --no-upload

echo "---------- Compiling servo examples ----------"
echo "Compiling knob"
$INTERPRETER_PATH $REPO_DIR/examples/servo/knob.py --no-upload
echo "Compiling sweep"
$INTERPRETER_PATH $REPO_DIR/examples/servo/sweep.py --no-upload

echo "---------- Compiling software serial examples ----------"
echo "Compiling software_serial_example"
$INTERPRETER_PATH $REPO_DIR/examples/software_serial/software_serial_example.py --no-upload
echo "Compiling two_port_receive"
$INTERPRETER_PATH $REPO_DIR/examples/software_serial/two_port_receive.py --no-upload

echo "---------- Compiling spi examples ----------"
echo "Compiling barometric_pressure_sensor"
$INTERPRETER_PATH $REPO_DIR/examples/spi/barometric_pressure_sensor.py --no-upload
echo "Compiling digital_pot_control"
$INTERPRETER_PATH $REPO_DIR/examples/spi/digital_pot_control.py --no-upload

echo "---------- Compiling stepper examples ----------"
echo "Compiling motor_knob"
$INTERPRETER_PATH $REPO_DIR/examples/stepper/motor_knob.py --no-upload
echo "Compiling stepper_one_revolution"
$INTERPRETER_PATH $REPO_DIR/examples/stepper/stepper_one_revolution.py --no-upload
echo "Compiling stepper_one_step_at_a_time"
$INTERPRETER_PATH $REPO_DIR/examples/stepper/stepper_one_step_at_a_time.py --no-upload
echo "Compiling stepper_speed_control"
$INTERPRETER_PATH $REPO_DIR/examples/stepper/stepper_speed_control.py --no-upload

echo "---------- Compiling wire examples ----------"
echo "Compiling digital_potentiometer"
$INTERPRETER_PATH $REPO_DIR/examples/wire/digital_potentiometer.py --no-upload
echo "Compiling i2c_scanner"
$INTERPRETER_PATH $REPO_DIR/examples/wire/i2c_scanner.py --no-upload
echo "Compiling master_reader"
$INTERPRETER_PATH $REPO_DIR/examples/wire/master_reader.py --no-upload
echo "Compiling master_writer"
$INTERPRETER_PATH $REPO_DIR/examples/wire/master_writer.py --no-upload
echo "Compiling slave_receiver"
$INTERPRETER_PATH $REPO_DIR/examples/wire/slave_receiver.py --no-upload
echo "Compiling slave_sender"
$INTERPRETER_PATH $REPO_DIR/examples/wire/slave_sender.py --no-upload
