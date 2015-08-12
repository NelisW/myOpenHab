#Setting up the Raspberry Pi Remote Access

If the RPi is on a network it is very convenient to gain access from another PC.  There are several available options, ranging from simple terminal access to X11 graphical interface access.  The [Mobaxterm](http://mobaxterm.mobatek.net/download.html) software provides a variety of means to access your RPi remotely.

##Terminal access

To follow


## Setting up to work with X11 forwarding using SSH on Mobaxterm

<http://blogspot.tenettech.com/?p=2850>  
<http://en.tldp.org/HOWTO/XDMCP-HOWTO/ssh.html>  

The X windowing system comprises a server and a client with messages travelling between the two.  In this case the server is running on the RPi and the client is run on a remote PC.  The client understands the X11 commands and renders these on the screen.  The user interaction is then captured on the PC and sent back to the server on the RPi.

X11 server-client communication is insecure - SSH forwarding can be used to secure the channel. This is called 'X11 Forwarding using SSH'.  

Download and install Mobaxterm <http://mobaxterm.mobatek.net/download.html>

1. Start Mobaxterm
2. Start a new `Session` (click on icon on the left).  
1. Click on SSH 
1. Add the remote host IP address (e.g., 10.0.0.16)
3. Click on `Advanced SSH settings`
4. In the `Remote environment` dropdown select the `LDXE` desktop and click `OK`.
5. It will prompt you to enter the RPi username and password.
6. If the login is successful you should see the X11 screen.

## Setting up to work with VNC server

VNC is virtual network computing, where the server transmits the pre-rendered screen contents to the client, and the client responds back by sending keyboard and mouse events. VNC differs from X11 in the sense that X11 sends low level commands to the client to render the screen in the client.  VNC sends the pre-rendered image.

<http://searchnetworking.techtarget.com/definition/virtual-network-computing>  
<http://www.instructables.com/id/Setting-up-a-VNC-Server-on-your-Raspberry-Pi>  
<https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/installing-vnc>  
<https://learn.adafruit.com/adafruit-raspberry-pi-lesson-7-remote-control-with-vnc/using-a-vnc-client>

Installing a VNC Server on your Raspberry Pi

    sudo apt-get update
    sudo apt-get install tightvncserver
	vncserver :1

or to set the resolution use

	vncserver :1 -geometry 1920x1080 -depth 24

Remember the passwords (8 chars long max)

You can also make a shell script to start the server

	cd /home/pi
	geany vnc.sh

and enter the text

	#!/bin/sh
	vncserver :0 -geometry 1920x1080 -depth 24 -dpi 96

Make the file executable:

	chmod +x vnc.sh

Then you can run it at any time with:

	./vnc.sh


Set up the client by determining the IP address of the Raspberry Pi

	sudo ifconfig

Look for the IP address on the wlanx line next to inet addr: something like `10.0.0.16` or similar.

When you enter the ip address on a vncviewer, you have to enter the server and screen number. 
For example 192.xxx.x.x and then enter :1 or :2 etc. to indicate the screen number. 

##Set up the RPi to start the VNC server on boot-up

	sudo raspi-config

Select `Enable boot to Desktop` then select `Desktop` select `Finish` or  Escape to return to the terminal prompt.

Set up the RPi to boot to the graphical user interface:

	cd /home/pi
	cd .config
	sudo mkdir autostart
	cd autostart
	sudo geany tightvnc.desktop (or sudo nano tightvnc.desktop)

enter the following into the file

	[Desktop Entry]
	Type=Application
	Name=TightVNC
	Exec=vncserver :1
	StartupNotify=false

Save the file. Next time the RPi boots up it will start the VNC server.

An alternative approach is as follows:

	sudo su
	cd /etc/init.d/

Create a new file `vncboot` with the following script:

	### BEGIN INIT INFO
	# Provides: vncboot
	# Required-Start: $remote_fs $syslog
	# Required-Stop: $remote_fs $syslog
	# Default-Start: 2 3 4 5
	# Default-Stop: 0 1 6
	# Short-Description: Start VNC Server at boot time
	# Description: Start VNC Server at boot time.
	### END INIT INFO
	
	#! /bin/sh
	# /etc/init.d/vncboot
	
	USER=pi
	HOME=/home/pi
	
	export USER HOME
	
	case "$1" in
	 start)
	  echo "Starting VNC Server"
	  #Insert your favoured settings for a VNC session
	  su - pi -c "/usr/bin/vncserver :0 -geometry 1280x800 -depth 16 -pixelformat rgb565"
	  ;;
	
	 stop)
	  echo "Stopping VNC Server"
	  /usr/bin/vncserver -kill :0
	  ;;
	
	 *)
	  echo "Usage: /etc/init.d/vncboot {start|stop}"
	  exit 1
	  ;;
	esac
	
	exit 0

Make the file executable

	chmod 755 vncboot

Enable dependency-based boot sequencing:

	update-rc.d /etc/init.d/vncboot defaults

If enabling dependency-based boot sequencing was successful, you will see this:

	update-rc.d: using dependency based boot sequencing

But if you see this:

	update-rc.d: error: unable to read /etc/init.d//etc/init.d/vncboot

then try the following command:

	update-rc.d vncboot defaults

Reboot your Raspberry Pi and you should find a VNC server already started.






