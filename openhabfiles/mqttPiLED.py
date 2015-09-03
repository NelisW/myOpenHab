#!/usr/bin/env python

"""
https://pypi.python.org/pypi/paho-mqtt

"""

import mosquitto
import time

#define what happens after connection
def on_connect(rc):
   print "Connected"
   pass

def on_message(msg):
	pass
	
mqttc = mosquitto.Mosquitto("doorbell_cam")

#define the callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect

#connect
mqttc.connect("10.0.0.16", 1883, 60, True)

#subscribe to topic 
mqttc.subscribe("house/doorbell", 2)

#keep connected to broker
while mqttc.loop() == 0:
    pass

