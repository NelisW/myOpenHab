# ESP8266 on the Arduino IDE


## Pin mapping nodeMCU to GPIO2

<https://github.com/esp8266/Arduino/blob/master/variants/nodemcu/pins_arduino.h#L37-L60>

    static const uint8_t SDA = 4;
    static const uint8_t SCL = 5;

    static const uint8_t SS    = 15;
    static const uint8_t MOSI  = 13;
    static const uint8_t MISO  = 12;
    static const uint8_t SCK   = 14;

    static const uint8_t LED_BUILTIN = 16;
    static const uint8_t BUILTIN_LED = 16;

    static const uint8_t A0 = 17;

    static const uint8_t D0   = 16;
    static const uint8_t D1   = 5;
    static const uint8_t D2   = 4;
    static const uint8_t D3   = 0;
    static const uint8_t D4   = 2;
    static const uint8_t D5   = 14;
    static const uint8_t D6   = 12;
    static const uint8_t D7   = 13;
    static const uint8_t D8   = 15;
    static const uint8_t D9   = 3;
    static const uint8_t D10  = 1;

## Setting up the Arduino IDE

Follow the instructions provided in 411-ESP8266-prepare-Arduino-IDE.md, with the details provided [here](http://www.wemos.cc/d1/Getting_Started).

Software can be update [over the air (OTA)](http://www.wemos.cc/d1/Wireless_Upload).

## Connecting the nodeMCU to the IDE

## Projects

<http://www.instructables.com/id/ESP8266-NodeMCU-v10-ESP12-E-with-Arduino-IDE/?ALLSTEPS>

## Why use C and not lua

http://internetofhomethings.com/homethings/?p=424

issues with expressif SKD http://internetofhomethings.com/homethings/?p=426    
Note that the SDK has been updated in the meantime.

issues with Arduino IDE  http://internetofhomethings.com/homethings/?p=429  
