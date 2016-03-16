# ESP PIR Alarm

This is a very early version of the project, not much functionality is actually working.

## Objective
This project creates an alarm system with the following objectives:

1. Standalone ESP8266, connected by wifi to the rest of the network. Completed.
1. The ESP must be programmable/flashable over the air (OTA) once deployed. Completed.
1. MQTT comms with a Raspberry Pi to escalate the alarm to an OpenHab instance. Completed.
1. The ESP must send regular MQTT pings to confirm it is on the air. Completed.
1. Multiple PIR sensors, with intelligent logic before triggering the alarm. Completed.
1. Switching on a security light if any one of the PIRs is triggered.
1. The light must remain on for a programmable time, and then switch off again.
1. The light must switch on if an approriate MQTT command is sent to the ESP.
1. Set up the OpenHab environment to react to messages from this alarm

The idea is to use the low-cost PIR sensors available on EBay and AliExpress for dollar or two.

Presently a LED is switched on/off but the idea is to later switch a mains-powered LED.

## Code
This text accompanies the ESP code [here](
https://github.com/NelisW/IoTPlay/blob/master/PlatformIO-IDE/interrupt/src/main.ino)

The code developed here uses the Arduino-IDE ESP8266 core libraries,  in the [platformio-ide](https://github.com/NelisW/myOpenHab/blob/master/docs/413b-ESP8266-PlatformIO-Arduino-Framework.md).  Using the Arduino core libraries simplifies the coding considerably compared to writing code in the Expressif SDK.

## Use case
The alarm must be deployed to cover an area outside the house, such that sustained movement in Zone 1 must trigger the alarm, movement in Zone 2 must not trigger the alarm, but movement in either of the zones must switch on the light.  

Zone 1 must have a low false alarm rate: one or more designated PIR sensors must trigger within Tsim seconds of each other, at least N times in a Twin second period.  The Twin period is a running window that must keep track of alarms in the most recent Twin seconds. Tsim, Twin and N must be software programmable.

A trigger on any PIR, or a MQTT message, must switch on the light, which must stay on for Tl seconds.

The light must also be switched on and off via OpenHab.

## Hardware

The software is developed on the nodeMCU ESP8266 dev board.  This board is freely available
on EBay and AliExpress, at a price of around USD 5-7.  The board features a USB port, power
supply regulator and download functionality.  Just plug it into the PC USB port and it works.

The PIR sensors are operated from the nodeMCU 3.3V supply.  Connect the PIR ground to nodeMCU
ground. Connect the PIR positive supply to the 3.3 V supply to the H retrigger pin.

![pir_motion_sensor_arduino.jpg](images/pir_motion_sensor_arduino.jpg)

The three PIR sensors are connected to the following pins:

|PIR ID | GPIO pin | nodeMCU pin|
|---|-----|----|
| 0 | 12  | D6 |
| 1 | 13  | D7 |
| 2 | 14  | D5 |

## MQTT

The purpose with this ESP8266 device and PIRs is to raise an alarm via MQTT.  The
alarm is serviced elsewhere by another controller that subscribes to the alarm MQTT messages.  

The ESP8266 uses the PubSubClient library, originally developed for the Arduino,
then ported to the ESP8266.  Install the PubSubClient from http://platformio.org/#!/lib.
Download the tar file and untar into this project's lib folder (follow the platformio conventions).

The MQTT broker/server runs on a Raspberry Pi, which also handles the alarm events
in a larger OpenHab system.

The messages are transmitted on the `alarmW/` topic and messages can be displayed
any PC on the network by the Mosquitto client subscription command:

    mosquitto_sub -v -d -t "alarmW/+

## Wireless

### Fixed IP address
I have this thing about fixed IP addresses. In this project there may be more than
one ESP8266 device on the network and in order to do over the air (OTA) updates there
two choices: use a fixed IP address or use mDNS to resolve IP addresses.  The
fixed-IP-address seems simpler because all the configuration information is in one
file (the main.ino) file.

The code describes how to set a fixed IP address.

### Over the Air Update (OTA)

OTA is faster than using the serial download and supports firmware deployment to
ESP boards irrespective of where they are, provided that network access is available
(which is a given, because the ESP8266 must be on the wifi network to do its thing).

The code describes how to program the OTA functionality.

## Interrupts and times

ESP Pin interrupts are supported through attachInterrupt(), detachInterrupt()
functions. Interrupts may be attached to any GPIO pin except GPIO16,
but since GPIO6-GPIO11 are typically used to interface with the flash memory ICs
on most esp8266 modules, applying interrupts to these pins are likely to cause problems.
Standard Arduino interrupt types are supported: CHANGE, RISING, FALLING.

In this code the three PIRs each has its own interrupt service routine, because each pin is interrupted separately from the other.

The alive-ping signal is provided by a timer that triggers another interrupt service routine every few seconds.

Very little work is done in the interrupt service routines. These routines simply set flags for processing later in the `loop()` function phase of execution.  When action is taken in the `loop()` function, the flags are reset. This approach ensures stable interrupt operation.
