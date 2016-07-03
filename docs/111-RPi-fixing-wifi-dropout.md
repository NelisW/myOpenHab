# Fixing wifi dropout on the RPi

When the ADSL wifi drops out some services on the Raspberry Pi do not restart (e.g., myopenHAB).

Following the weworkweplay page listed below do the following to reboot the RPi when the wifi falls away.

Store this script in `/usr/local/bin/checkwifi.sh`.

	ping -c4 192.168.1.1 > /dev/null
	 
	if [ $? != 0 ] 
	then
	  sudo /sbin/shutdown -r now
	fi

Change the IP on the first line to the IP of your router or something like `www.google.com`, or some other device on your network that you can assume will be always online.

Make sure the script has the correct permissions to run

	sudo chmod 775 /usr/local/bin/checkwifi.sh

SSH into the Raspberry Pi and open up the crontab editor by typing `crontab -e`. 
Add the following line:

	*/5 * * * * /usr/bin/sudo -H /usr/local/bin/checkwifi.sh >> /dev/null 2>&1

This runs the script we wrote every 5 minutes as sudo (so you have permission to do the shutdown command), writing its output to /dev/null so it won't clog your syslog. 
Exit the crontab editor, reboot your Raspberry Pi and from now on it'll reboot when it drops connection.

If a reboot is somewhat excessive, you can also try to just restart the wireless connection:

	ping -c4 192.168.1.1 > /dev/null
	 
	if [ $? != 0 ] 
	then
	  echo "No network connection, restarting wlan0"
	  /sbin/ifdown 'wlan0'
	  sleep 5
	  /sbin/ifup --force 'wlan0'
	fi

## Python solutions
https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=54001

    import subprocess
    WLAN_check_flg = False

    def WLAN_check():
        '''
        This function checks if the WLAN is still up by pinging the router.
        If there is no return, we'll reset the WLAN connection.
        If the resetting of the WLAN does not work, we need to reset the Pi.

        '''

        ping_ret = subprocess.call(['ping -c 2 -w 1 -q 192.168.1.1 |grep "1 received" > /dev/null 2> /dev/null'], shell=True)
        if ping_ret:
            # we lost the WLAN connection.
            # did we try a recovery already?
            if WLAN_check_flg:
                # we have a serious problem and need to reboot the Pi to recover the WLAN connection
                subprocess.call(['logger "WLAN Down, Pi is forcing a reboot"'], shell=True)
                WLAN_check_flg = False
                subprocess.call(['sudo reboot'], shell=True)
            else:
                # try to recover the connection by resetting the LAN
                subprocess.call(['logger "WLAN is down, Pi is resetting WLAN connection"'], shell=True)
                WLAN_check_flg = True # try to recover
                subprocess.call(['sudo /sbin/ifdown wlan0 && sleep 10 && sudo /sbin/ifup --force wlan0'], shell=True)
        else:
            WLAN_check_flg = False


## Reference

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/test-and-configure# fixing-wifi-dropout-issues

http://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/

https://raspberrypispot.wordpress.com/2013/07/08/wifi-and-ethernet-dropout-problems-in-raspberry-pi/

http://root42.blogspot.co.za/2013/03/how-to-make-raspberry-pi-automatically.html

http://raspberrypi.stackexchange.com/questions/4120/how-to-automatically-reconnect-wifi

https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=54001