#my.openHAB

<https://my.openhab.org/docs>

##register on my.openHAB

For this purpose you will need your local openHAB UUID and secret key.
These two numbers are located in the `secret` and `uuid` files in ([see here](https://my.openhab.org/docs))

	/opt/openhab/webapps/static
	
##	Download the my.openHAB bundle 

First see if you don't already have an `org.openhab.io.myopenhab-1.x.x.jar` file in `/opt/openhab/addons/`. If you don't have the file  download the latest version from 
<https://my.openhab.org/docs>.  I had the 1.7.1 version already in the addons directory.

## Adjust security settings

Edit openhab.cfg
	
	sudo nano /opt/openhab/configurations/openhab.cfg

and set the following:

- `security:option=EXTERNAL` 
- `security:netmask=` to your local LAN IP subnet, i.e., `255.255.255.0/24`
- `servicediscovery:bind_address= to your local (RPi) IP address

After editing restart the daemon to note the new config settings:

		sudo /etc/init.d/openhab restart

##Set up the Android app

http://www.homeautomationforgeeks.com/openhab_android.shtml

1. Install the app from Google Play

2. Go to Settings and disable the demo mode

3. Deselect the demo mode, you want to use your own site.

3. Set `openHAB URL` to your local network url:  `http://192.168.1.80:8080/` using the http protocal, port 8080. Use the http protocol and don't add anything beyond the port number.

4. Set the `openHAB Remote URL`  to `https://my.openhab.org`

5. Use the same username and password that you registered with on myopenHAB.

6. Select the `Ignore SSL certificate` must have the tick mark.

6. Deselect the `Ignore SSL hostname` must not have the tick mark.

7. Escape back to the app's main window.  

##Notes

After setting up the openHAB and my.openHAB you have to wait some time before the app seems to work.




