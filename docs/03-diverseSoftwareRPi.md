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

	

[raspberry-pi-email-server-part-1-postfix](https://samhobbs.co.uk/2013/12/raspberry-pi-email-server-part-1-postfix)  
[raspberry-pi-email-server-part-2-dovecot](https://samhobbs.co.uk/2013/12/raspberry-pi-email-server-part-2-dovecot)  

[send email on startup](https://gist.github.com/johnantoni/8199088)  
[How to set up smtp and send emails?](http://raspberrypi.stackexchange.com/questions/12405/how-to-set-up-smtp-and-send-emails)  
[Easily connect Raspberry Pi to Gmail, Facebook, Twitter ](http://mitchtech.net/connect-raspberry-pi-to-gmail-facebook-twitter-more/)  
[sending email from the command line](https://www.raspberrypi.org/forums/viewtopic.php?f=36&t=32077)  
[Prepare Your Pi To Send Mail Through Gmail](http://www.sbprojects.com/projects/raspberrypi/exim4.php)  


--------------------------------------------
#Set up mail

[Prepare Your Pi To Send Mail Through Gmail](http://www.sbprojects.com/projects/raspberrypi/exim4.php)  

Install ssmtp

	sudo apt-get install ssmtp mailutils mpack

Now edit the file `/etc/ssmtp/ssmtp.conf` as root 

	sudo nano /etc/ssmtp/ssmtp.conf

and add the next lines. Please note that some of the lines already exist and may need to be changed. Others don't exist yet and need to be added to the end of the file.

	mailhub=smtp.gmail.com:587
	hostname=ENTER YOUR RPI'S HOST NAME HERE
	AuthUser=YOU@gmail.com
	AuthPass=PASSWORD
	useSTARTTLS=YES

you'll have to replace YOU with your gmail login name and PASSWORD with your (application specific) gmail password. 
After this you're done. You don't even have to restart the SSMTP server (in fact, there is none).

Some processes, for instance crontabs, can send mails to root or other system users. If you don't want to miss any of them you can setup some aliases. You can do that by editing the file /etc/aliases. 

	sudo nano /etc/aliases

Here's an example of its contents:

	# /etc/aliases
	mailer-daemon: postmaster
	postmaster: root
	nobody: root
	hostmaster: root
	usenet: root
	news: root
	webmaster: root
	www: root
	ftp: root
	abuse: root
	noc: root
	security: root
	root: pi
	pi: youremail@example.com

This tells the system to redirect all mail to root, while mail to root is redirected to the user pi, while mail to user pi is finally redirected to my own mail account. This way all system mail will eventually be sent to my own mail account, no matter to what local user the mail was originally sent.

The next command will setup a new full name (pi @ domotics) for the user name pi, with which you can identify the source of the e-mail.

	sudo chfn -f "pi @ domotics" pi


--------------------------------------------
#Set up mail

[Prepare Your Pi To Send Mail Through Gmail](http://www.sbprojects.com/projects/raspberrypi/exim4.php)  

Install Exim4

	sudo apt-get install exim4

After installing exim4 we need to configure it. This is done by the following command:

	sudo dpkg-reconfigure exim4-config

A series of questions are asked - refer to the web site above for the answers.

If you get this message:

	IPv6 socket creation failed: Address family not supported by protocol

Short detour:
	
http://www.geeklee.co.uk/basic-exim-mta-relay-on-raspberry-pi-with-raspbian/

I had to perform the following:

Edit the file /etc/exim4/update-exim4.conf.conf (e.g. with nano)

	sudo nano /etc/exim4/update-exim4.conf.conf
	
Remove ::1 from dc_local_interfaces section. Save and exit. Delete the paniclog:

	sudo rm /var/log/exim4/paniclog

Reconfigure Exim:

	sudo update-exim4.conf
	
Restart Exim service:

	sudo service exim4 restart

Return to main theme:

Now you'll have to enter your account details. As root, edit the file

	sudo nano /etc/exim4/passwd.client 
 
and add the next three lines at the end of the file.

gmail-smtp.l.google.com:YOU@gmail.com:PASSWORD
*.google.com:YOU@gmail.com:PASSWORD
smtp.gmail.com:YOU@gmail.com:PASSWORD

Needless to say that you'll have to change YOU to your Gmail login name, and PASSWORD to your password on all three lines. After that you only have to update and restart exim4 and you're done! The next two lines will do that for you:

	sudo update-exim4.conf
	sudo /etc/init.d/exim4 restart


