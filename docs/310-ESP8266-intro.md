#ESP8266

detail to follow - currently this file only contains links.


[ESP8266 community](http://www.esp8266.com/)

[nodeMCU](http://nodemcu.com/index_en.html)

[MicroPython on ESP8266](https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266))

[Spec](https://www.adafruit.com/images/product-files/2471/0A-ESP8266__Datasheet__EN_v4.3.pdf)

[Arduino code for ESP8266](https://github.com/esp8266/Arduino)

[Catalogue of ESP8266 modules](http://www.happybison.com/reviews/esp8266-based-esp-modules-10/)

[Overview with some technical data](https://nurdspace.nl/ESP8266)

[Somewhat confusing post](http://www.instructables.com/id/ESP8266-based-web-configurable-wifi-general-purpos-1/)

[long series of posts](http://horaciobouzas.com/)

[lua on ESP8266](https://www.youtube.com/watch?v=_GSYZ1e14nc)

Nice series of articles:  

1. [Getting started with AT commands](https://alselectro.wordpress.com/2015/05/05/wifi-module-esp8266-1-getting-started-with-at-commands/)

2. [Setting up](https://alselectro.wordpress.com/2015/05/13/wifi-module-esp8266-2-tcp-client-server-mode/)

3. [Connect to Android Mobile](https://alselectro.wordpress.com/2015/05/13/wi-fi-module-esp8266-3-connect-to-android-mobile/)

4. [Control from anywhere in the World–Internet of Things](https://alselectro.wordpress.com/2015/05/31/wi-fi-module-esp8266-4-control-from-anywhere-in-the-worldinternet-of-things/)


[ESD8266-Dev,SDIO mode, UART mode and FLASH mode.](https://www.olimex.com/Products/IoT/MOD-WIFI-ESP8266-DEV/resources/MOD-WIFI-ESP8266-DEV_jumper_reference.pdf)


##Setting up
Remember to secure the ESP8266 if used in access point mode.

ESP8266 WIFI module has [3 modes of operation](https://alselectro.wordpress.com/2015/05/13/wifi-module-esp8266-2-tcp-client-server-mode/).

- ST  – Station mode in which ESP acts as a device & connects to an existing Access point.

- AP – Access Point mode where the ESP itself acts as AP & other devices like Mobile can connect to it.

- Both – ST & AP both mode is allowed in ESP.The mode of operation is set by the AT command


[Boot modes](https://github.com/esp8266/esp8266-wiki/wiki/Boot-Process)

[Firmware upgrade](https://alselectro.wordpress.com/2015/07/28/esp8266-wifi-firmware-upgrading/#comment-1506)


http://rancidbacon.com/files/kiwicon8/ESP8266_WiFi_Module_Quick_Start_Guide_v_1.0.4.pdf

##AT commands
ESP8266, in it’s default configuration, boots up into the serial modem mode. In this mode you can communicate with it using a set of AT commands.  ESP8266 expects <CR><LF> or CarriageReturn and LineFeed at the end of each command, but just<CR> seems to work too.


https://room-15.github.io/blog/2015/03/26/esp8266-at-command-reference/



##ESP-12 series

[Getting Started with the ESP8266 ESP-12](http://www.instructables.com/id/Getting-Started-with-the-ESP8266-ESP-12/?ALLSTEPS)

[ESP-12 spec](https://www.mikrocontroller.net/attachment/243558/fcc_11.pdf)

ESP-12 modules have metal shield with FCC logo on it. It appears these modules are FCC approved (FCC ID: 2ADUIESP-12). The modules have 16 pins and PCB antenna. Similar to ESP-07, some ESP-12 boards have GPIO 4 and 5 switched.  The newer ESP-12-E module adds 5 more half-hole (without extra hole) pins on the side. There are also two more variations of ESP-12-E module: ESP-12-D and ESP-12-Q. Probably referring to Dual and Quad SPI operations for Flash chip because ESP-12-D frees up GPIO 9 and GPIO 10 which are usually occupied for Quad mode SPI operations.