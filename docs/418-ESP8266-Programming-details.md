# Programming details

<https://github.com/esp8266/Arduino/blob/master/doc/reference.md>    

<http://www.devacron.com/arduino-ide-for-esp8266/>  

<https://github.com/esp8266/arduino>


## Digital IO

Pin numbers in Arduino correspond directly to the ESP8266 GPIO pin numbers. pinMode, digitalRead, and digitalWrite functions work as usual, so to read GPIO2, call digitalRead(2).

Digital pins 0—15 can be INPUT, OUTPUT, or INPUT_PULLUP. Pin 16 can be INPUT, OUTPUT or INPUT_PULLDOWN_16. At startup, pins are configured as INPUT.

Pins may also serve other functions, like Serial, I2C, SPI. These functions are normally activated by the corresponding library.

In the Espressive SDK  The most usable pin functions are mapped to the macro SPECIAL, so calling pinMode(pin, SPECIAL) will switch that pin to UART RX/TX on pins 1 - 3, HSPI for pins 12-15 and CLK functions for pins 0, 4 and 5. SPECIAL maps to:

    0. CLK_OUT
    1. TX0
    2. TX1
    3. RX0
    4. CLK_XTAL
    5. CLK_RTC
    12. SPI_MISO
    13. SPI_MOSI
    14. SPI_CLK
    15. SPI_SS

You can activate any “FUNCTION_” with pinMode(pin, FUNCTION_1)for example
Note : func number 1-5 in Expressife table correspond to FUNCTION 0-4 in SDK

![ESP8266 pins](esp8266-pin_functions.png)


When using a GPIO as output (i.e. to drive something such as an LED) it is important to note that the maximum output current is 12mA.

## LED Pin

GPIO1 which is also TX is wired to the blue LED on many devices. Note that the LED is active low (conected to Vcc and sinks through the chip to ground) so setting a logical value of 0 will light it up. Since GPIO1 is also the TX pin, you won't be able to blink the LED and perform Serial communications at thew same time unless you switch TX/RX pins

## Interrupts

Pin interrupts are supported through attachInterrupt, detachInterrupt functions. Interrupts may be attached to any GPIO pin, except GPIO16. Standard Arduino interrupt types are supported: CHANGE, RISING, FALLING.

## Analog input

ESP8266 has a single ADC channel available to users. It may be used either to read voltage at ADC pin, or to read module supply voltage (VCC).

To read external voltage applied to ADC pin, use analogRead(A0). Input voltage range is 0 — 1.0V.

To read VCC voltage, use ESP.getVcc() and ADC pin must be kept unconnected. Additionally, the following line has to be added to the sketch:

    ADC_MODE(ADC_VCC);

This line has to appear outside of any functions, for instance right after the #include lines of your sketch.

The ADC cannot be used when the chip is transmitting. Otherwise the voltage may be inaccurate.(From Expressif datasheet CH 8.5)

## PWM

analogWrite(pin, value) enables software PWM on the given pin. PWM may be used on pins 0 to 15. Call analogWrite(pin, 0) to disable PWM on the pin. value may be in range from 0 to 1023. 0 to 255 is normal on an arduino board as its an 8bit ADC but ESP8266 is 10 bit so 1023 is full duty cycle.


## Timing and delays

millis() and micros() return the number of milliseconds and microseconds elapsed after reset, respectively.

delay(ms) pauses the sketch for a given number of milliseconds and allows WiFi and TCP/IP tasks to run. delayMicroseconds(us) pauses for a given number of microseconds.

Remember that there is a lot of code that needs to run on the chip besides the sketch when WiFi is connected. WiFi and TCP/IP libraries get a chance to handle any pending events each time the loop() function completes, OR when delay is called. If you have a loop somewhere in your sketch that takes a lot of time (>50ms) without calling delay, you might consider adding a call to delay function to keep the WiFi stack running smoothly.

There is also a yield() function which is equivalent to delay(0). The delayMicroseconds function, on the other hand, does not yield to other tasks, so using it for delays more than 20 milliseconds is not recommended.

## Serial

Serial object works much the same way as on a regular Arduino. Apart from hardware FIFO (128 bytes for TX and RX) HardwareSerial has additional 256-byte TX and RX buffers. Both transmit and receive is interrupt-driven. Write and read functions only block the sketch execution when the respective FIFO/buffers are full/empty.

Serial uses UART0, Serial1 uses UART1

By default the diagnostic output from WiFi libraries is disabled when you call `Serial.begin`. To enable debug output again, call `Serial.setDebugOutput(true);`

Upload via serial port:  Select “esptool” as a programmer, and pick the correct serial port. You need to put ESP8266 into bootloader mode before uploading code (pull GPIO0 low and toggle power).

Serial.print is interrupt-driven, so it is "fire and forget" most of the time, unless the TX buffer overflows. When it does, it blocks hard until it gets a TX_EMPTY interrupt, then it puts more data into the buffer.
Long story short: don't call Serial.print from interrupt, or expect that long strings will lead to a halt (and a WDT reset afterwards).
There's ets_printf which doesn't buffer and you can use it from interrupts. It may loose some characters though.


# Program memory

The Program memory features work much the same way as on a regular Arduino; placing read only data and strings in read only memory and freeing heap for your application. The important difference is that on the ESP8266 the literal strings are not pooled. This means that the same literal string defined inside a F("") and/or PSTR("") will take up space for each instance in the code. So you will need to manage the duplicate strings yourself.

    const char HTTP[] PROGMEM = "http:";
    ...
    {
       String response1;
       response1 += FPSTR(HTTP);
       ...
       String response2;
       response2 += FPSTR(HTTP);
    }


## WiFi(ESP8266WiFi library)

This is mostly similar to WiFi shield library. Differences include:

-  WiFi.mode(m): set mode to WIFI_AP, WIFI_STA, or WIFI_AP_STA.
-  call WiFi.softAP(ssid) to set up an open network
-  call WiFi.softAP(ssid, passphrase) to set up a WPA2-PSK network
-  WiFi.macAddress(mac) is for STA, WiFi.softAPmacAddress(mac) is for AP.
-  WiFi.localIP() is for STA, WiFi.softAPIP() is for AP.
-  WiFi.RSSI() doesn’t work
-  WiFi.printDiag(Serial); will print out some diagnostic info

WiFiServer, WiFiClient, and WiFiUDP behave mostly the same way as with WiFi shield library.

## Ticker

Library for calling functions repeatedly with a certain period. Two examples included.

##  EEPROM

This is a bit different from standard EEPROM class. You need to call EEPROM.begin(size) before you start reading or writing, size being the number of bytes you want to use. Size can be anywhere between 4 and 4096 bytes.

## I2C (Wire library)

Only master mode works

##  OneWire (from https://www.pjrc.com/teensy/td_libs_OneWire.html)

Library was adapted to work with ESP8266 by including register definitions into OneWire.h Note that if you have OneWire library in your Arduino/libraries folder, it will be used instead of the one that comes with the Arduino IDE (this one).

##  Other libraries

Libraries that don’t rely on low-level access to AVR registers should work well. Here are a few libraries that were verified to work:

-  PubSubClient MQTT library
-  DHT11 – initialize DHT as follows: DHT dht(DHTPIN, DHTTYPE, 15);
-  DallasTemperature
