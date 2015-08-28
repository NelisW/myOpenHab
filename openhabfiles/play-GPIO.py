#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

#define some pin numbers
pinLedSw = 19
pinLedRd = 13

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
	
#experiment with pins		
pinSet(pinLedSw,True)
print(pinRead(pinLedRd))
sleep(2)
pinSet(pinLedSw,False)
print(pinRead(pinLedRd))
sleep(2)

#we have to clean up to reset pin definitions
GPIO.cleanup()

