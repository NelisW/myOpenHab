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

## Configuring

http://www.switchdoc.com/2016/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/

Open the file as follows:

	sudo nano /etc/mosquitto/mosquitto.conf

## Running as a service

I found the default init.d method does not work (jessie). This works:  
https://xperimentia.com/2015/08/20/installing-mosquitto-mqtt-broker-on-raspberry-pi-with-websockets/

The following instructions include the installation of a systemd unit file in place of the older init.d script which is used with Raspbian Wheezy. The older init.d script is included  with the Mosquitto installation. While the newer systemd which is used in Raspbian Jessie is backward compatible with the init.d script, the systemd unit file is much simpler and more efficient. 

If you are running Raspbian light you may need to install Git. You can do so with:

First disable the init.d script:

	sudo update-rc.d mosquitto remove

Then

	sudo git clone https://github.com/Dan-in-CA/mosquitto_unit_file.git

copy the mosquitto.service file

	sudo cp mosquitto_unit_file/mosquitto.service /etc/systemd/system/mosquitto.service

Enable the service

		sudo systemctl enable mosquitto.service

After a reboot you can use:

sudo systemctl status | stop | start | restart mosquitto

to control the mosquitto daemon. This is extremely useful when editing and testing the mosquitto.conf file.


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


https://medium.com/@eranda/setting-up-authentication-on-mosquitto-mqtt-broker-de5df2e29afc

Password file will contain your username and the encrypted password. Run the following command to create and add a user to this file.

	sudo mosquitto_passwd -c /etc/mosquitto/passwd <user_name>

Then, you will be asked for your password twice, enter that too.

Now we have to give the location of the password file to the Mosquitto broker config file. To do that open the mosquitto.conf file using the following command,

sudo gedit /etc/mosquitto/mosquitto.conf

And add/change following two entries to the mosquitto.conf file (pwfile is the password filename, and`allow_anonymous false` prevents unauthenticated access),

	password_file /etc/mosquitto/pwfile
	allow_anonymous false


Todo: complete the security section
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04
https://primalcortex.wordpress.com/2016/11/08/mqtt-mosquitto-broker-client-authentication-and-client-certificates/


## mqtt-spy

https://github.com/kamilfb/mqtt-spy
https://github.com/kamilfb/mqtt-spy/wiki/Downloads



## Notes


<https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh>

http://stackoverflow.com/questions/27534953/how-do-i-set-up-my-own-mqtt-server-with-mosquitto

http://mosquitto.org/man/mosquitto-tls-7.html

http://mosquitto.org/man/mosquitto-conf-5.html

http://stackoverflow.com/questions/18896087/mosquitto-mqtt-broker-and-java-client-with-ssl-tls

http://stackoverflow.com/questions/29576230/arduino-with-mosquitto-mqtt

http://stackoverflow.com/questions/26657319/how-do-you-set-up-encrypted-mosquitto-broker-like-a-webpage-which-has-https

http://www.steves-internet-guide.com/mqtt-username-password-example/
