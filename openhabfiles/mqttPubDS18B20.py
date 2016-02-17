#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import glob
import time
import datetime
import collections

"""
Setting up  is described in 
https://github.com/NelisW/myOpenHab/blob/master/docs/021-1wire-RPi.md
https://github.com/NelisW/myOpenHab/blob/master/docs/050-DS18B20-temperature.md

the driver expects the 1-wire device on GPIO4
"""

# load the 1-wire interface driver, unless already loaded during boot
#ideally it must be done at boot, commented out here
#os.system('modprobe w1-gpio')
#adds temperature support
#os.system('modprobe w1-therm')


#set up the path to device and get list of all devices
base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')

#print(device_folders)

def read_temp_raw(device):
    f = open(device + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(device_folders, device_key):
    dicmeasure = {}
    for device in device_folders:
        devID = device[device.rfind('/')+1:]
        lines = read_temp_raw(device)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw(device)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_c = float(lines[1][equals_pos+2:]) / 1000.0 
            ctime = datetime.datetime.now().isoformat(' ')
            dicmeasure[devID]= [ctime, temp_c]
	if device_key in dicmeasure.keys():
		rtnTemp = dicmeasure[device_key]
	else:
		rtnTemp = -100.0
    return rtnTemp


lastTime = datetime.datetime.now()

while True:
    
    #for i,key in enumerate(dicmeasure):
        #print('{}: {} {:.1f} C'.format(key,dicmeasure[key][0], dicmeasure[key][1]))

    # RPi CPU temperature
    tempCPU = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    #print('CPU temperature {} '.format(tempCPU))
    
    #publish regular status meassages to openHAB via mqtt
    #os.system("mosquitto_pub -t 'home/garage/PVTemperatureMid' -m '{}'".format(dicmeasure['28-000004d0250c'][1]))
    #os.system("mosquitto_pub -t 'home/garage/PVTemperatureFar' -m '{}'".format(dicmeasure['28-021582d1d0ff'][1]))
    #os.system("mosquitto_pub -t 'home/garage/PVTemperatureNer' -m '{}'".format(dicmeasure['28-021582f6a5ff'][1]))
    #os.system("mosquitto_pub -t 'home/study/RoomTemperature' -m '{}'".format(dicmeasure['28-021582d26eff'][1]))

    os.system("mosquitto_pub -t 'home/garage/PVTemperatureMid' -m '{}'".format(read_temp(device_folders, '28-000004d0250c')))
    os.system("mosquitto_pub -t 'home/garage/PVTemperatureFar' -m '{}'".format(read_temp(device_folders, '28-021582d1d0ff')))
    os.system("mosquitto_pub -t 'home/garage/PVTemperatureNer' -m '{}'".format(read_temp(device_folders, '28-021582f6a5ff')))
    os.system("mosquitto_pub -t 'home/study/RoomTemperature' -m '{}'".format(read_temp(device_folders, '28-021582d26eff')))
    os.system("mosquitto_pub -t 'home/study/CPUTemperature' -m '{}'".format(tempCPU))
    
    #publish mqtt warnings when the CPU temperature rises above some threshold
    #the message can be used to trigger a pushover and/or email notification
    thresholdTempCPU = 50.
    if tempCPU > thresholdTempCPU:
		now = datetime.datetime.now()
		#this warning must only be issued between 0600 and 2200
		if now.hour > 6 and now.hour < 22:
			#get day of year to ensure only one warning per day
			lastDay = (lastTime.year - 2000) * 356 + lastTime.timetuple().tm_yday
			nowDay = (now.year - 2000) * 356 + now.timetuple().tm_yday
			#this warning must only be issued once per day 
			if nowDay > lastDay:
				os.system("mosquitto_pub -t 'pushover/warnCPU' -m 'CPU temperature is {} C'".format(tempCPU))			
				lastTime = now	
    
    time.sleep(10)  





