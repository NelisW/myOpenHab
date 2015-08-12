#mqttwarn on RPi

<https://github.com/jpmens/mqttwarn>   
<http://jpmens.net/2014/02/17/introducing-mqttwarn-a-pluggable-mqtt-notifier/>  
<http://jpmens.net/2014/04/03/how-do-your-servers-talk-to-you/>  


mqttwarn subscribes to any number of MQTT topics (with wildcards) and hands incoming messages off to plugins you configure to handle them. For example, you could have a topic monitor/home which sends alerts to your e-mail address, and another called phone/calls which notifies your smartphone via Pushover.

Notifications are sent to targets. A target is a combination of a service (e.g. Twitter, Pushover, SMTP, XBMC, etc.) and an "account" on that service. So, for example, suppose you wish to notify missed phone calls to yourself and your spouse, mqttwarn will do that. You could, at a later stage, also decide to log those to a file; no problem.

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
