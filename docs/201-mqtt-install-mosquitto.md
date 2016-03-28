# Install mosquitto on RPi

Why?
<https://www.element14.com/community/community/design-challenges/forget-me-not/blog/2014/09/17/fmnxx-mqtt--the-language-of-iot>

<http://mosquitto.org/download/>  
<http://jpmens.net/2013/09/01/installing-mosquitto-on-a-raspberry-pi/>  
<http://www.homeautomationforgeeks.com/mosquitto.shtml>  
<http://www.element14.com/community/community/design-challenges/forget-me-not/blog/2014/09/17/fmnxx-mqtt--the-language-of-iot>


Mosquitto is an open-source message broker, which means it allows different programs to exchange information in a way they can all understand.

## Installing the broker and clients

Install the mosquitto lib on RPi, **But do not use JPM's commands**. mosquitto is now in the debian distribution (<http://mosquitto.org/download/>). Just do this:

	sudo apt-get install mosquitto
	sudo apt-get install mosquitto-clients
	sudo apt-get install python-mosquitto

To install the broker (first line), clients (second line) and the python bindings (third line).

The broker is immediately started; stop it in order to configure it:

	sudo /etc/init.d/mosquitto stop

## installing mosquitto from source:  

http://blog.thingstud.io/recipes/how-to-make-your-raspberry-pi-the-ultimate-iot-hub/

## Testing

Test the installation as follows:
<http://stackoverflow.com/questions/26716279/how-to-test-the-mosquitto-server>

1. Start the broker:

	sudo /etc/init.d/mosquitto start

2. Start the command line subscriber (-d is for debug information, -v is for verbose)

	mosquitto_sub -v -d -t "test/topic"

3. Publish test message with the command line publisher:

	mosquitto_pub -t "test/topic" -m 'helloWorld'

As well as seeing both the subscriber and publisher connection messages in the broker terminal the following should be printed in the subscriber terminal:

	test/topic helloWorld

## Authentication and security 	

By default mosquitto has no security protection.  Various methods of secure operation are possible:

1. Username/password:  this option sends the open password over the network and is fine for authentication but is not safe on open or insecure networks.

2. Certificates: a symmetric key pair is used to authenticate the messages.

3. Asymmetric encryption, although this is not quite the use case for asymmetric encryption.

Note that having a limited number of simple messages (like on/off) could be to vulnerable to attack, so pad simple messages with random data (e.g., if one bit is used to signal on/off, add 63 bits of random data).




Todo: complete the security section

<https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh>

http://stackoverflow.com/questions/27534953/how-do-i-set-up-my-own-mqtt-server-with-mosquitto

http://mosquitto.org/man/mosquitto-tls-7.html

http://mosquitto.org/man/mosquitto-conf-5.html

http://stackoverflow.com/questions/18896087/mosquitto-mqtt-broker-and-java-client-with-ssl-tls

http://stackoverflow.com/questions/29576230/arduino-with-mosquitto-mqtt

http://stackoverflow.com/questions/26657319/how-do-you-set-up-encrypted-mosquitto-broker-like-a-webpage-which-has-https
