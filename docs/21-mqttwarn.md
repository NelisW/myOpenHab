#mqttwarn on RPi

<https://github.com/jpmens/mqttwarn>   
<http://jpmens.net/2014/02/17/introducing-mqttwarn-a-pluggable-mqtt-notifier/>  
<http://jpmens.net/2014/04/03/how-do-your-servers-talk-to-you/>  


mqttwarn subscribes to any number of MQTT topics (with wildcards) and hands incoming messages off to plugins you configure to handle them. For example, you could have a topic monitor/home which sends alerts to your e-mail address, and another called phone/calls which notifies your smartphone via Pushover.

Notifications are sent to targets. A target is a combination of a service (e.g. Twitter, Pushover, SMTP, XBMC, etc.) and an "account" on that service. So, for example, suppose you wish to notify missed phone calls to yourself and your spouse, mqttwarn will do that. You could, at a later stage, also decide to log those to a file.

mqttwarn will also attempt to decode incoming messages from JSON. If that succeeds, you can transform the message before it's sent out. 

##Instaling mqttwarn

Go right to the end of the readme.md file on the github repo  
<https://github.com/jpmens/mqttwarn#installation> 

You'll need at least the following components:

- Python 2.x (tested with 2.6 and 2.7)
- An MQTT broker (e.g. Mosquitto)
- The Paho Python module: `sudo pip install paho-mqtt`

Installation

1. Clone this repository into a fresh directory 

	git clone https://github.com/jpmens/mqttwarn.git
	
2. Copy mqttwarn.ini.sample to mqttwarn.ini and edit to your taste. A good start is to use the ini file shown at <https://github.com/jpmens/mqttwarn#getting-started>

3. Install the prerequisite Python modules for the services you want to use

4. Launch mqttwarn.py. JPM recommends you use [Supervisord](http://supervisord.org/) for running the script.  For starters just open a terminal and run `./mqttwarn.py`

5. Proceed to test the installation as described in <https://github.com/jpmens/mqttwarn#getting-started>.  

6. Look at <http://jpmens.net/2014/04/03/how-do-your-servers-talk-to-you/> and see if you can get the smtp and pushover services working.
Setting up Pushover is outlined in the file `22-pushover-notification.md`.


##mqttwarn ini file

The following `mqttwarn.ini` file reports all MQTT messages on the `test\+` topic to
1. the mqttwarn log file
2. a message file located at `/tmp/mqtt.log`
3. sends a gmail notification and 
4. sends a Pushover notification

	[defaults]
	hostname  = 'masterPi'
	port      = 1883
	; name the service providers you will be using.
	launch   = file, log, smtp, pushover

	[config:file]
	append_newline = True
	targets = {
		'mylog'     : ['/tmp/mqtt.log']
		}

	[config:log]
	targets = {
		'info'   : [ 'info' ]
	  }

	[config:pushover]
	targets = {
		'appkey'      : ['your user key', 'your app key for mqttwarn'],
	  }

	[config:smtp]
	server  =  'smtp.gmail.com:587'
	sender  =  "yourGmailUser@gmail.com"
	username  =  "yourGmailUser@gmail.com"
	password  =  "yourGmailPassword<Saw"
	starttls  =  True
	targets = {
		'gmail'     : [ 'recipient01@gmail.com', 'recipient02@gmail.com' ],
		}

	[test/+]
	targets = file:mylog, log:info, smtp:gmail, pushover:appkey

These `test/+` MQTT messages can be published by any MQTT source, on the command line, as in 

	mosquitto_pub -t 'test/topic' -m 'helloWorld'
	
or from your openHab or any other application.

If you have another PC connected to the same network as the RPi, test the system with the following command:

	mosquitto_pub -h x.x.x.x -p 1883 -t "test/play" -m "howzat!"

where the x.x.x.x is the IP address of your RPi.  It should interact with the RPi's MQTT broker and relay the message.


For this to work, you have to have the following installed:

1. MQTT broker, such as mosquitto must be installed and running in the background.
2. warnmqtt must be installed and running in the background (use supervisord for that purpose (see 03-diverseSoftwareRPi.md).
3. you must have an account on pushover with known User Key
4. the warnmqtt plugin application must be registered against your pushover user account.
5. you must have installed and set up smtp with an active email account, e.g., a gmail account.








