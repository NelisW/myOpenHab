# ESP PIR Alarm

This is a very early version of the project, not much functionality is actually working.

## Objective
This project creates an alarm system with the following objectives:

1. Standalone ESP8266.
1. MQTT comms with a Raspberry Pi to escalate the alarm.
1. Multiple PIR sensors, with intelligent logic before triggering the alarm.
1. Switching on a security light if one of the PIRs triggered.
1. The light must switch on if an approriate MQTT command is sent to the ESP.
1. The light must remain on for a programmable time, and then switch off again.
1. The ESP must be programmable/flashable over the air (OTA) once deployed.
1. The ESP must send regular MQTT pings to confirm it is on the air.

The idea is to use the low-cost PIR sensors available on EBay and AliExpress for dollar or two.

## Code
This text accompanies the ESP code [here](
https://github.com/NelisW/IoTPlay/blob/master/PlatformIO-IDE/interrupt/src/main.ino)

## Use case
The alarm must be deployed to cover an area outside the house, such that sustained movement in Zone 1 must trigger the alarm, movement in Zone 2 must not trigger the alarm, but movement in either of the zones must switch on the light.  

Zone 1 must have a low false alarm rate: one or more designated PIR sensors must trigger within Tsim seconds of each other, at least N times in a Twin second period.  The Twin period is a running window that must keep track of alarms in the most recent Twin seconds. Tsim, Twin and N must be software programmable.

A trigger on any PIR, or a MQTT message, must switch on the light, which must stay on for Tl seconds.

## Over the Air Update (OTA)

OTA was implemented right from the start to free up a USB on my PC.
