# Blinking a LED via openHAB

## Purpose

The purpose with this experiment is to switch a LED on and off via openHAB. We are using mqtt to communicate between openHAB, the RPi and the LED controller. This means that the LED controller can be any device on the network that is reachable via mqtt: just use the appropriate topic for the specific controller.  

In this experiment the LED control happens to be on the RPi, but it can easily be moved to an ESP8266 or any other station on the network. This change is as simple as an edit to change the mqtt topic.

## Prerequisites

You must have the following functionality on the RPi:

1. A running mqtt broker (can be anywhere, but the RPi is fine).
1. mqtt clients on the openHAB controller (RPi) and the LED controller (also RPi in this instance).
1. LED attached to the LED controller's GPIO pins.
1. Registration on the myopenHAB  server in order to use a smart phone app for control.
1. The RPi must have the python libraries `RPi.GPIO` and `paho.mqtt`

## Hardware

Wire the LED and current limiting resistor to pin 19.  This pin will be used to switch the LED on and off.

Wire pin 13 to read the voltage on pin 19. The idea is that the LED state can be read at any time to determine if it is switched on.

## Software

The code here is based on the examples given in the []Python mqtt library](https://pypi.python.org/pypi/paho-mqtt).  The code is well documented and should be easy to follow.

In essence we set up a mqtt client object and define two callback functions: `on_connect` and `on_message`. 

In the `on_connect` function body do everything you need to do during the initialisation and setup phase.  In particular, tell the client which topic must be subscribed to.  The topic can be any string you want, it must just be consistent with the publisher topic (in this case, the openHAB binding).

In the `on_message` function do everything that needs to be done during the operational phase. The primary function here is to decode the mqtt message and respond in the appropriate manner.  In this case switch the LED on or off, depending on the message.  We also read the status of pin 13 and publish this status as a message on another mqtt topic.  This way we can ascertain that the LED is indeed switched on or off.

The Python code running on the RPI is as follows:

    # !/usr/bin/env python

    import paho.mqtt.client as mqtt
    import RPi.GPIO as GPIO
    from time import sleep


    # define some pin numbers
    pinLedSw = 19
    pinLedRd = 13

    # we have to clean up to reset pin definitions
    GPIO.cleanup()

    # set the software to use the Broadcom numbers
    GPIO.setmode(GPIO.BCM)
    # set up the  pins definitions
    GPIO.setup(pinLedSw,GPIO.OUT)
    GPIO.setup(pinLedRd,GPIO.IN)

    def pinSet(pin, setLed):
        """set pin number to given state"""
        GPIO.output(pin, setLed)
            
    def pinRead(pin):
        """Read pin number state"""
        return GPIO.input(pin)


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("home/study/PiLED")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        if 'ON' in msg.payload:
            pinSet(pinLedSw,True)
        if 'OFF' in msg.payload:
            pinSet(pinLedSw,False)
        state = pinRead(pinLedRd)
        if state:
            sstate = "on"
        else:
            sstate = "off"
        print(sstate)
        client.publish("home/study/PiLED/state", sstate)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("10.0.0.16", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

Start the script as a     
    
    
## openHAB
On the other side of the mqtt channel we must have a publisher providing the LED switch commands and a subscriber listening to follow the LED status.  This functionality is running in openHAB.

The openHAB sitemap file for this experiment is as follows (just ignore the temperature content):

    sitemap default label="Main Menu"
    {
            Frame label="Study" {
                    Text item=StudyTemperature
                    Text item=CPUTemperature
            Switch item=PiLED label="Pi LED"] 
            }
    }	

The openHAB items file for this experiment is as follows (just ignore the temperature content):

    Group All

    Group gGroundFloor (All)

    Group GF_Study "Study" <video> (gGroundFloor)

    Number StudyTemperature "Room Temperature [%.1f C]" <temperature> (GF_Study) {mqtt="<[mymosquitto:home/study/RoomTemperature:state:default]"}

    Number CPUTemperature "CPU Temperature [%.1f C]" <temperature> (GF_Study) {mqtt="<[mymosquitto:home/study/CPUTemperature:state:default]"}

    Switch PiLED "Pi LED" <switch> (GF_Study) {mqtt=">[mymosquitto:home/study/PiLED:command:on:ON],>[mymosquitto:home/study/PiLED:command:off:OFF],<[mymosquitto:home/study/PiLED/state:state:default]"}

In these two files the LED device is called PiLED, which is located in the study.  The item definition of the LED is as follows (the definition is spread over many lines for readability, normally all this will be on one line):

    Switch PiLED "Pi LED" <switch> (GF_Study) 
    {mqtt="
    >[mymosquitto:home/study/PiLED:command:on:ON],
    >[mymosquitto:home/study/PiLED:command:off:OFF],
    <[mymosquitto:home/study/PiLED/state:state:default]
    "}

 
 
 
 

 