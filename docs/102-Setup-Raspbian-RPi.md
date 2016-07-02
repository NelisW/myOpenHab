
# Prepare the RPi


## Installing the operating system

To follow

## Set up a fixed IP address for the Raspberry Pi

Set up the Raspberry Pi server to run on a fixed IP address. The fixed IP is necessary when the port forwarding is set up.




## Make a backup of your SD card

see at the end of 
<http://www.homeautomationforgeeks.com/raspberrypi_internet.shtml>



<http://forums.connectedly.com/guides-how-articles-f10/how-set-up-raspberry-pi-2626/>

Go to the setup page for your router. Everyone is a little different, but somewhere you can set the DHCP server to always assign the same IP address to a device based on its MAC address. 

## Updating Raspbian
https://www.raspberrypi.org/documentation/raspbian/updating.md

First, update your system's package list by entering the following command in LXTerminal or from the command line:

	sudo apt-get update

Next, upgrade all your installed packages to their latest versions with the command:

	sudo apt-get dist-upgrade

When running `sudo apt-get dist-upgrade`, it will show how much data will be downloaded and how much space it will take up on the SD card. It's worth checking with `df -h` that you have enough disk space free, as unfortunately `apt` will not do this for you. Also be aware that downloaded package files (`.deb` files) are kept in `/var/cache/apt/archives`. You can remove these in order to free up space with `sudo apt-get clean`.

