# Dynamic DNS and Port Forwarding

## IP addresses

1.  The RPi running on a local wifi network only has visibility within the network itself, it is not visible on the internet.  The wifi router connects the local servers to the internet so the router must be set up properly to connect the local serveron the local network to the internet.  

2. The internet identifies servers and networks by IP addresses, a 12 wide number, written with dots like this `216.58.223.35`.  We humans don't remember the numbers so well and prefer to use words, such as `www.google.com`.  The server that links the numbers to the words is called a Domain Name Server or DNS server.  If you type a word address the DNS looks up the IP address and uses that for further communication.

3.  A key issue here is that on some internet connections (e.g., ADSL) the service provides gives the router a different IP address every time that it connects (or even more frequently).  The local ADSL network does not have a fixed and constant IP address. So it is impossible to access your server on the local network from the internet, by using the service provider's IP address. Furthermore there is no DNS server that knows your ADSL router's IP address.

4. There are several suppliers on the internet that provides a dynamic IP address lookup for your router.  Some are paid services and some are free.  Your router (or some server on the local network) publishes its own  router public (temporary) internet IP address together with some identifier (typically a host name of your choice) to the service provider.  The service provider then links the hostname/identifier and pushes this to the network on DNS servers.  There is normally a mechanism that detects changes to the local router IP address and then updates the service provider's records, who in turn then pushes a new IP/hostname pair to the DNS servers.

5. For the purpose of this document we assume you want to make an HTTP server on your Raspbwrry Pi visible on the internet.  This server could serve blog pages or provide control of some service (via HTTP) on your internal network.

## Set up an HTTP server on the Raspberry Pi

Setting up a Python Flask server on the Raspberry Pi is documented [here](https://github.com/NelisW/myOpenHab/blob/master/docs/113-Webserver-with-Flask.md).

By default a Flask server runs on port 5000.  Test the webserver to ensure that it runs on the port you want to expose to the internet. Suppose that your Pi is running on ip `10.0.0.100` and the Flask server is running. Access the Pi from within your nerwork with `10.0.0.100:port` where `port` is the port number you selected.  HTTP ports are usually 80, but you can use any port number (if not already used by some other server).

## DynDNS

[DynDNS Pro](http://dyn.com/dns/) provides a paid dynamic IP lookup service (in July 2016 it costs USD40 per year) and provides up to 30 dedicated hostnames on the Pro account.  You can connect any IP device such as IP cameras or computers to the internet via DynNDS.  The instructions to subscribe and set up the service is provided [here](http://dyn.com/remote-access-6-16/).  The instructions are very generic in nature and probably does not cover your specific hardware.  

The procedure documented here worked in my instance:

1. Sign-up for a Dyn.com account and [purchase Remote Access](https://cart.dyn.com/checkout/#/). If you have an account and/or have already purchased, simply [log-in](https://account.dyn.com/entrance/).

1. Once logged into the interface, navigate to `DynDNS Pro`. The page should show your account details including currently registered DYNDNS hostnames and the IP address currently linked to the hostname.  You can a new hostname by clicking on `+ Add New Hostname`. A page will appear that allows you to enter your prefered hostname, current IP address and the type of service.

	1. Type in your prefered name. For example `savvyPetesBlog` and select the rest of the domainname from the dropout box, e.g., `is-lost.org`.  This means that your internet-visible address will be `savvyPetesBlog.is-lost.org`
	2. Select the service type to be `Host with IP address`.  This means that your router's IP address will be looked up in the DNS servers against `savvyPetesBlog.is-lost.org`
	3. Next enter the IP address you want to use, or click on the link that is shown in the page (your router's current IP address). 
	4. Change the DNS update time if you want to change the default value.
	5. Click on `Add to Cart`. This should add your new hostname againt the currently indicated IP address (which may change in future).

1. Test the hostname you created by typing it into a web browser bar _outside your home network_.  It may very well not work if 
	1. You are testing from within your wifi network. Do the testing from outside your wifi network (e.g., on your mobile phone with wifi switched off).
	2. Your router firewall rules block the incoming traffic.
	3. Port forwarding is not properly set up, could be connected with your firewall rules on some routers.
	4. Your server is not yet running (or running on the wrong port).

  All these topics are discussed below - fix them and test again until it is working.

1.  Lastly, install an updater client to ensure that any subsequent router IP address change is made known to DynDNS.  These updates could be done from the router hardware, a decicated software app running on your server or using the [Dyn updater client](http://dyn.com/apps/update-%20%20client-faqs/). DynDNS recommends that you use a software updater (I used both the router hardware and software option).  The software runs on the Raspberry Pi (see below).

  On my Netgear router there is an entry `Dynamic DNS` under `Advanced`. On the dynamic DNS setup page:
	1. Select the `WAN1` (only) option.
	2. Set the `Use a Dynamic DNS Service` check box.
	3. Select the `www.DynDNS.org` service provider.
	4. Enter your hostname (in our example `savvyPetesBlog.is-lost.org`).
	5. Enter your DynDNS user name and passwords that you used when registering with DynDNS in the first item above.
	6. Click on `Apply`.  This will cause the router to notify DynDNS of any IP changes.



## Firewall and port forwarding

On my Netgear N300/DGN2200Mv2 router the port forwarding and firewall rules are combined as set out here below.  In the example below we set up the Raspberry HTTP server to run on port 888 (replace with your own port number).

1. Open the router management console and click on the `Services` link to open up the `Services` page. 
2. Click on `Add` and then enter the following details into the fields and click on `Add` when done:


  |Field | Enter|
  |--|--|
  |Name  | RPiHTTP| 
  |Type  | TCP | 
  |Start port  | 888 | 
  |End port  |888  | 






https://alselectro.wordpress.com/2015/07/03/port-forwarding-part-1-tips-troubleshooting/

https://alselectro.wordpress.com/2015/07/04/port-forwarding-part-2-solution/

http://portforward.com/

