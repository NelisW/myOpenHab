
# Prepare the RPi


## Installing the operating system

To follow

## Updating Raspbian
https://www.raspberrypi.org/documentation/raspbian/updating.md

First, update your system's package list by entering the following command in LXTerminal or from the command line:

	sudo apt-get update

Next, upgrade all your installed packages to their latest versions with the command:

	sudo apt-get dist-upgrade

When running `sudo apt-get dist-upgrade`, it will show how much data will be downloaded and how much space it will take up on the SD card. It's worth checking with `df -h` that you have enough disk space free, as unfortunately `apt` will not do this for you. Also be aware that downloaded package files (`.deb` files) are kept in `/var/cache/apt/archives`. You can remove these in order to free up space with `sudo apt-get clean`.



## Set up a fixed IP address for the Raspberry Pi

Set up the Raspberry Pi server to run on a fixed IP address. The fixed IP is necessary when the port forwarding is set up.  The fixed IP address can be setup by setting the router to do so, or by setting the computer itsel to do so.  Both should work equally well.

The router normally sets up all the IP addresses in the LAN automatically by DHCP.  It is possible to use the router to allocated fixed IP address to specific computers on the wifi LAN.

1.  In the NetGear router configuration webserver, go to the `LAN Setup` page. It should show the router's own IP address and indicate that the router uses DHCP. Further down the page there should be list of fixed IP address computers. 
2.  Add new computers by clicking on `Add`.  A new page opens up and show all the computers on the network, with their current IP addresses. Below the table in the edit fields, enter the MAC address, required IP address and a text name for the computer that must get a fixed IP address. Click on `Add` when al fields are filled in.  The next time the computer connects to the router, the router will allocate the fixed IP address to the computer.


Here are instructions on how to do the fixed IP setup in the Raspberry Pi (I used the router to set mine):  
http://raspberrypi.stackexchange.com/questions/6757/how-to-use-ssh-out-of-home-network  
http://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address  

## Make a backup of your SD card

see at the end of 
<http://www.homeautomationforgeeks.com/raspberrypi_internet.shtml>


<http://forums.connectedly.com/guides-how-articles-f10/how-set-up-raspberry-pi-2626/>

Go to the setup page for your router. Everyone is a little different, but somewhere you can set the DHCP server to always assign the same IP address to a device based on its MAC address. 

