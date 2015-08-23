# myOpenHab

##Overview
An implementation of a DIY home automation system based on openHab, mosquitto MQTT, mqttwarn, and lua or C, running on ESP8266 and Raspberry Pi.

In doing this work we are inspired by these noteworthy projects:

- <https://openhardwarecoza.wordpress.com/2015/03/29/openhab-mqtt-arduino-and-esp8266-part-1-setting-up-your-environment/>

- <http://www.instructables.com/id/Uber-Home-Automation-w-Arduino-Pi>

- <https://electronichamsters.wordpress.com/2014/06/09/home-automation-with-arduino-and-openhab/>

We intend to use these technologies and tools:

- <http://www.openhab.org/> and <https://my.openhab.org/>

- <http://mosquitto.org/> and <https://github.com/jpmens/mqttwarn>

- <https://pushover.net/>

- <http://nodemcu.com/index_en.html>

- <https://github.com/esp8266/Arduino>

- <https://www.raspberrypi.org/>

- <http://www.esp8266.com/>


##Status

Warning: I am a tool freak: a job started with the right tools is 50% done at the moment you start.  This project is built on top of a series of  tools, integrated together into a powerful and easy to use/maintain system.  At present I am still waiting for most of the hardware - somewhere in the mail.  The Raspberry Pi is running. 

The current status of this project is very early pre-alpha.  It will take some time to complete this project.

At present we installed most of the tools detailed in the `docs` folder (smpt, mosquitto, mqttwarn, supervisor). A DS18B20 temperature sensor is running on the RPi and the ambient room temperature and RPi CPU temperature are running in a small openHAB design, on the my.openHAB cloud.
If the RPi CPU temperature exceeds a given threshold, a notification is pushed to Pushover.

Our languages of choice in order of preference are Python, C or lua.  The initial implementation will probably use lua, simply because of the strong lua support for the ESP8266.  Later the code will be migrated to C. Even later we might be using micropython, but the ESP8266 implementation for micropython is still under development and not yet stable enough.



  
