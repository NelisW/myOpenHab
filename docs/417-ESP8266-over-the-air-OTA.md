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

https://github.com/squix78/platformio-test

https://github.com/NelisW/IoTPlay/blob/master/PlatformIO-IDE/interrupt/src/main.ino

## How to do OTA

The following procedure works in the platformio environment.

In the main source file make the following includes:

    // start OTA block
    #include <ESP8266mDNS.h>
    #include <WiFiUdp.h>
    #include <ArduinoOTA.h>
    // end OTA block

In setup() include the following, after the `wifi.begin();wifi.config();` statements:

        //start OTA block
        ArduinoOTA.onStart([]() {
          Serial.println("Start");
        });
        ArduinoOTA.onEnd([]() {
          Serial.println("\nEnd");
        });
        ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
          Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
        });
        ArduinoOTA.onError([](ota_error_t error) {
          Serial.printf("Error[%u]: ", error);
          if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
          else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
          else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
          else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
          else if (error == OTA_END_ERROR) Serial.println("End Failed");
        });
        ArduinoOTA.begin();
        //end OTA block

In loop() include the following code at the top of the loop:

    // Start OTA block
    ArduinoOTA.handle();
    // end OTA block

Put the `upload_port` value in platformio.ini:

    [env:esp12e]
    platform = espressif
    framework = arduino
    board = esp12e
    upload_port = XXX.XXX.XXX.XXX

this will tell platformio to use the wifi to upload to the specified IP address.
In my case I hardcoded the IP address (not using DCHP and mDNS).
Uncomment the line in platformio.ini to disable OTA and use USB.

To hardcode the IP address do the following (replace with your own local IP, local gateway and subnet values)

    IPAddress ipLocal(XXX.XXX.XXX.XXX);
    IPAddress ipGateway(YYY, YYY, YYY, YYY);
    IPAddress ipSubnetMask(ZZZ, ZZZ, ZZZ, ZZZ);

    WiFi.mode(WIFI_STA); // set up in station mode
    WiFi.begin(wifi_ssid, wifi_password);
    //set up the static IP
    WiFi.config(ipLocal, ipGateway, ipSubnetMask);
