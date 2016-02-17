#!/usr/bin/env python

"""
https://pypi.python.org/pypi/paho-mqtt
"""

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep


#define some pin numbers
pinLedSw = 19
pinLedRd = 13

#we have to clean up to reset pin definitions
#GPIO.cleanup()

#set the software to use the Broadcom numbers
GPIO.setmode(GPIO.BCM)
#set up the  pins definitions
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
	sleep(0.1)
	state = pinRead(pinLedRd)
	if state:
		sstate = 1
	else:
		sstate = 0
	client.publish("home/study/PiLED/state", sstate)

#def on_disconnect(client, userdata, rc):
#	if rc != 0:
#		pass
#	client.connect("10.0.0.16", 1883, 60)
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_disconnect = on_disconnect

client.connect(host="10.0.0.16", port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
