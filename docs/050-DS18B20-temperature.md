#DS18B20 temperature sensor on 1-wire

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

The first line confirms that the cyclic redundancy check passed (data is trustworthy).  If the `YES` does not appear, it means that the data is not right or the device is broken.  The second line shows the temperature in degrees celsius after the `t=`. The value `23250` means a temperature of 23.25 deg C.



