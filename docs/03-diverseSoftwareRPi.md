to follow

	sudo apt-get install chromium
	
	
http://www.raspipress.com/2012/09/tutorial-prepare-your-raspberry-pi-to-become-a-web-server/

##Install pip

pip is not installed by default on RPi.

	wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
	sudo python get-pip.py

##Install mail sending capability

<http://iqjar.com/jar/sending-emails-from-the-raspberry-pi/>  
<http://raspberrypi.stackexchange.com/questions/8180/raspberry-pi-as-an-email-server>  
<https://help.ubuntu.com/community/MailServer>


<http://www.raspipress.com/2012/09/tutorial-install-postfix-to-allow-outgoing-email-on-raspberry-pi/>

Install and set up Postfix:

	sudo apt-get update
	sudo apt-get install postfix
	
Follow the instructions in the install and on the website.

	

https://samhobbs.co.uk/2013/12/raspberry-pi-email-server-part-1-postfix
https://samhobbs.co.uk/2013/12/raspberry-pi-email-server-part-2-dovecot

