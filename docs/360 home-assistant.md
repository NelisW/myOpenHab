# Home Assistant

##  Pi All-in-One Installer

The Raspberry Pi All-In-One Installer deploys a complete Home Assistant server including support for MQTT with websockets, Z-Wave, and the Open-Zwave Control Panel.

### Installing on a fresh Raspbian

The only requirement is that you have a Raspberry Pi with a fresh installation  of Raspbian (with SSH enabled!) connected to your network.  Download Raspbian from [here](https://www.raspberrypi.org/downloads/raspbian/).  Raspbian PIXEL is a full system with a nice GUI desktop and lots of (unwanted? content, such as Wolfram).  Raspbian Lite  is headless (no keyboard, display etc). Flash the Raspbian image to an SD card (at least 8 GB, preferably 16 GB).  Note that as of 2016-11-30 SSH is disabled by default in the official Raspbian images. It seems that you **must enable SSH** for the installation to proceed.  Adding an empty file called `ssh` to `/boot/` or the FAT32 partition will enable it. More information is on the [Raspberry Pi Foundation Blog](https://www.raspberrypi.org/blog/page/2/?fish#a-security-update-for-raspbian-pixel)

Login to Raspberry Pi. Remotely with `ssh pi@your_raspberry_pi_ip` or on the raspi itself.  Follow the procedure described [here](https://home-assistant.io/docs/installation/raspberry-pi-all-in-one/),  [here](https://github.com/home-assistant/fabric-home-assistant), and [here](https://www.youtube.com/watch?v=VGl3KTrYo6s). Run the following command:

    curl -O https://raw.githubusercontent.com/home-assistant/fabric-home-assistant/master/hass_rpi_installer.sh && sudo chown pi:pi hass_rpi_installer.sh && bash hass_rpi_installer.sh

Note
- This command is one line and not run as sudo
-  By default, installation makes use of a Python Virtualenv. If you wish to not follow this recommendation, you may add the flag `-n` to the end of the install command specified above.

Installation will take approx. 1-2 hours depending on the Raspberry Pi model the installer is being run against.   Once rebooted, your Raspberry Pi will be up and running with Home Assistant. You can access it at `http://your_raspberry_pi_ip:8123`.

The Home Assistant configuration files are located at `/home/homeassistant/.homeassistant`. The virtual environment with the Home Assistant installation is located at `/srv/homeassistant/homeassistant_venv`. As part of the secure installation, a new user, named `homeassistant`, is created to run Home Assistant. This is a system account and does not have login or other abilities by design.

## Managing HA runs via systemd

If all went well, HA should start at boot using the systemd daemon.

You can control the HA daemon with the following commands

    sudo systemctl stop home-assistant.service
    sudo systemctl start home-assistant.service
    sudo systemctl restart home-assistant.service
    sudo systemctl enable home-assistant.service
    sudo systemctl disable home-assistant.service

The home-assistant.service file is present here `/etc/systemd/system/home-assistant.service`, with a symbolic link to this file here `/etc/systemd/system/multi-user.target.wants/home-assistant.service`. The file has this contents:

    [Unit]
    Description=Home Assistant
    After=network.target

    [Service]
    Type=simple
    User=homeassistant
    ExecStart=/srv/homeassistant/homeassistant_venv/bin/hass -c "/home/homeassistant/.homeassistant"

    [Install]
    WantedBy=multi-user.target

If you edit this file, you need to reload systemd to make the daemon aware of the new configuration.

    sudo systemctl --system daemon-reload

### Starting HA manually

To start the server manually, first stop the daemon version. Then activate the home assistant virtual environment and run hass in the environment:

    source /srv/homeassistant/homeassistant_venv/bin/activate
    hass


## Home Assistant Configuration

You configure your HA installation by editing the `configuration.yaml` file. To edit the file as user `pi` you must edit the file with  `sudo` for elevated rights to edit the file.  I prefer to use the geany editor, which must be invoked by `gksudo geany &`  to set up the graphical environment first (see  [here](https://linux.die.net/man/1/gksudo)).

Start by adding the information as shown [here](https://home-assistant.io/docs/configuration/basic/), changing the details as necessary for your installation.


https://home-assistant.io/components/group/
https://home-assistant.io/components/scene/
https://home-assistant.io/components/zone/


### Multi-file configuration

https://home-assistant.io/getting-started/configuration/  
https://home-assistant.io/docs/configuration/  
https://home-assistant.io/docs/configuration/yaml/  
http://www.yaml.org/spec/1.2/spec.html  
https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html  
https://home-assistant.io/docs/configuration/splitting_configuration/  
https://home-assistant.io/docs/configuration/secrets/  
https://home-assistant.io/docs/configuration/troubleshooting/

At some point all the information in the yaml config file becomes just too much.
The configuration details can be split over many files all, to be `!include`d in
the main configuration file.  I split the details between different files for 
sensors, switches, groups, customization, etc. - but only one file each. A different
strategy might create files per device, another strategy could use subdirectories, 
and so on.

Here are my key observations so far:

- yaml is indent sensitive so be careful with the spaces.
- the `customize` keyword must fall under the main `homeassistant` keyword.
- some keywords such as `sensor` or `switch` can appear only once in the entire set of files. So
  group items together under one heading, either in included files the heading.
- use the `!secret` keyword to keep al the sensitive information in one file (and protect it well).
- the naming convention is quite weird and requires special care, see below


Naming convention:  I am still figuring this out. Variants of the same name will be used
in different places with underscores removed and capitalisation to lower case, but these
are all the same name.


### Sensors and Switches

See here:  
https://github.com/NelisW/myOpenHab/blob/master/docs/361%20home-assistant-sensors.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/362%20home-assistant-switches.md  


### MQTT

https://home-assistant.io/docs/mqtt/broker/  
https://home-assistant.io/components/mqtt/  

I make extensive use of MQTT in my ESP8266-based sensors and switches. For more detail see here:  
https://github.com/NelisW/myOpenHab/blob/master/docs/201-mqtt-install-mosquitto.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/202-mqtt-tips.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/204-mqtt-c.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/205-mqttwarn.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/206-mqtt-python.md  
https://github.com/NelisW/myOpenHab/blob/master/docs/206-mqtt-python.md  



### Customise 

detail to follow.

https://materialdesignicons.com/ 






