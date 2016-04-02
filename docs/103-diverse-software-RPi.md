# Setting up diverse software tools

## Install browsers

	sudo apt-get install chromium

## Change the RPi hostname

<http://www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/>

## General advice

[Tutorial – Prepare your Raspberry Pi to become a web server](http://www.raspipress.com/2012/09/tutorial-prepare-your-raspberry-pi-to-become-a-web-server/)  
[How set up a secure Raspberry Pi server installation](https://www.pestmeester.nl/)

## General software

The full home automation requires quite a list of software to be installed - details are interspersed throughout the set of documentation files.  Software not listed elsewhere are as follows:

- geany editor
- vim editor (nano is actually quite useful - easier than vim)
- chromium browser
- tofrodos (sometimes convert files between Windows and Linux line-endings)
- dos2unix (sometimes convert files between Windows and Linux line-endings)

## Install samba

To access files on your RPi directory from Windows.

<http://www.homeautomationforgeeks.com/samba.shtml>

	sudo apt-get install samba samba-common-bin
	sudo nano /etc/samba/smb.conf

Set a password (the same password as when logging in as pi):

	sudo smbpasswd -a pi

Add the requisite directories with appropriate rights to the samba config file 	
	[OpenHAB]
	comment = OpenHAB
	path = /opt/openhab
	browseable = Yes
	writeable = Yes
	only guest = no
	create mask = 0777
	directory mask = 0777
	public = no
	force user = root


Open the folder in Windows Explorer as `\\yourRPiIPaddress\sambamount`  
For example, if your RPi IP address is `10.0.0.5`, open Windows Explorer and then type `\\10.0.0.5\OpenHab`, or just `\\10.0.0.5` to see all the samba folders.


## Install pip

pip is not installed by default on RPi.

	wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
	sudo python get-pip.py


## git-crypt

If you want to save your files in a git repository and want to protect some files (e.g., password files, etc) consider 	(git-crypt)[<https://www.agwa.name/projects/git-crypt/] <https://github.com/AGWA/git-crypt>

## node-js

<http://randomnerdtutorials.com/how-to-install-the-latest-version-of-node-js-in-raspberry-pi/> not yet installed.

## Shutdown button

You can set up a switch to the GPIO pins which can be used to shutdown the RPi orderly if you don't have a keyboard and screen.  See here: https://github.com/lucsmall/Raspberry-Pi-Shutdown-Button.
