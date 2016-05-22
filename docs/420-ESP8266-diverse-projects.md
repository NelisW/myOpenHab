# ESP8266 Diverse Projects

## Web-based ESP environments

A somewhat confusing [post](http://www.instructables.com/id/ESP8266-based-web-configurable-wifi-general-purpos-1/)

The [ESPEasy project](http://www.esp8266.nu/index.php/Main_Page)

## Miscellaneous projects

<http://horaciobouzas.com/> has a number of project posts, some of which are in the amateur radio context.  The author also sells PCBs for some of his projects.

[Connecting two ESP8266](http://randomnerdtutorials.com/how-to-make-two-esp8266-talk/), one as access point and one as station

[Using Blynk with ESP8266-as-Arduino-Uno-wifi](http://www.instructables.com/id/Connect-to-Blynk-using-ESP8266-as-Arduino-Uno-wifi/)

[Wireless logger ESP8266 NodeMCU v1.0 with Arduino IDE](http://www.instructables.com/id/ESP8266-NodeMCU-v10-ESP12-E-with-Arduino-IDE/)

## Weather station with DS18B20, DHT11 and BMP085

http://internetofhomethings.com/homethings/?p=345

http://www.survivingwithandroid.com/2016/04/iot-arduino-programming-monitor-environment.html

## Intro with remote power switching

http://www.instructables.com/id/An-inexpensive-IoT-enabler-using-ESP8266/?ALLSTEPS

## ESP with DHT and display
https://nathan.chantrell.net/20141230/wifi-mqtt-display-with-the-esp8266  
https://github.com/nathanchantrell/esp_mqtt_oled  

## ESPwifiwebserver

https://github.com/iot-playground/Arduino/blob/master/ESP8266ArduinoIDE/WiFiWebServer/WiFiWebServer.ino

This sketch demonstrates how to set up a simple HTTP-like server.  
The server will set a GPIO pin depending on the request  
http://server_ip/gpio/0 will set the GPIO2 low,  
http://server_ip/gpio/1 will set the GPIO2 high  
server_ip is the IP address of the ESP8266 module, will be   
printed to Serial when the module is connected.  


## WiFiManager

<https://github.com/tzapu/WiFiManager>

ESP8266 WiFi Connection manager with fallback web configuration portal
The configuration portal is of the captive variety, so on various devices it will present the configuration dialogue as soon as you connect to the created access point.

-  when your ESP starts up, it sets it up in Station mode and tries to connect to a previously saved Access Point
-  if this is unsuccessful (or no previous network saved) it moves the ESP into Access Point mode and spins up a DNS and WebServer (default ip 192.168.4.1)
-  using any wifi enabled device with a browser (computer, phone, tablet) connect to the newly created Access Point
-  because of the Captive Portal and the DNS server you will either get a 'Join to network' type of popup or get any domain you try to access redirected to the configuration portal
-  choose one of the access points scanned, enter password, click save
-  ESP will try to connect. If successful, it relinquishes control back to your app. If not, reconnect to AP and reconfigure.


## Simple Arduino IDE example

https://dzone.com/articles/its-time-develop-applications

flashes two leds

## ESPEasy

http://sourceforge.net/projects/espeasy/?source=typ_redirect

http://www.esp8266.com/viewtopic.php?f=29&t=4540

http://www.esp8266.nu/forum/viewtopic.php?t=37

http://www.whatimade.today/esp8266-on-websockets-mdns-ota-and-leds/

## OTA house project

http://www.whatimade.today/esp8266-on-websockets-mdns-ota-and-leds/

ESP8266 - On Websockets, mdns, OTA and LEDS

So what this project consists?

-  An ESP8266 which controls a 7 meters, 5050 RGB 12V led strip, 60Leds/meter.
-  The ESP8266 is connected to the house router via WiFi.
-  The ESP8266 receives data through a websocket on port 81, which means it can be controlled from any browser/OS.
-  It supports mdns, so no need for IP address to communicate with the ESP8266 (Partially at the moment).
-  It supports OTA (Over-The-Air) updates - So no need to connect it to the computer to update the code.

## iot-playground


http://iot-playground.com/

http://iot-playground.com/download

http://iot-playground.com/blog/2-uncategorised/67-arduino-esp8266-ide

http://iot-playground.com/blog/2-uncategorised/35-esp8266-firmware-update

http://iot-playground.com/blog/2-uncategorised/15-esp8266-wifi-temperature-and-humidity-sensor

http://iot-playground.com/blog/2-uncategorised/21-esp8266-wifi-air-pressure-and-weather-forecast-sensor

http://iot-playground.com/blog/2-uncategorised/41-esp8266-ds18b20-temperature-sensor-arduino-ide

http://iot-playground.com/blog/2-uncategorised/74-esp8266-wifi-pir-motion-sensor-easyiot-cloud-rest-api

## internetofhomethings

http://internetofhomethings.com/homethings/?page_id=207


## Weather station

https://github.com/squix78/platformio-test




## Diverse Projects

[Low power sensor board](https://github.com/z2amiller/sensorboard).

<http://randomnerdtutorials.com/7-weekend-projectstutorials-for-the-esp8266-wifi-module/>

<http://randomnerdtutorials.com/how-to-control-your-esp8266-from-anywhere-in-the-world/>

http://blog.thethings.io/connect-esp8266-to-the-internet-at-thethings-io/
