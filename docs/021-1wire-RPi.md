#1-Wire on RPi

##1-Wire overview

<http://www.maximintegrated.com/en/app-notes/index.mvp/id/1796>

The basis of 1-Wire technology is a serial protocol using a single data line plus ground reference for communication. A 1-Wire master initiates and controls the communication with one or more 1-Wire slave devices on the 1-Wire bus). Each 1-Wire slave device has a unique, unalterable, factory-programmed, 64-bit ID (identification number), which serves as device address on the 1-Wire bus. 1-Wire devices can be connected in parallel on s single bus, they co-exist quite well without interfering with each other.

##Installing 1-Wire drivers

<http://pi-io.com/how-to/173-2/>  
<http://devicehive.com/samples/python-and-raspberry-pi-temperature-sensor>

<https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20>

It gets a bit confusing when you google, there are some minor differences between the different web pages on what to install and the commands for this purpose.
One source says that the 1-Wire library is installed in the Raspbian OS,  but not loaded/executed.  We will follow the [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20) instruction here (it is dated relatively recently).

If it is not already there, add the line `dtoverlay=w1-gpio,gpiopin=4` to the end of `/boot/config.txt`.  The `gpiopin=4` registers the new sensor connected to GPIO4.   

    sudo nano /boot/config.txt

The reboot the RPi with `sudo reboot`

In all that follows the `w1` should be the letter w, followed by the number 1 (not the letter el).  This is because it is the 1-Wire interface, not the el-Wire interface.

`modprobe` adds or removes a loadable kernel module (LKM) to Linux/Raspbian. 
PThe 1-Wire driver names are somewhat confusing: should it be `w1_therm` or `w1-therm`?  Go look on your Rpi in these two locations and see which form is present:  
</lib/modules/3.18.11-v7+/kernel/drivers/w1/masters>: `w1-gpio.ko`  
</lib/modules/3.18.11-v7+/kernel/drivers/w1/slaves>: `w1_therm.ko`  
then use these forms (drop the `.ko`).

Run following commands:
    sudo modprobe w1-gpio
    sudo modprobe w1_therm
  
`modprobe w1-gpio` adds gpio support (to use the io pins).  
`w1-therm` adds the temperature support.   

Add lines `w1-gpio` and `w1_therm` into `/etc/modules` so they get loaded 
automatically the next time you restart the Raspberry Pi.

    sudo nano /etc/modules

The DS18B20 temperature sensor driver `w1_therm` is installed in the kernel directories shown above. There is also a link to the `w1_therm` driver at 
`/sys/bus/w1/devices`. If there are other 1-Wire devices, you can also see them here.  The directories starting with  `28*` are one or more of the temperature sensors. The data is written to the file `w1_slave` in these directories.   Use `chmod 666`  the change permissions for reading the sensordata.  

    chmod 666 /sys/bus/w1/devices/28-*/w1_slave

Now you're able to get the temperature values from the devices with the command:

    cat /sys/bus/w1/devices/28__ADDRESS__/w1_slave

where `28__ADDRESS__` is the directory for each device.  The address is different for each device, because the device unique ID number is used to create the directory.

Reading and manipulating the data is described in   
<https://github.com/NelisW/myOpenHab/blob/master/docs/050-DS18B20-temperature.md>

