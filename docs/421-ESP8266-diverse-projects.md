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
