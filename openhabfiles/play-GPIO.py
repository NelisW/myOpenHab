#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

#define some pin numbers
pinLedSw = 19
pinLedRd = 13

#set the software to use the Broadcom numbers
GPIO.setmode(GPIO.BCM)
#set up th
GPIO.setup(pinLedSw,GPIO.OUT)
GPIO.setup(pinLedRd,GPIO.IN)

def pinSet(pin, setLed):
		GPIO.output(pin, setLed)
		
def pinRead(pin):
		return GPIO.input(pin)
		
pinSet(pinLedSw,True)
print(pinRead(pinLedRd))
sleep(2)
pinSet(pinLedSw,False)
print(pinRead(pinLedRd))
sleep(2)

GPIO.cleanup()

