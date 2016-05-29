# MQTT Tips

## How To:  Topic definitions

[Topic naming](http://blog.hekkers.net/2012/09/18/mqtt-about-dumb-sensors-topics-and-clean-code/# comment-20582)


[Republising MQTT with new topics](http://lodge.glasgownet.com/2012/09/23/mqtt-republishing-itch/)


## Homie
Homie is a lightweight MQTT convention for the IoT.


https://github.com/marvinroger/homie

https://github.com/marvinroger/homie-server



Homie for ESP8266:   

https://github.com/marvinroger/homie-esp8266   

https://github.com/marvinroger/homie-esp8266/wiki  

 -  Automatic connection/reconnection to Wi-Fi/MQTT
 -  Cute JSON configuration file to configure the credentials of the device
 -  Cute API / Web UI / App to get information about the device and to remotely send the configuration to the device
 -  OTA support
 -  Available in the PlatformIO registry
 -  Pretty straightforward sketches

### keep this safe here - work on this later



## Attend to this later, just keep it safe here so long

http://openenergymonitor.blogspot.co.za/2015/12/openenergymonitor-emonpi-and-openhab.html?m=1
For example the line in the items file to pull power 1 from emonhub MQTT is as follows:
Number  emonpi_ct1       "Power 1 [%d W]"    { mqtt="<[mosquitto:emonhub/rx/5/values:state:REGEX((.*),.*,.*,.*,.*,.*,.*,.*,.*,.*,.*)]" }
Notice the REGEX is used to tell openHAB that we want the first value in the 11 part CSV emonhub posts to MQTT to emonhub/rx/5/values.

Number emonpi_ct1 "Power 1 [%d W]" { mqtt="<[mosquitto:emonhub/rx/5/values:state:REGEX((.*),.*,.*,.*,.*,.*,.*,.*,.*,.*,.*)]" }

or

Number emonpi_ct1 "Power 1 [%d W]" { mqtt="<[mosquitto:emonhub/rx/5/values:state:REGEX((.*?),.*?,.*?,.*?,.*?,.*?,.*?,.*?,.*?,.*?,.*?)]" }

Seem to work fine for me. Either with or without the '?'. What effect does adding '?' have?

Most regex quantifiers (such as * or +) are "greedy". That is : they will look for the biggest string which matches the expression. The question mark make them "lazy"; looking for the shortest string.

For instance, here is a sample string : "whatever". If you have the following regex /<.+>/, it will match the full string. If you use /<.+?>/, it will match "".

In your case, it does not change much it terms of match but it may have a performance impact. I think using ? make it faster because it won't try to read the whole string to see if there's a longer match.

You could also use /([^,]*),[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*/. This may be even better in terms of performance. [^,]* means any string not containing ",".

But if you want to only retrieve the first field (and not checking there is exactly 11 fields, then you could use /^([^,]*)/ which will find the first substring not containing a ",".


