
#HABmin
 
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
	
