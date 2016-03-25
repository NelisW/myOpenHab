# IO on the RPi

## RPi pins-python-2818/
[gadgetoid](http://pi.gadgetoid.com/pinout/pin8_gpio14) has a very nice web site explaining the IO pins on the RPi.

## The GPIO  library

The GPIO library provides Python access to set and read the input/output pin on the Raspberry.

## Installing the GPIO  library

[Installing GPIO](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-gpio)

sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio

The RPi.GPIO library uses access to /dev/mem which requires root. So, to run your Python scripts, do this as sudo:

    sudo python myscrpt.py

## Using GPIO

[GPIO pins tutorial](http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)

<http://forums.connectedly.com/raspberry-pi-f179/introduction-controlling-gpio-pins-python-2818/>




<http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/>

<https://code.google.com/p/webiopi/>
<https://code.google.com/p/webiopi/wiki/INSTALL>


------------------------------------------------------------------------
## C / C++

http://visualgdb.com/tutorials/raspberry/  Developing a Raspberry PI app with Visual Studio
http://visualgdb.com/tutorials/raspberry/LED/

http://abyz.co.uk/rpi/pigpio/index.html


-----------------------------------------------------------------


## install wiringPi and its Python binding

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


-------------------------------------

[How to communicate with gpio, onewire, spi, i2c](http://pi-io.com/how-to/173-2/)

## raspberry-gpio-python

https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

RPi.GPIO module basics
Importing the module

To import the RPi.GPIO module:

    import RPi.GPIO as GPIO

By doing it this way, you can refer to it as just GPIO through the rest of your script.

To import the module and check to see if it is successful:

    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

### Pin numbering

There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. The first is using the BOARD numbering system. This refers to the pin numbers on the P1 header of the Raspberry Pi board. The advantage of using this numbering system is that your hardware will always work, regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.

The second numbering system is the BCM numbers. This is a lower level way of working - it refers to the channel numbers on the Broadcom SOC. You have to always work with a diagram of which channel number goes to which pin on the RPi board. Your script could break between revisions of Raspberry Pi boards.

To specify which you are using using (mandatory):

    GPIO.setmode(GPIO.BOARD)
      # or
    GPIO.setmode(GPIO.BCM)

To detect which pin numbering system has been set (for example, by another Python module):

    mode = GPIO.getmode()

The mode will be GPIO.BOARD, GPIO.BCM or None

### Warnings

It is possible that you have more than one script/circuit on the GPIO of your Raspberry Pi. As a result of this, if RPi.GPIO detects that a pin has been configured to something other than the default (input), you get a warning when you try to configure a script. To disable these warnings:

    GPIO.setwarnings(False)

### Setup up a channel

You need to set up every channel you are using as an input or an output. To configure a channel as an input:

    GPIO.setup(channel, GPIO.IN)

(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)).

More advanced information about setting up input channels can be found here.

To set up a channel as an output:

    GPIO.setup(channel, GPIO.OUT)

(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)).

You can also specify an initial value for your output channel:

    GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

### Setup more than one channel

You can set up more than one channel per call (release 0.5.8 onwards). For example:

    chan_list = [11,12]    # add as many channels as you want!
                           # you can tuples instead i.e.:
                           #   chan_list = (11,12)
    GPIO.setup(chan_list, GPIO.OUT)

### Input

To read the value of a GPIO pin:

    GPIO.input(channel)

(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)). This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

### Output

To set the output state of a GPIO pin:

    GPIO.output(channel, state)

(where channel is the channel number based on the numbering system you have specified (BOARD or BCM)).

State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

### Output to several channels

You can output to many channels in the same call (release 0.5.8 onwards). For example:

    chan_list = [11,12]                             # also works with tuples
    GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
    GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW

### Cleanup

At the end any program, it is good practice to clean up any resources you might have used. This is no different with RPi.GPIO. By returning all channels you have used back to inputs with no pull up/down, you can avoid accidental damage to your RPi by shorting out the pins. Note that this will only clean up GPIO channels that your script has used. Note that GPIO.cleanup() also clears the pin numbering system in use.

To clean up at the end of your script:

    GPIO.cleanup()

It is possible that don't want to clean up every channel leaving some set up when your program exits. You can clean up individual channels, a list or a tuple of channels:

    GPIO.cleanup(channel)
    GPIO.cleanup( (channel1, channel2) )
    GPIO.cleanup( [channel1, channel2] )

### RPi Board Information and RPi.GPIO version

To discover information about your RPi:

    GPIO.RPI_INFO

To discover the Raspberry Pi board revision:

    GPIO.RPI_INFO['P1_REVISION']
    GPIO.RPI_REVISION    (deprecated)

To discover the version of RPi.GPIO:

    GPIO.VERSION
