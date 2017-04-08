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

### Managing HA runs via systemd

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


### Editing the configuration file

You configure your HA installation by editing the `configuration.yaml` file. To edit the file as user `pi` you must edit the file with  `sudo` for elevated rights to edit the file.  I prefer to use the geany editor, which must be invoked by `gksudo geany &`  to set up the graphical environment first (see  [here](https://linux.die.net/man/1/gksudo)).

### Material icons

https://materialdesignicons.com/ 


Start by adding the information as shown [here](https://home-assistant.io/docs/configuration/basic/), changing the details as necessary for your installation.

## System monitor

https://home-assistant.io/components/sensor.systemmonitor/

    # Example configuration.yaml entry
    sensor:
    - platform: systemmonitor
        resources:
        - type: disk_use
            arg: /
        - type: disk_free
            arg: /
        - type: memory_use_percent
        - type: last_boot
        - type: since_last_boot

## Sonoff

https://community.home-assistant.io/t/sonoff-homeassistant-alternative-firmware-for-sonoff-switches-for-use-with-mqtt-ha/2332
https://github.com/KmanOz/Sonoff-HomeAssistant
https://home-assistant.io/components/switch.mqtt/

https://alienlabs.eu/2016/09/19/sonoff-mqtt-and-home-assistant/
https://www.hawker.id.au/index.php/2017/01/17/home-assistant-sonoff-mqtt/
http://www.cnx-software.com/2017/02/27/karls-home-automation-project-part-1-home-assistant-yaml-mqtt-sonoff-and-xmas-lights/
https://community.home-assistant.io/t/sonoff-homeassistant-alternative-firmware-for-sonoff-switches-for-use-with-mqtt-ha/2332/83


https://esp8266hints.wordpress.com/2016/04/10/using-theo-arends-sonoffmqtt-package-tasmota/
https://esp8266hints.wordpress.com/2016/05/01/using-tasmota-part-2-mqtt/
https://esp8266hints.wordpress.com/2017/02/18/how-to-do-a-sonoff-memory-upgrade/
https://esp8266hints.wordpress.com/2017/03/09/nice-little-tft-screen-adapter-board/


Homie:
https://github.com/marvinroger/homie-esp8266


## Efergy engergy measurement

https://home-assistant.io/components/sensor.efergy/
https://community.home-assistant.io/t/efergy-switch-in-hass/6958/11
http://napi.hbcontent.com/document/index.php

The utc_offset parameter is  in minutes, and the negative of what you'd think (this is from the API. For example, my timezone is UTC-5:00, so my utc_offset is 300.
The utc_offset parameter is only used for the daily cost.

    # Example configuration.yaml entry
    sensor:
    - platform: efergy
        app_token: hk0IIuOsH-n_vWo4bFTCw8mDGHr6oBKJ
        utc_offset: -120
        monitored_variables:
        - type: instant_readings
        - type: amount
            period: day


  customize:
    sensor.energy_budget:
       icon: mdi:power-plug
    sensor.energy_cost:
       icon: mdi:power-plug
    sensor.energy_usage:
       icon: mdi:power-plug
    sensor.energy_consumed:
       friendly_name: 'Daily Usage'
       icon: mdi:power-plug



    # Example configuration.yaml entry
    sensor:
    - platform: efergy
        app_token: APP_TOKEN
        utc_offset: -120
        monitored_variables:
        - type: instant_readings
        - type: budget
        - type: cost
            period: day
            currency: $
        - type: amount
            period: day

 





----------------------------
--------------------------------------------------
-------------------------------------------------------------

https://home-assistant.io/components/sensor.efergy/

https://home-assistant.io/components/sensor.pvoutput/

https://home-assistant.io/components/sensor.wunderground/

https://home-assistant.io/components/sensor.emoncms/
https://home-assistant.io/components/emoncms_history/

https://home-assistant.io/components/camera.rpi_camera/

https://home-assistant.io/components/camera.generic/

https://home-assistant.io/components/sensor.fitbit/

https://home-assistant.io/components/octoprint/
https://home-assistant.io/components/sensor.octoprint/

https://home-assistant.io/components/notify.pushover/

https://home-assistant.io/components/device_tracker.netgear/


https://home-assistant.io/components/mqtt/
https://home-assistant.io/components/notify.mqtt/
https://home-assistant.io/components/alarm_control_panel.mqtt/
https://home-assistant.io/components/binary_sensor.mqtt/

https://home-assistant.io/components/switch.mqtt/
https://home-assistant.io/components/sensor.mqtt/


https://home-assistant.io/components/switch.rest/
https://home-assistant.io/components/sensor.rest/
https://home-assistant.io/components/rest_command/
https://home-assistant.io/components/binary_sensor.rest/
https://home-assistant.io/components/switch.arest/
https://arest.io/about




https://home-assistant.io/components/group/
https://home-assistant.io/components/scene/
https://home-assistant.io/components/zone/


--------------------------------------------------------

https://home-assistant.io/blog/2016/07/28/esp8266-and-micropython-part1/

## Nextion

http://tech.scargill.net/coding-the-nextion/
http://openhardware.gridshield.net/home/nextion-lcd-getting-started-for-arduino
https://www.itead.cc/wiki/Nextion_Editor_Quick_Start_Guide
http://support.iteadstudio.com/support/discussions/topics/1000065323

