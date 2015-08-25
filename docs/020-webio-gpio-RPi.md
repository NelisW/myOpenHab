#IO on the RPi

##RPi pins-python-2818/
[gadgetoid](http://pi.gadgetoid.com/pinout/pin8_gpio14) has a very nice web site explaining the IO pins on the RPi.

  
    
    
--------------------------------------------------
#Installing the GPIO  library
    
[Configuring GPIO](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-gpio)

[How to communicate with gpio, onewire, spi, i2c](http://pi-io.com/how-to/173-2/)

<http://forums.connectedly.com/guides-how-articles-f10/how-set-up-raspberry-pi-2626/>

Go to the setup page for your router. Everyone is a little different, but somewhere you can set the DHCP server to always assign the same IP address to a device based on its MAC address. 


<http://forums.connectedly.com/raspberry-pi-f179/introduction-controlling-gpio-pins-python-2818/>

sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio

<http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/>

<https://code.google.com/p/webiopi/>
<https://code.google.com/p/webiopi/wiki/INSTALL>

The RPi.GPIO library uses access to /dev/mem which requires root. 

------------------------------------------------------------------------
##C / C++

http://visualgdb.com/tutorials/raspberry/  Developing a Raspberry PI app with Visual Studio
http://visualgdb.com/tutorials/raspberry/LED/

http://abyz.co.uk/rpi/pigpio/index.html


-----------------------------------------------------------------


##install wiringPi and its Python binding
__Don't execute the installation in this section, not required__

<http://wiringpi.com/> WiringPi is a GPIO access library written in C for the BCM2835 used in the Raspberry Pi. It’s released under the GNU LGPLv3 license and is usable from C and C++ and many other languages with suitable wrappers (See below) It’s designed to be familiar to people who have used the Arduino “wiring” system1

<http://wiringpi.com/download-and-install/>

	git clone git://git.drogon.net/wiringPi
	cd wiringPi
	git pull origin
	cd wiringPi
	sudo ./build

run the gpio command to check the installation:

	cd gpio
	gpio -v
	gpio readall

Now install the Python bindings to wiringPi

<https://github.com/Gadgetoid/WiringPi2-Python>

    git clone https://github.com/Gadgetoid/WiringPi2-Python.git
    cd WiringPi2-Python
    sudo python setup.py install    
    
  -------------------------------------------------------------------
  
https://learn.adafruit.com/debugging-with-the-raspberry-pi-webide/debug-a-blinking-led  
http://www.petervis.com/Raspberry_PI/Raspberry_Pi_Blink_LED/Raspberry_Pi_Blink_LED.html  
https://startingelectronics.org/software/raspberry-PI/raspberry-PI-Flash-LED-Python/  
http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html   
  