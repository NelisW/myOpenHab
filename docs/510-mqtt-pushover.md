# Pushover

[Pushover](https://pushover.net/) is a notification app for Android, IOS and other clients.  It is a relatively simple tool to set up and very simple to use.  You are allowed 7500 notifications per month on the free account.

## Setting up

1.  [Install the app from Google Play](https://play.google.com/store/apps/details?id=net.superblock.pushover&hl=en).  The app provides a seven day free trial, after which you must but the app for USD5.  The app has built in plugins for several applications, and you can add your own plugin for your specific need.

2. Create a user account on <https://pushover.net/>.  On registration you will receive a User Key, which is your identification for all notifications to be pushed over the service.  Store the key in a safe place.

3. You can send notifications by sending an email to YourKey@api.pushover.net or by sending a notification from <https://pushover.net/>


## Registering your mqttwarn application


<https://pushover.net/apps> lists a number of existing clients.  You can also register your own app from this page.  

1. Log in to Pushover with your User Key.

1.  Click on `Create a New Application`.  This should open a page with a form to complete.

2. Add a human-friendly name you want to use for this application.  This name will be used in your client as main heading, so choose an appropriate name for the notification topic.

3. Select `Script` for the type of application: we will be using JP Mens' mqttwarn Python script.

4. Add a short description.

6. In the URL field add the mqttwarn plugin script URL on github:  <https://github.com/jpmens/mqttwarn/blob/master/services/pushover.py>


7. Upload an icon to be used in the app.  This is not required, so skip if you are not into icons.

8. Check the legal agreement to indicate that you accept the terms.

9. Before you click on the 'Create Application` button make sure that this application definition is correct, somewhere there is a note that says that you cannot change the details later. So start with names like test01 at first until you are ready for the big time final version. 

10. The website should now return with your newly created API Token/Key. Make a note of this Application Key, you will need it later to set up pushover in the mqttwarn ini file. The `[config:pushover]` section you link the pushover service (`config:pushover`) with the target warning (`nagios`) you want pushed.  Use your Pushover user key (your ID created when you registered on Pushover) and the Application key you created linking JPMs mqttwarn script.

	[config:pushover]
	targets = {
	    'nagios'     : ['userkey1', 'appkey1']
	    }

11. You can create any number of new application keys to interface with other applications.


