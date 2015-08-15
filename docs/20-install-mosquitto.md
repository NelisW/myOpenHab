#Install mosquitto on RPi

<http://mosquitto.org/download/>  
<http://jpmens.net/2013/09/01/installing-mosquitto-on-a-raspberry-pi/>

##Installing the broker and clients

Install the mosquitto lib on RPi, **But do not use JPM's commands**. mosquitto is now in the debian distribution (<http://mosquitto.org/download/>). Just do this:

	sudo apt-get install mosquitto
	sudo apt-get install mosquitto-clients
	sudo apt-get install python-mosquitto

To install the broker (first line), clients (second line) and the python bindings (third line).

The broker is immediately started; stop it in order to configure it:

	sudo /etc/init.d/mosquitto stop

##Testing

Test the installation as follows:
<http://stackoverflow.com/questions/26716279/how-to-test-the-mosquitto-server>

1. Start the broker:

	sudo /etc/init.d/mosquitto start

2. Start the command line subscriber:

	mosquitto_sub -v -t 'test/topic'

3. Publish test message with the command line publisher:

	mosquitto_pub -t 'test/topic' -m 'helloWorld'
	
As well as seeing both the subscriber and publisher connection messages in the broker terminal the following should be printed in the subscriber terminal:

	test/topic helloWorld	
	
##Authentication and security 	

By default mosquitto has no security protection.  Two methods of secure operation are possible:

1. Username/password:  this option sends the open password over the network and is fine for authentication and not safe on open networks.

2. Certificates: a symmetric key pair is used to authenticate the messages.

Todo: complete the security section

<https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh>

http://stackoverflow.com/questions/27534953/how-do-i-set-up-my-own-mqtt-server-with-mosquitto

http://mosquitto.org/man/mosquitto-tls-7.html

http://mosquitto.org/man/mosquitto-conf-5.html

http://stackoverflow.com/questions/18896087/mosquitto-mqtt-broker-and-java-client-with-ssl-tls

http://stackoverflow.com/questions/29576230/arduino-with-mosquitto-mqtt

http://stackoverflow.com/questions/26657319/how-do-you-set-up-encrypted-mosquitto-broker-like-a-webpage-which-has-https

