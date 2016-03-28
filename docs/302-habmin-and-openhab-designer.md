# GUI tools: HABmin and Designer

## HABmin

<http://www.instructables.com/id/openHAB-Admin-Console-HABmin-on-Raspberry-Pi/>

HABmin is a GUI interface for performing openHAB administrative tasks.
It can do all of this

• General configuration (openHAB.cfg)
• Configure bindings
• Configure items
• Configure mapping
• Configure sitemaps
• Configure ZWave network
• Configure rules and notifications
• Query and graph data from persistence stores
• View OSGi binding status
• View log files


Stop openHab, download and unzip HABmin

	sudo /etc/init.d/openhab stop
	cd /opt/openhab
	sudo wget https://github.com/cdjackson/HABmin/archive/master.zip
	sudo unzip master.zip
	sudo rm master.zip

You will need to make a file called habmin. This file should be located inside the "webapps" folder. If you are already in the openhab folder it should look like this:

	sudo mkdir webapps/habmin

relocate the contents of the HABmin-master folder to the webapps folder. Assuming you are in the openhab folder...

	sudo mv HABmin-master/* webapps/habmin/
	sudo rm -rf HABmin-master
	cd webapps/habmin

move the addons older in its proper location which should be /opt/openhab/addons		

	sudo mv addons/* ../../addons/
	sudo rm -rf addons

Start openHab

	sudo /etc/init.d/openhab start

Access the admin tool locally on the same machine running openHAB at

	http://localhost:8080/habmin/index.html


## Openhab Designer
I find it hard to change the items and sitemap files manually, because of the austere language used.

Download OpenHab Designer from here: <http://www.openhab.org/getting-started/downloads.html>

After I downloaded it on the RPi I could not get it to run. So I downloaded the Windows version, with the idea of editing on Windows and then download to the RPi.  After installation the GUI opened but had preciously few menu options. In fact, the thing was essentially dead and useless.

OpenHab Designer has, like most of OpenHab, very little documentation. I found this link, which helped a great deal:
<https://community.openhab.org/t/openhab-designer-dont-work/3125>

It turns out you must use the folder button to open the folder where the OpenHab config file is.
The OpenHab config file should be created like [this](http://www.openhab.org/getting-started/index.html):

"Within the `/opt/openhab` directory, there’ll be a folder called `configurations`. Within this folder create a copy of the default configuration file `openhab_default.cfg` and name it `openhab.cfg`. This is where you’ll store all your settings for openHAB and any bindings you need."

It turns out you need both the `openhab_default.cfg` and`openhab.cfg` files in this directory for the Designer to open.  Then OpenHab designer must be told where this is:
![openhab-designer-01.jpg](images/openhab-designer-01.jpg)

With a tip from [here](https://community.openhab.org/t/using-openhab-designer-on-windows-with-openhab-on-linux/4687) you can mount the remote RPi on you local windows system with [sftp-net-drive](https://www.eldos.com/sftp-net-drive/), and directly edit the files on RPi from Windows using the openHab Designer.

Once I got this going I was disappointed to learn that Designer mainly supports editing of rules, this what the [web site](https://github.com/openhab/openhab/wiki/Rules#ide-support) says, actually.
But after watching a video on YouTube, it is clear that I need to spend more time on this tool to understand its finer details.  The big help here is the content assist (Ctrl+Space) that provide context-sensitive completion capability - quite useful.

You can mount the openHab config folder on the PRi as a Windows folder and then use Designer on Windows (a lot easier than on the Pi)
<https://community.openhab.org/t/using-openhab-designer-on-windows-with-openhab-on-linux/4687/11>.
