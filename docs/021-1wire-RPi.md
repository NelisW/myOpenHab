#1-Wire on RPi

##1-Wire overview

<http://www.maximintegrated.com/en/app-notes/index.mvp/id/1796>

The basis of 1-Wire technology is a serial protocol using a single data line plus ground reference for communication. A 1-Wire master initiates and controls the communication with one or more 1-Wire slave devices on the 1-Wire bus). Each 1-Wire slave device has a unique, unalterable, factory-programmed, 64-bit ID (identification number), which serves as device address on the 1-Wire bus. 1-Wire devices can be connected in parallel on s single bus, they co-exist quite well without interfering with each other.

##Installing 1-Wire drivers

<http://pi-io.com/how-to/173-2/>  
<http://devicehive.com/samples/python-and-raspberry-pi-temperature-sensor>

<https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20>

It gets a bit confusing when you google, there are some minor differences between the different web pages.
One says that the 1-Wire library is installed in the Raspbian OS,  but not loaded/executed.  We will follow the [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20) instruction here (it is dated relatively recently).

If it is not already there, add the line `dtoverlay=w1-gpio,gpiopin=4` to the end of `/boot/config.txt`

    sudo nano /boot/config.txt

The reboot the RPi with `sudo reboot`



Run following commands:
    sudo modprobe w1-gpio
    sudo modprobe w1_therm
  
`modprobe w1-gpio` registers the new sensor connected to GPIO4.   
`w1-therm` adds the temperature support.   

Add lines `w1-gpio` and `w1_therm` into /etc/modules so they get loaded 
automatically the next time you restart the Raspberry Pi.

"chmod 666" is adding all the permissions for reading the sensordata.
    chmod 666 /sys/bus/w1/devices/28-*/w1_slave

Now you're able to get the associated temperature value from the device with the command:
    cat /sys/bus/w1/devices/**__ADDRESS__**/w1_slave

You can see all recognized onewire addresses under:
    cd /sys/bus/w1/devices/

If you type the upper command you will get an output.
In the first line at the end, there is a "YES" for a successful CRC - Check.
Is there anything else how "NO" or "FALSE" or "ERROR",
means, that the sensor is broken.
In the second line you can now find the current temperature,
it is after the "t=".
A value like "2481" is the temperature ? "24,81".




http://pi-io.com/how-to/173-2/
#http://devicehive.com/samples/python-and-raspberry-pi-temperature-sensor

