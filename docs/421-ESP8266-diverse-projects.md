# ESP8266 Diverse Projects

## Weather station with DS18B20, DHT11 and BMP085

http://internetofhomethings.com/homethings/?p=345

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
