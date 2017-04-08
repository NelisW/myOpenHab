# Access via weaved

[Weaved](https://www.weaved.com) is a powerful cloud for IoT devices. It has an API and support for Raspberry Pi for web access and an iOS push notification app (it seems there is no Android app as yet).  <http://www.weaved.com/in-action/weaved-iot-kit>

Ypi can access the cloud service via SSH (port 22), via HTTP (port 80), via VNC (port 5901) or you can even write your own TCP service.

## Installing

Create an account on weaved.

https://developer.weaved.com/portal/members/betapi.php

https://developer.weaved.com/portal/login.php

On your RPi install the weaved software

    wget https://github.com/weaved/installer/raw/master/binaries/weaved-nixinstaller_1.2.13.bin
    chmod +x weaved-nixinstaller_1.2.13.bin
    ./weaved-nixinstaller_1.2.13.bin

Depending on the services you want select the `weavedssh22` service and/or select the `web` option. Use names that you can identify the type of service.  You can install more than one service.

## Using weaved

https://developer.weaved.com/portal/login.php

### SSH
You can access the RPi on SSH via a web browser or an Android app. There are many to choose from (I played with ConnectBot and JuiceSSH, but there are many more).

Login to https://developer.weaved.com/portal/login.php and select the SSH service to get an IP address:port combination that you can copy and paste to your SSH client to connect. When prompted for a password, use your RPi login user password to authenticate.



### Web (http) on port 80

This option is pre-configured for port 80, but don’t worry, all Weaved based connections are secure even if not using SSL. The free iOS app also includes a built in web browser, so you can use that to connect as well.


# Access via SSH

Change the port so some other lesser used port.
You need to change /etc/ssh/sshd_config which is the config file for the ssh server, not /etc/ssh_config which is the client config. Then restart ssh.

