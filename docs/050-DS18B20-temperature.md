#DS18B20 temperature sensor on 1-wire
<http://datasheets.maximintegrated.com/en/ds/DS18S20.pdf>  
<http://devicehive.com/samples/python-and-raspberry-pi-temperature-sensor>
<https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing>

Install the 1-Wire gpio and therm drivers as described here  
<https://github.com/NelisW/myOpenHab/blob/master/docs/021-1wire-RPi.md>

Once the drivers are installed and the devices are wired as shown []here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing) the temperature values are written to the file `/sys/bus/w1/devices/28__ADDRESS__/w1_slave`. To see the results open a terminal and type  

    cat /sys/bus/w1/devices/28__ADDRESS__/w1_slave

For the device currently wired in to my RPi I typed

    cat /sys/bus/w1/devices/28-000004d0250c/w1_slave
    
to get

    74 01 4b 46 7f ff 0c 10 55 : crc=55 YES
    74 01 4b 46 7f ff 0c 10 55 t=23250

The first line confirms that the cyclic redundancy check passed (data is trustworthy).  If the `YES` does not appear, it means that the data is not right or the device is broken.  The second line shows the temperature in degrees millicelsius after the `t=`. The value `23250` means a temperature of 23.25 deg C.

<http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf>

By default the device measures with 12 bits resolution, or 0.0625 deg C per least significant bit.
The hex values shown are the values returned from the device itself.  The first byte `74` is the least significant byte and the second byte `01` is the most significant byte. Convert the number to decimal and multiply with 0.0625 to get the temperature.  `0174` is 372, 372*0.062.5=23.25.

##Python example

This program reads all DS18B20 devices on the bus and prints the temperatures to the screen, as well as publishes the temperatures on MQTT.

#!/usr/bin/env python

"""
Setting up  is described in 
https://github.com/NelisW/myOpenHab/blob/master/docs/021-1wire-RPi.md
https://github.com/NelisW/myOpenHab/blob/master/docs/050-DS18B20-temperature.md
"""

    import os
    import glob
    import time
    import datetime
    import collections

    # load the 1-wire interface driver, unless already loaded during boot
    # the driver expects the 1-wire device on GPIO4
    #os.system('modprobe w1-gpio')
    #adds temperature support
    #os.system('modprobe w1-therm')

    #set up the path to device and get list of all devices
    base_dir = '/sys/bus/w1/devices/'
    device_folders = glob.glob(base_dir + '28*')

    print(device_folders)

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
        
        for i,key in enumerate(dicmeasure):
            print('{}: {} {:.1f} C'.format(key,dicmeasure[key][0], dicmeasure[key][1]))

        # RPi CPU temperature
        tempCPU = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
        #print('CPU temperature {} '.format(tempCPU))
        
        #publish to mqtt
        os.system("mosquitto_pub -t 'home/study/RoomTemperature' -m '{}'".format(dicmeasure['28-000004d0250c'][1]))
        os.system("mosquitto_pub -t 'home/study/CPUTemperature' -m '{}'".format(tempCPU))
        
        time.sleep(10)  

In order to run this program as a service you have to manage it with supervisord (see `003-diverse-software-RPi.md`).
Create a file with the following contents (assuming the file is located at  `/home/pi/myOpenHab/openhabfiles/mqttPubDS18B20.py`):

    [program:mqttPubDS18B20]
    directory = /home/pi/myOpenHab/openhabfiles
    command = /home/pi/myOpenHab/openhabfiles/mqttPubDS18B20.py
    autostart=true
    autorestart=true
    ;startretries=1000
    stderr_logfile=/home/pi/log/mqttPubDS18B20.err.log
    stdout_logfile=/home/pi/log/mqttPubDS18B20.out.log
    user = pi

 and save the file to `/etc/supervisor/conf.d/mqttPubDS18B20.conf`  and manage the file execution henceforth with supervisord, as explained in `003-diverse-software-RPi.md`.
 
  
    

 
        


##lua ESP8266 example

<https://bigdanzblog.wordpress.com/2015/04/25/esp8266-and-ds18b20-transmitting-temperature-data/>
<http://www.esp8266.com/viewtopic.php?f=19&t=752>


##Links

http://thepiandi.blogspot.com/2013_06_01_archive.html
http://www.sbprojects.com/projects/raspberrypi/temperature.php
http://pythonhosted.org/gadgets/_modules/gadgets/sensors/thermometer.html
https://iada.nl/en/blog/article/temperature-monitoring-raspberry-pi
http://iot-projects.com/index.php?id=connect-ds18b20-sensors-to-raspberry-pi


