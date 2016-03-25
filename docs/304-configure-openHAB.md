# Configuring the openHAB runtime

## Users and passwords

The openHAB usernames and passwords are stored in the file 
`/opt/openhab/configurations/users.cfg`.  The entries in this file must be of the format

	yourusername=yourpassword
	
ignore the test beyond the comma in the example entry, it is not yet implemented.


## Configure MQTT

<http://www.homeautomationforgeeks.com/project/openhab.shtml>

Edit the openHAB config file

	sudo nano /opt/openhab/configurations/openhab.cfg

Scroll to the Transport section and look for the MQTT transport section.  Look for the lines that contain `<broker>.url` and `<broker>.retain` and uncomment them.  Change them to the mosquitto broker that is running on the RPi.  Give the broker a name in the `<broker>` part - this name will be used later to refer to your broker.

	mqtt:mymosquitto.url=tcp://localhost:1883
	mqtt:mymosquitto.retain=true

You can set `localhost` to the IP address of the RPi.
    
You may also decide to set the last-will-and-testament .lwt to send a final message when closing down.

Also add these lines immediately after the line where you set lwt.  
<http://www.element14.com/community/community/design-challenges/forget-me-not/blog/2014/09/17/fmnxx-mqtt--the-language-of-iot>  
<http://jpmens.net/2014/01/14/a-story-of-home-automation/>  
<https://groups.google.com/forum/# !topic/openhab/mkthISbmmvU>  

    mqtt-eventbus:broker=mymosquitto
    mqtt-eventbus:commandPublishTopic=/home/out/${item}/command
    mqtt-eventbus:statePublishTopic=/home/state/${item}/state

After editing restart the daemon to note the new config settings:

		sudo /etc/init.d/openhab restart

Save and exit the file.

## Notes on configuring openHAB

Read these pages:
<https://github.com/openhab/openhab/wiki/Configuring-the-openHAB-runtime>  

You use the openHAB Designer, but you can also edit the files with a normal file editor.  The files must be in UTF-8 encoding.

Item and sitemap files  can be changed during runtime, with no need to restart openHAB.

The global configuration is done in the `openhab.cfg` file.  Changes made to this file have impact throughout all sitemaps.  There is a default version of this file which can be used as a template for your own work: make a copy of the default and edit the copy.

The most common global configuration changes are to activate specific bindings by uncommenting the appropriate lines, e.g., as when the MQTT binding was activated above in this file.

## Item definitions

Item files are stored in `/opt/openhab/configurations/items`.
Although items can be dynamically added, it is most common to statically define most of the items.  These static definition files follow a prescribed syntax.
For more information on how to create item files see here:  
<https://github.com/openhab/openhab/wiki/Explanation-of-Items>  

For an example see here
<http://www.homeautomationforgeeks.com/project/openhab.shtml>

	sudo nano /opt/openhab/configurations/items/default.items
	
Add the following text:

    Group All
    Group gGroundFloor (All)
    Group GF_Study "Study" <video> (gGroundFloor)
    Number StudyTemperature "Room Temperature [%.1f C]" <temperature> (GF_Study) {mqtt="<[mymosquitto:home/study/RoomTemperature:state:default]"}

    Number CPUTemperature "CPU Temperature [%.1f C]" <temperature> (GF_Study) {mqtt="<[mymosquitto:home/study/CPUTemperature:state:default]"}

    Switch PiLED "Pi-LED" (GF_Study) {mqtt=">[mymosquitto:/home/study/PiLED:command:on:ON],>[mymosquitto:/home/study/PiLED:command:off:OFF],<[mymosquitto:/home/study/PiLED:state:default]"}
    
The item lines have the following format:

    itemtype itemname ["labeltext"] [<iconname>] [(group1, group2, ...)] [{bindingconfig}]   
    
That last two lines are where we tell OpenHAB about our temperature sensor and LED. The parts are:

- itemtype: (Number/Switch) the type of the value.

- itemname: (TestTemperature/PiLED) a name for this item.

- labeltext: ("Temperature [%.1f C]"/"PiLED") how we want the value to be displayed. "%.1f" is a way to format a decimal number

- iconname: (<temperature>/<light>) the name of a built-in icon to display (a thermometer).

- [(group1, group2, ...)]: (GF_Living) which group this item belongs to.

- [{bindingconfig}]: {mqtt="<[mymosquitto:home/temperature:state:default]"}: where to get the value. This is telling OpenHAB to use the MQTT binding named "mymosquitto" (which we set up earlier) and to listen to the home/temperature channel. "state" is the type (another value is "command") and "default" is the transformation (in this case, no transformation). The < sign near the beginning means that we'll read from the channel (as opposed to writing to it).

## Sitemap definitions

Sitemap files are stored in `/opt/openhab/configurations/sitemaps`.
Sitemaps are used to define the user interface hierarchy - like a map of your home.
For more information on how to create item sitemap files see here:  
<https://github.com/openhab/openhab/wiki/Explanation-of-Sitemaps>  

	sudo nano /opt/openhab/configurations/sitemaps/default.sitemap
	
Add the following text

    sitemap default label="Main Menu"
    {
            Frame label="Study" {
                    Text item=StudyTemperature
                    Text item=CPUTemperature
            Switch item=PiLED label="Pi-LED" mappings=[ON="On",OFF="Off"]
            }
    }	

## Test the simple demo

Send a temperature value  with this mqtt publish command

	mosquitto_pub -t "home/temperature" -m "12"
	
or from another PC on the network send

	mosquitto_pub -h yourRPiIPaddress -t "home/temperature" -m "12"
	
When the above sitemap and items file are selected in the Android app, the light switch can be tested by opening a terminal and running a mqtt client to listen to the PiLED topics:

    mosquitto_sub -t "/home/study/PiLED"
    
Now, if the On or Off switch on the light entry in the Android app is touched, the mqtt client in the terminal responds with the text: `ON`, or `OFF`.  Hence we can conclude that openHAB published the messages on mqtt.  The next step is to capture these messages and actually switch the light on and off.








## Other files

Rule files are stored in `/opt/openhab/configurations/rules`. Rules provide flexible logic to openHAB for automation which can also use scripts(macros) using related events and actions.
Script files are stored in `/opt/openhab/configurations/scripts`.

Persistence  files are stored in `/opt/openhab/configurations/persistence`.
Persistences can store item states over a time (a time series).



# todo this later:

## Security

Documentation of openHAB's security features
Introduction

To secure the communication with openHAB there are currently two mechanisms in place

    HTTPS
    Authentication

Authentication is implemented by SecureHttpContext which in turn implements HttpContext. This SecureHttpContext is registered with the OSGi !HttpService and provides the security hook handleSecurity. At least all authentication requests are delegated to the javax.security.auth.login.LoginContext.LoginContext which is the entry point to JAAS (http://en.wikipedia.org/wiki/Java_Authentication_and_Authorization_Service) !LoginModules.

The SecureHttpContext is currently used by the WebAppServlet and the CmdServlet which constitutes the default iPhone UI as well as the RESTApplication which provides the REST functionality.
HTTPS

openHAB supports HTTPS out of the box. Just point your browser to

https://127.0.0.1:8443/openhab.app?sitemap=demo#

and the HTTP communication will be encrypted by SSL.

If you prefer to use your own X.509 certificates, you can. Configure_SSL has information on how to do that, and there's a step-by-step guide specifically for openHAB users.
Authentication

In order to activate Authentication one has to add the following parameters to the openHAB start command line

    -Djava.security.auth.login.config=./etc/login.conf - the configuration file of the JAAS !LoginModules

By default the command line references the file <openhabhome>/etc/login.conf which in turn configures a PropertyFileLoginModule that references the user configuration file login.properties. One should use all available LoginModule implementation here as well (see http://wiki.eclipse.org/Jetty/Tutorial/JAAS for further information).

The default configuration for login credentials for openHAB is the file <openhabhome>/configuration/users.cfg. In this file, you can put a simple list of "user=pwd" pairs, which will then be used for the authentication. Note that you could optionally add roles after a comma, but there is currently no support for different roles in openHAB.

## More information


https://github.com/openhab/openhab/wiki/Explanation-of-Items

https://github.com/openhab/openhab/wiki/Explanation-of-Sitemaps


[Use a MAP](http://forum.mysensors.org/topic/1405/adding-a-light-switch-to-openhab-mqtt-gateway/2):

    Switch node1_sw1 "sw1" {mqtt=">[mysensors:MyMQTT/1/1/V_LIGHT:command:ON:1],>[mysensors:MyMQTT/1/1/V_LIGHT:command:OFF:0],<[mysensors:MyMQTT/1/1/V_LIGHT:command:MAP(1on0off.map)]"}

