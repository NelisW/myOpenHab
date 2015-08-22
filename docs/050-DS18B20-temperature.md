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




##lua ESP8266 example

<https://bigdanzblog.wordpress.com/2015/04/25/esp8266-and-ds18b20-transmitting-temperature-data/>
<http://www.esp8266.com/viewtopic.php?f=19&t=752>


##Links

http://thepiandi.blogspot.com/2013_06_01_archive.html
http://www.sbprojects.com/projects/raspberrypi/temperature.php
http://pythonhosted.org/gadgets/_modules/gadgets/sensors/thermometer.html
https://iada.nl/en/blog/article/temperature-monitoring-raspberry-pi
http://iot-projects.com/index.php?id=connect-ds18b20-sensors-to-raspberry-pi


