# Multiple DS18B20

## Overview
### Use case

I have a need to measure, display and store temperatures on my solar panels.  Three DS18B20 sensors are attached to the back of three of solar panels. 


### Objective

This project measures and displyas DS18B20 temperatures with the following objectives:

1. Standalone ESP8266, connected by fixed IP address on wifi to the rest of the network.
1. The ESP must be programmable/flashable over the air (OTA) once deployed.
1. The ESP must send regular MQTT pings to confirm it is alive.
1. Multiple DS18B20 sensors, with proper identification.
1. To timestamp the environmental data I added a local wall clock time library,  synchronised with NTP servers on the internet.  The time is synchronised at regular intervals.
o the outside world.
1. Set up an openHAB environment to display the temperatures.

## Software
### Source code and development environment
This text accompanies the code [available here on github](
https://github.com/NelisW/IoTPlay/tree/master/PlatformIO-IDE/esp8266-DS18B20)

The code developed here uses the Arduino ESP8266 core framework,  in the [platformio-ide](https://github.com/NelisW/myOpenHab/blob/master/docs/413b-ESP8266-PlatformIO-Arduino-Framework.md), with [platformio](http://platformio.org/) used from within the [atom](https://atom.io/) editor.  Using the Arduino core libraries simplifies the coding considerably compared to writing code in the Expressif SDK. PlatformIO is a much easier environment to use than The Arduino IDE.  T

### Libraries
The project uses the following libraries:


1. [PubSubClient](http://platformio.org/lib/show/89/PubSubClient) MQTT client to publish and subscribe to topics. Install in platformio terminal with `platformio lib install 89`.

2. [DallasTemperature](http://platformio.org/lib/show/54/DallasTemperature) to read the DS18B20 temperature sensor.  Install in platformio terminal with `platformio lib install 54`.

3. [OneWire](http://platformio.org/lib/show/1/OneWire) to provide the onewire library required by the DS18B20 sensor.  Install in platformio terminal with `platformio lib install 1`.

4. [WifiManager](http://platformio.org/lib/show/567/WifiManager) to provide the WifiManager library to default to Access Point mode if Station Mode fails.  Install in platformio terminal with `platformio lib install 567`.

4. [Json](http://platformio.org/lib/show/64/Json) to provide the Json library to read and write files to the filesystem.  Install in platformio terminal with `platformio lib install 64`.



Install the required libraries using the platformio command line method. The easiest method is to work in an environment with no proxies (and set your PC to no proxy) and then type the following at the command line:

    platformio lib install XX

where XX is the library number in the platformio library of libraries. The libraries will be installed in the general platformio library folder (`%USER%\.platformio\lib`), not in your project folder.  You may find it illuminating to work through the libraries downloaded here to see what happens behind the scenes. The library authors put in a huge effort to make life easier for us on the Arduino framework level.


For more information on how to load the libraries see the platformio website or [here](https://github.com/NelisW/myOpenHab/blob/master/docs/413b-ESP8266-PlatformIO-Arduino-Framework.md).

### Controller concept

Most events don't directly control any functionality, the events rather trigger semaphores or flags in the interrupt or timer callback routines.   The interrupt service routines are very small and fast, only setting the flags, hence it returns quickly after servicing the interrupt. The control changes take place in the `loop()` function, as prescribed by the flag settings. When action is taken in the `loop()` function, the flags are reset. This approach ensures stable interrupt and timer operation. 

In a way this design follows the principles of [distributed microservices](http://martinfowler.com/articles/microservices.html) where eash small part of the design has a clear specification and interface and prepares/processes only a small part of the total process.  The concept is well summarised [here](http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html): "In brief a Micro Service Architecture exists when your system is divided in small (single context bound) responsibilities blocks, those blocks doesn't know each other, they only have a common point of communication, generally a message queue, and does know the communication protocol and interfaces."  In this project we use MQTT between the ESP-based alarm and the rest of the world, but inside this software we use flags/semaphores to signal actions between different parts of the code.  Most of the action influencing the work happens in interrupt or timer service routines, but the actual time consuming work takes place in the `loop()` phase. This approach hardens the execution of the software against time overruns or blocking interrupts.  The end result is stable software execution.

### DS18B20

Any number of sensors can be placed on the bus. It seems that the code requires at least one device on the bus, otherwise the code hangs.  My application requires three temperatures to be sent to Weather Underground and to the Raspberry Pi for logging.  The sensor ID word is used as identification for the measured data. 

### Weather Underground Upload

The temperatures are uploaded to Weather Underground as additional temperatures (`tempxf` where x is 2,3, etc.).  The upload API protocol is described [here](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol).  The Weather Underground server returns a code to indicate success (or some fail code), but this return value is not processed other than displayed on the Serial output.


### MQTT

The main objective with this project is to send the information to a Raspberry Pi for recording purposes and to display in openHAB.  The MQTT broker/server also runs on the same Raspberry Pi.

The messages are transmitted on the `home/DS18B20/temperatureC/+` topic and messages can be displayed on any PC on the network by the Mosquitto (or any other) client subscription command:

    mosquitto_sub -v -d -t "home/DS18B20/temperatureC/+

where the `/+` indicates that all sensor data IDs must be shown. 
The payload comprises the current date and time and the measured temperature in the units indicated in the topic. 
The long strings with the date and temperature described above obviously did not work in openHAB, because openHAB expected only float values. To provide the required format for openHab, new topics were created that carries only the temperature.



### Wall clock time

The ESP has wall clock timekeeping (Arduino `timelib.h`) that is synchronised at regular intervals with an internet NTP server. The time of day is required to support the timestamping of environmental data. The code describes how to program the wall clock functionality.

### Interrupts

The PIR interrupts on GPIO pins are implemented  through Arduino-style `attachInterrupt()` functions.

### Timers

Only one software timer is set up to control regular events such as the alive-ping signal and the environmental sensor readings:

 - `aliveTimer` triggering regular alive messages and the temperature measurements.

The timer service routine sets a flag for subsequent servicing in the `loop()` phase.

### Web server

A simple web server is running on the IP address for this board (10.0.0.32). The server displays the temperatures for all the devices on the one-wire cable in deg C.  The server also displays the current time (to compare to the measurement times) and the status of the NTP sync flag (if the most recent sync attempt status).


## Wireless

### Fixed IP address
I have this thing about fixed IP addresses. In all my projects there may be more than
one ESP8266 device on the network and in order to do over the air (OTA) updates there
two choices: use a fixed IP address or use mDNS to resolve IP addresses.  The
fixed-IP-address seems simpler because all the configuration information is in one
file (the main.ino) file. See [here](https://github.com/NelisW/myOpenHab/blob/master/docs/417-ESP8266-over-the-air-OTA.md) how to implement fixed IP addresses.


### Over the Air Update (OTA)

OTA is faster than using the serial download and supports firmware deployment to
ESP boards irrespective of where they are, provided that network access is available
(which is a given, because the ESP8266 must be on the wifi network to do its thing).
See [here](https://github.com/NelisW/myOpenHab/blob/master/docs/417-ESP8266-over-the-air-OTA.md) how to implement OTA.

## Environmental sensors

### DS18B20 Temperature sensor

Install the `DallasTemperature` library (number 54) from <http://platformio.org/lib/show/54/DallasTemperature>.  
This will install both the  `DallasTemperature` library and its dependency, the `OneWire` library.  

Some users have difficulty getting the DS18B20 to work on the ESP8266.  A common complaint is that the temperatures are out of range at 85C, 100C, 127C or -127C.  Digging in to `DallasTemperature.h` revealed this:

    #define DEVICE_DISCONNECTED_C -127
    #define DEVICE_DISCONNECTED_F -196.6
    #define DEVICE_DISCONNECTED_RAW -7040

Also looking into the DS18B20 datasheet is is clear that 85C is the preloaded temperatures in the sensor, prior to any measurement execution.  So if you do read these values do some hardware fault finding.  I could not get the library going on GPIO pin 15 (D8 on my nodemcu), so I moved it to another pin and it worked well.

Note that the DS18B20 conversion time varies with the required resolution. The default resolution in the `DallasTemperature` library is nine bits, requiring just a little less than 100 ms.


| Mode|	Resolution|	Conversion time|
|---|---|----|
| 9 bits|	0.5°C	|93.75 ms|
| 10 bits|	0.25°C|	187.5 ms|
| 11 bits|	0.125°C|	375 ms|
| 12 bits|	0.0625°C|	750 ms|



## Hardware
GPIO00 is used for the one-wire interface.

The relatively large size of the code base requires that an ESP8266e be used, the memory in the ESP01 is too limited.
