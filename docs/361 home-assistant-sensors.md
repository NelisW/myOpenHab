# Home Assistant Sensors

## Command line 

https://home-assistant.io/components/sensor.command_line/

The command line component provides the ability to execute any task on the host and then use the return value. There are several applications where this component can be used. For example, to read the CPU temperature use this sensor:

    sensor:
    - platform: command_line
        name: CPU Temperature
        command: "cat /sys/class/thermal/thermal_zone0/temp"
        unit_of_measurement: "°C"
        value_template: '{{ value | multiply(0.001) }}'




## System monitor

https://home-assistant.io/components/sensor.systemmonitor/

To monitor the state of my Raspberry Pi host I use the following:

in sensors.yaml

    # raspberry pi system monitor
    - platform: command_line
    name: CPU Temp
    command: "/bin/cat /sys/class/thermal/thermal_zone0/temp"
    unit_of_measurement: "ºC"
    value_template: '{{ value | multiply(0.001) }}'

    - platform: systemmonitor
    resources:
    - type: disk_use_percent
        arg: /
    - type: memory_free
    - type: memory_use_percent
    - type: processor_use
    - type: since_last_boot

in groups.yaml

    host_view:
    view: yes
    name: Host
    entities:
        - group.host_grp

    host_grp:
    name: Host
    entities:
        - sensor.cpu_use
        - sensor.cpu_temp
        - sensor.disk_use_
        - sensor.ram_free
        - sensor.ram_use_percent
        - sensor.since_last_boot

https://community.home-assistant.io/t/monitor-remote-pi-cpu-temp/12640


## Efergy energy measurement

https://home-assistant.io/components/sensor.efergy/
https://community.home-assistant.io/t/efergy-switch-in-hass/6958/11
http://napi.hbcontent.com/document/index.php

The utc_offset parameter is  in minutes, and the negative of what you'd think (this is from the API. For example, my timezone is UTC-5:00, so my utc_offset is 300.
The utc_offset parameter is only used for the daily cost.

In sensors.yaml  

    sensor:
    - platform: efergy
        app_token: !secret efergy_token
        utc_offset: -120
        monitored_variables:
        - type: current_values
        - type: amount
            period: day

In groups.yaml

    # solar energy group
    solar_energy_grp:
    name: Solar Energy Status
    entities:
        - sensor.energy_consumed
        - sensor.efergy_<your number here>

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

 
## More sensors

See my configuration files here:  
https://github.com/NelisW/myHome-Assistant-Config  



## Sensor Components

There are a great many number of sensors defined here:  
https://home-assistant.io/components/

These ones piqued my interest:  
- https://home-assistant.io/components/sensor.efergy/
- https://home-assistant.io/components/sensor.pvoutput/
- https://home-assistant.io/components/sensor.wunderground/
- https://home-assistant.io/components/sensor.emoncms/
- https://home-assistant.io/components/emoncms_history/
- https://home-assistant.io/components/camera.rpi_camera/
- https://home-assistant.io/components/camera.generic/
- https://home-assistant.io/components/sensor.fitbit/
- https://home-assistant.io/components/octoprint/
- https://home-assistant.io/components/sensor.octoprint/
- https://home-assistant.io/components/notify.pushover/
- https://home-assistant.io/components/device_tracker.netgear/
- https://home-assistant.io/components/mqtt/
- https://home-assistant.io/components/notify.mqtt/
- https://home-assistant.io/components/alarm_control_panel.mqtt/
- https://home-assistant.io/components/binary_sensor.mqtt/
- https://home-assistant.io/components/switch.mqtt/
- https://home-assistant.io/components/sensor.mqtt/
- https://home-assistant.io/components/switch.rest/
- https://home-assistant.io/components/sensor.rest/
- https://home-assistant.io/components/rest_command/
- https://home-assistant.io/components/binary_sensor.rest/
- https://home-assistant.io/components/switch.arest/
- https://arest.io/about

## Nextion

I have one on order....

http://tech.scargill.net/coding-the-nextion/
http://openhardware.gridshield.net/home/nextion-lcd-getting-started-for-arduino
https://www.itead.cc/wiki/Nextion_Editor_Quick_Start_Guide
http://support.iteadstudio.com/support/discussions/topics/1000065323


## MicroPython for Home Assistant

https://home-assistant.io/blog/2016/07/28/esp8266-and-micropython-part1/
https://home-assistant.io/blog/2016/08/31/esp8266-and-micropython-part2/
https://github.com/davea/sonoff-mqtt

## Homie  

https://github.com/marvinroger/homie-esp8266

