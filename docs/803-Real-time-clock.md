# Real time clocks

## The time library

Note that Arduino and ESP8266 both have time libraries.
Look for time.h, time.c and time.ino
The smallest resolution available is one second, starting from 19700101.

There are small differences between the ESP (`time_t now = time(nullptr)`) and Arduino (`time_t t=now()`.

In ESP see this example: https://github.com/esp8266/Arduino/blob/master/tests/Time/Time.ino

https://github.com/esp8266/Arduino/blob/master/cores/esp8266/time.c

http://www.pjrc.com/teensy/td_libs_Time.html

http://playground.arduino.cc/Code/Time

## Links to set up from RTC or NTP

http://iot-playground.com/blog/2-uncategorised/23-esp8266-wifi-real-time-clock-display

http://www.buxtronix.net/2015/12/esp8266-based-ntp-clock.html
https://github.com/buxtronix/arduino/tree/master/esp8266-ledclock

http://iot-playground.com/blog/2-uncategorised/23-esp8266-wifi-real-time-clock-display

https://github.com/hwiguna/g33k/blob/master/ArduinoProjects/2015/_Done/118-ESP8266_RealTimeClock/HandwrittenClock_07_ESP/HandwrittenClock_07_ESP.ino

https://www.youtube.com/watch?v=XDGsnAyOXQs

http://thearduinoguy.org/using-an-esp8266-as-a-time-source/

this one may leak memory:
https://github.com/shantanugoel/esp8266-smartwatch/blob/master/user/ntp.c

http://richard.burtons.org/2015/05/02/a-simple-ntp-client-for-esp8266/
https://github.com/raburton/esp8266/tree/master/ntp

https://abzman2k.wordpress.com/2015/09/24/esp8266-rtc-and-ntp/

https://www.pjrc.com/teensy/td_libs_Time.html

http://www.makeuseof.com/tag/how-and-why-to-add-a-real-time-clock-to-arduino/

http://www.pjrc.com/teensy/td_libs_Time.html
