#supervisord

`supervisor` is a service system that allows its users to monitor and control a number of processes on UNIX-like operating systems. Supervisor launches programs, monitors them for failure, logs their output, and restarts them. 

`supervisor` is an ideal way to start Python scripts and other processes to run as service-type applications.  We are using this tool to start numerous scripts and apps in the home automation project.  Examples of these scripts are mqttwarn.py and mqttPubDS18B20.py.


##Install supervisord

<http://jpmens.net/2014/02/13/in-my-toolbox-supervisord/>  
<http://supervisord.org/>

###Installing supervisor

<https://serversforhackers.com/monitoring-processes-with-supervisord>

To install Supervisord, we can simply run the following:

	sudo apt-get install -y supervisor

Installing it as a package gives us the ability to treat it as a service:

	sudo service supervisor start
	
The configuration file is here

	sudo nano /etc/supervisor/supervisord.conf

In order to control supervisor as a regular user, at the top of the file add the chown line underneath the chmod line:

	chmod=0700                  ; socket file mode (default 0700)
	chown=pi:pi                 ; socket file uid:gid owner
	
Towards the bottom of this file is written

	[include]
	files = /etc/supervisor/conf.d/*.conf

which implies that process configuration files can be placed in `/etc/supervisor/conf.d/`, because these file will be included in the main config file.

<http://supervisord.org/configuration.html>

The scripts that you want to run must have config files in the `supervisor/conf.d` directory.  Here are two examples of such files in our home automation system.

Save the following lines to a file as `/etc/supervisor/conf.d/mqttwarn.conf`

    [program:mqttwarn]
    directory = /home/pi/mqttwarn
    command = /home/pi//mqttwarn/mqttwarn.py
    autostart=true
    autorestart=true
    ;startretries=1000
    stderr_logfile=/home/pi/log/mqttwarn.err.log
    stdout_logfile=/home/pi/log/mqttwarn.out.log
    user = pi
    environment= MQTTWARNINI="/home/pi/mqttwarn/mqttwarn.ini"
        
Save the following lines to a file as `/etc/supervisor/conf.d/mqttPubDS18B20.conf`
    [program:mqttPubDS18B20]
    directory = /home/pi/myOpenHab/openhabfiles
    command = /home/pi/myOpenHab/openhabfiles/mqttPubDS18B20.py
    autostart=true
    autorestart=true
    ;startretries=1000
    stderr_logfile=/home/pi/log/mqttPubDS18B20.err.log
    stdout_logfile=/home/pi/log/mqttPubDS18B20.out.log
    user = pi

Save the following lines to a file as `/etc/supervisor/conf.d/mqttPubPiLED.conf`
    [program:mqttPubPiLED]
    directory=/home/pi/myOpenHab/openhabfiles
    command=/home/pi/myOpenHab/openhabfiles/mqttPubPiLED.py
    autostart=true
    autorestart=true
    ;startretries=1000
    stderr_logfile=/home/pi/log/mqttPubPiLED.err.log
    stdout_logfile=/home/pi/log/mqttPubPiLED.out.log
    user=root

    
We will be setting up numerous file similar to these during the course of the project.   
    
The first line points to the directory where mqttwarn is installed, change to suit your installation.  The same holds for the second line. In the third and fourth line enter your user home directory (if different from pi).

After changing the file reload and update or add

	sudo supervisorctl reread
	sudo supervisorctl add xxx
	sudo supervisorctl update

check that mqttwarn is running:

	sudo supervisorctl
	-> type exit to leave the tool

When in supervisor you can type `help` to get a list of commands.

Starting/stopping mqttwarn:

	sudo supervisorctl stop mqttwarn
	sudo supervisorctl start mqttwarn

see the status:

	sudo supervisorctl status
		
##Preparing files for execution in `supervisor`

`supervisor` requires the file to be executable.  Scripts (Bash, Python or Perl scripts) can be made e(x)ecutable by (a)ll users, with  the following command

    chmod a+x /path/to/your/filename.extension

<https://en.wikipedia.org/wiki/Shebang_%28Unix%29>

`#!` at the beginning of a script is called shebang. Under Unix-like operating systems, when a script with a shebang is run as a program, the program loader parses the rest of the script's initial line as an interpreter directive; the specified interpreter program is run instead.  Often the `#!` is followed by `/usr/bin/env` to introduce a level of indirection, followed by the desired command with or without full path, as in  `#!/usr/bin/env python`; which will start up the Python interpreter and then process the rest of the file in the Python interpreter.  You need to add this first line to all scripts to be run under `supervisor` (or from the command line):

    #!/usr/bin/env python
	
There is one catch however, if the file is created in Windows, the line ending is not Linux (RPi) friendly.  This means that the operating system is looking for something called `python\r', which is not recognised in Linux.  I tried converting the file from Windows to Linux format by using the `fromdos` command, but that did not help.  Opening and closing the file in `nano` did not help either.  The only remedy was to (1) open the file in `nano` move to the top of the file, (2) manually type in the whole first line followed by `Enter` a few times, making very sure that a new line ending is introduced, and (3) then remove the old line with the bad line ending.



	
