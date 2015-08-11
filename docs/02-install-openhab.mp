#Start and stop openHAB

	sudo /etc/init.d/openhab start
	sudo /etc/init.d/openhab status
	sudo /etc/init.d/openhab restart
	sudo /etc/init.d/openhab stop

You have to wait a while for the stop command to execute.

#Install OpenHab

<http://www.instructables.com/id/OpenHAB-on-Raspberry-Pi>  
<http://www.openhab.org/getting-started/index.html>  
<https://github.com/openhab/openhab/wiki/Samples-Tricks#how-to-configure-openhab-to-start-automatically-on-linux>

Update the software packages

	sudo apt-get update
	sudo apt-get upgrade
	
Update raspbian

	sudo rpi-update
	
Create a directory to download openhab
	
	sudo mkdir /opt/openhab	
	cd /opt/openhab 
	
Get the latest version and unzip

	sudo wget https://bintray.com/artifact/download/openhab/bin/distribution-1.7.1-runtime.zip  
	sudo unzip distribution-1.7.1-runtime.zip
	sudo rm distribution-1.7.1-runtime.zip
	
The runtime is installed and the zip files erased, but in order for openHAB to work you will need to add bindings. Upon extrating the runtime zip a "addons" folder was created. All bindings belong in this folder. Go to the addons folder and extract the addons zip. First lets download them to the appropriate folder.	
	
	cd addons/
	sudo wget https://bintray.com/artifact/download/openhab/bin/distribution-1.7.1-addons.zip
	sudo unzip distribution-1.7.1-addons.zip
	sudo rm distribution-1.7.1-addons.zip

This contains all the bindings available for openHAB. As stated in the openHAB wiki, Bindings are optional packages that can be used to extend functionality of openHAB. 

	cd ..
	sudo cp configurations/openhab_default.cfg configurations/openhab.cfg
	
make a copy of the "openhab_default.cfg" file. You will call the copy "openhab.cfg". In the event that you have to update your openhab the default file will be updated as well. By making a copy of this file, openhab will use this file for configurations and also not update it. Since you will be making your own custom configurations, it is important that those get written in the "openhab.cfg" file for safe keeping.

Deploy the demo app

	cd /opt/openhab
	sudo wget https://bintray.com/artifact/download/openhab/bin/distribution-1.7.1-demo.zip
	sudo unzip distribution-1.7.1-demo.zip
	sudo rm distribution-1.7.1-demo.zip 
	sudo chmod +x start.sh
	
When unzipping it will ask to overwrite addons/org.openhab.binding.http-1.7.1.jar.
I am not sure if the answer must be yes or no. I said yes.


Then the fun begins:

	sudo ./start.sh
	
You should have a fully loaded demo that you can use to familiarize yourself with openHAB. Just go to your telephone or computer and place the following url in your favorite browser. Be sure to replace the ip address with the Ip address of your Pi. 

http://10.0.0.16:8080/openhab.app?sitemap=demo

	
#openHAB to start at boot

Create a new file in the /etc/init.d folder called "openhab" using your favourite editor

	sudo geany /etc/init.d/openhab

See the contents of the file here:   
<https://github.com/openhab/openhab/wiki/Samples-Tricks#how-to-configure-openhab-to-start-automatically-on-linux>
Be sure to remove leading spaces  (the hash comments must all start on the first character of the line).

    #! /bin/sh
    ### BEGIN INIT INFO
    # Provides:          openhab
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: OpenHAB Daemon
    ### END INIT INFO

    # Author: Thomas Brettinger 

    # Do NOT "set -e"

    # PATH should only include /usr/* if it runs after the mountnfs.sh script
    PATH=/sbin:/usr/sbin:/bin:/usr/bin

    DESC="Open Home Automation Bus Daemon"
    NAME=openhab
    DAEMON=/usr/bin/java
    PIDFILE=/var/run/$NAME.pid
    SCRIPTNAME=/etc/init.d/$NAME
    ECLIPSEHOME="/opt/openhab";
    HTTPPORT=8080
    HTTPSPORT=8443
    TELNETPORT=5555
    # be sure you are adopting the user to your local OH user 
    RUN_AS=pi

    # get path to equinox jar inside $eclipsehome folder
    cp=$(find $ECLIPSEHOME/server -name "org.eclipse.equinox.launcher_*.jar" | sort | tail -1);

    DAEMON_ARGS="-Dosgi.clean=true -Declipse.ignoreApp=true -Dosgi.noShutdown=true -Djetty.port=$HTTPPORT -Djetty.port.ssl=$HTTPSPORT -Djetty.home=$ECLIPSEHOME -Dlogback.configurationFile=$ECLIPSEHOME/configurations/logback.xml -Dfelix.fileinstall.dir=$ECLIPSEHOME/addons -Djava.library.path=$ECLIPSEHOME/lib -Djava.security.auth.login.config=$ECLIPSEHOME/etc/login.conf -Dorg.quartz.properties=$ECLIPSEHOME/etc/quartz.properties -Djava.awt.headless=true -jar $cp -console ${TELNETPORT}"

    # Exit if the package is not installed
    [ -x "$DAEMON" ] || exit 0

    # Read configuration variable file if it is present
    [ -r /etc/default/$NAME ] && . /etc/default/$NAME

    # Load the VERBOSE setting and other rcS variables
    . /lib/init/vars.sh

    # Define LSB log_* functions.
    # Depend on lsb-base (>= 3.2-14) to ensure that this file is present
    # and status_of_proc is working.
    . /lib/lsb/init-functions

    #
    # Function that starts the daemon/service
    #
    do_start()
    {
        # Return
        #   0 if daemon has been started
        #   1 if daemon was already running
        #   2 if daemon could not be started
        start-stop-daemon --start --quiet --make-pidfile --pidfile $PIDFILE --chuid $RUN_AS --chdir $ECLIPSEHOME --exec $DAEMON --test > /dev/null \
            || return 1
        start-stop-daemon --start --quiet --background --make-pidfile --pidfile $PIDFILE --chuid $RUN_AS --chdir $ECLIPSEHOME --exec $DAEMON -- $DAEMON_ARGS \
            || return 2
        # Add code here, if necessary, that waits for the process to be ready
        # to handle requests from services started subsequently which depend
        # on this one.  As a last resort, sleep for some time.
        return 0
    }

    #
    # Function that stops the daemon/service
    #
    do_stop()
    {
        # Return
        #   0 if daemon has been stopped
        #   1 if daemon was already stopped
        #   2 if daemon could not be stopped
        #   other if a failure occurred
        start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --pidfile $PIDFILE --name $NAME
        RETVAL="$?"
        [ "$RETVAL" = 2 ] && return 2
        # Wait for children to finish too if this is a daemon that forks
        # and if the daemon is only ever run from this initscript.
        # If the above conditions are not satisfied then add some other code
        # that waits for the process to drop all resources that could be
        # needed by services started subsequently.  A last resort is to
        # sleep for some time.
        start-stop-daemon --stop --quiet --oknodo --retry=0/30/KILL/5 --exec $DAEMON
        [ "$?" = 2 ] && return 2
        # Many daemons don't delete their pidfiles when they exit.
        rm -f $PIDFILE
        return "$RETVAL"
    }

    #
    # Function that sends a SIGHUP to the daemon/service
    #
    do_reload() {
        #
        # If the daemon can reload its configuration without
        # restarting (for example, when it is sent a SIGHUP),
        # then implement that here.
        #
        do_stop
        sleep 1
        do_start
        return 0
    }

    case "$1" in
      start)
        log_daemon_msg "Starting $DESC"
        do_start
        case "$?" in
            0|1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
        esac
        ;;
      stop)
        log_daemon_msg "Stopping $DESC" 
        do_stop
        case "$?" in
            0|1) log_end_msg 0 ;;
            2) log_end_msg 1 ;;
        esac
        ;;
      status)
           status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
           ;;
      #reload|force-reload)
        #
        # If do_reload() is not implemented then leave this commented out
        # and leave 'force-reload' as an alias for 'restart'.
        #
        #log_daemon_msg "Reloading $DESC" "$NAME"
        #do_reload
        #log_end_msg $?
        #;;
      restart|force-reload)
        #
        # If the "reload" option is implemented then remove the
        # 'force-reload' alias
        #
        log_daemon_msg "Restarting $DESC" 
        do_stop
        case "$?" in
          0|1)
            do_start
            case "$?" in
                0) log_end_msg 0 ;;
                1) log_end_msg 1 ;; # Old process is still running
                *) log_end_msg 1 ;; # Failed to start
            esac
            ;;
          *)
              # Failed to stop
            log_end_msg 1
            ;;
        esac
        ;;
      *)
        #echo "Usage: $SCRIPTNAME {start|stop|restart|reload|force-reload}" >&2
        echo "Usage: $SCRIPTNAME {start|stop|status|restart|force-reload}" >&2
        exit 3
        ;;
    esac
    :


Lastly you will want to make this an executable file. 

	sudo chmod a+x /etc/init.d/openhab

And for it to automatically boot at the start of Pi 

	sudo update-rc.d openhab defaults	

you should get a response like this:
	
	update-rc.d: using dependency based boot sequencing
	
If you get an error that looks like this: 

	insserv: Script openhab is broken: incomplete LSB comment. 
	insserv: missing `Provides:' entry: please add. 
	....
	insserv: Default-Stop undefined, assuming empty stop runlevel(s) for script `openhab'	
	
Then you have an indentation problem. Sometimes upon pasting into your editor the text gets placed into an easy to read format which places indentations into some of the initial lines of code. Any information that is written for update-rc.d must be in first column. And there should not be any tabulation or space before the "#". If there are any remove them or you will generate that error. 

It seems that the /opt/openhab files must be in the pi group and owned by pi to load at boot. Do the following:

	sudo chown -hR pi:pi /opt/openhab
	
openhab should now load at boot.


