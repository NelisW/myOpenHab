# ESP8266 Over the air (OTA) update

<https://github.com/esp8266/Arduino/blob/master/doc/ota_updates/ota_updates.md>

OTA (Over the Air) update is the process of loading the firmware to ESP module using Wi-Fi connection rather that a serial port. Such functionality became extremely useful in case of limited or no physical access to the module.

OTA may be done using:

-  Arduino IDE
-  Web Browser
-  HTTP Server

Arduino IDE option is intended primarily for software development phase. The two other options would be more useful after deployment, to provide module with application updates manually with a web browser or automatically using a http server.

In any case first firmware upload have to be done over a serial port. If OTA routines are correctly implemented in a sketch, then all subsequent uploads may be done over the air.


http://www.esp8266.com/viewtopic.php?f=29&t=6022

http://www.penninkhof.com/2015/12/1610-over-the-air-esp8266-programming-using-platformio/
