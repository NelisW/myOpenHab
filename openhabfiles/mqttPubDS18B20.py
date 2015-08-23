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
"""

# load the 1-wire interface driver, unless already loaded during boot
# the driver expects the 1-wire device on GPIO4
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

def read_temp(device_folders):
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
    return dicmeasure
  

while True:
    dicmeasure = read_temp(device_folders)
    
    #for i,key in enumerate(dicmeasure):
        #print('{}: {} {:.1f} C'.format(key,dicmeasure[key][0], dicmeasure[key][1]))

    # RPi CPU temperature
    tempCPU = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    #print('CPU temperature {} '.format(tempCPU))
    
    #publish to mqtt
    os.system("mosquitto_pub -t 'home/study/RoomTemperature' -m '{}'".format(dicmeasure['28-000004d0250c'][1]))
    os.system("mosquitto_pub -t 'home/study/CPUTemperature' -m '{}'".format(tempCPU))
    
    time.sleep(10)  





