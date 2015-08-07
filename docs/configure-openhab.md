Configuring the openHAB runtime

This page describes the different places in which the openHAB runtime can be configured and customized:

    general configuration
    individual configuration
    advanced configuration

Note: The configuration files are text files that can be edited with any text editor of your choice. Nevertheless, you may want to use the openHAB designer to edit them, and you will get informed about any syntax error. Note that the expected file encoding is UTF-8.

Note: Items and sitemap(s) may be changed during runtime as needed.

Note: Use the demo setup if you wish: http://www.openhab.org/downloads.html
General Configuration - openhab.cfg

The runtime comes with one core configuration file, the file openhab_default.cfg. The purpose of this file is to define all basic settings, such as IP addresses, mail server, folder locations etc.

The file also contains settings for all (optional) bindings. These settings are automatically dispatched to the according binding. For this, all settings come with a namespace (such as "mail:" or "knx:") to identify the associated binding.

First thing after unzipping the runtime should be creating a copy of openhab_default.cfg to openhab.cfg. All personal settings should always only be done in this copy. This ensures that your settings are not lost, if you unzip a new version of the runtime to your openHAB home directory.

The openhab_default.cfg file comes with extensive comments which explain, what settings are available and what can be configured with them. If you have any doubts, please ask on the discussion group.

To activate a binding uncomment the specific settings.

Example: The easiest way of configuring a KNX binding is by connecting in ROUTER mode. To do so, enable this: knx:type=ROUTER . If you cannot use the ROUTER mode, set it to TUNNEL, but you must then configure the IP: knx:ip=<IP of the KNX-IP module>
Individual Configuration

Besides the *.cfg files and *.xml files (see below: loggin) the configuration folder ${openhab_home}/configurations consists of dedicated subfolders for specific topics. For each topic, there should be another sub folder, such as ${openhab_home}/configurations/items.
Item Definitions

Item files are stored in ${openhab_home}/configurations/items.

Although items can be dynamically added by item providers (as OSGi services), it is usually very practical to statically define most of the items that should be used in the UI or in automation rules.

These static definition files follow a certain syntax. This syntax will be explained here. (For the technical interested: This syntax is in fact a Xtext DSL grammar.)

Please visit the Items page on how to configure items.
Sitemap Definitions

Sitemap files are stored in ${openhab_home}/configurations/sitemaps.

Sitemaps are a declarative UI definition. With a few lines it is possible to define the structure and the content of your UI screens.

(For the technical interested: This syntax is in fact a Xtext DSL grammar.)

Please see page sitemaps for a description on how to create sitemaps.
Automation

Rule files are stored in ${openhab_home}/configurations/rules.

Script files are stored in ${openhab_home}/configurations/scripts.

Rules provide flexible logic to openHAB for automation which can also use scripts(macros) using related events and actions..

Please visit the automation section for further detailes.
Persistence

Script files are stored in ${openhab_home}/configurations/persistence.

Persistences can store item states over a time (a time series).

Please visit the persistence section for further details.
Transformation

Transformations files are stored in ${openhab_home}/configurations/transformation.

Purpose: tbd...

Please visit the transformation section for further details.
Advanced Configuration
general

You will find the openHAB configuration under /etc/openhab. If you change configuration files it will not be overwritten by updates or upgrades.
${openhab_home}/etc/default/openhab

USER_AND_GROUP=openhab:openhab
HTTP_PORT=8080
HTTPS_PORT=8443
TELNET_PORT=5555
OPENHAB_JAVA=/usr/bin/java

Logging
Configuration

The runtime uses /etc/openhab/logback.xml. A template for debugging is provided through /etc/openhab/logback_debug.xml. You can change logback.xml to your needs.
Log files

The runtime log: /var/log/openhab/openhab.log Further log files are placed also into: /var/log/openhab/
Jetty

/etc/openhab/jetty/etc/
Runtime generated files

/var/lib/openhab
login.conf

/etc/openhab/login.conf
users.cfg

/etc/openhab/users.cfg
quartz.properties

/etc/openhab/quartz.properties


---------------------------------
Security


Documentation of openHAB's security features
Introduction

To secure the communication with openHAB there are currently two mechanisms in place

    HTTPS
    Authentication

Authentication is implemented by SecureHttpContext which in turn implements HttpContext. This SecureHttpContext is registered with the OSGi !HttpService and provides the security hook handleSecurity. At least all authentication requests are delegated to the javax.security.auth.login.LoginContext.LoginContext which is the entry point to JAAS (http://en.wikipedia.org/wiki/Java_Authentication_and_Authorization_Service) !LoginModules.

The SecureHttpContext is currently used by the WebAppServlet and the CmdServlet which constitutes the default iPhone UI as well as the RESTApplication which provides the REST functionality.
HTTPS

openHAB supports HTTPS out of the box. Just point your browser to

https://127.0.0.1:8443/openhab.app?sitemap=demo#

and the HTTP communication will be encrypted by SSL.

If you prefer to use your own X.509 certificates, you can. Configure_SSL has information on how to do that, and there's a step-by-step guide specifically for openHAB users.
Authentication

In order to activate Authentication one has to add the following parameters to the openHAB start command line

    -Djava.security.auth.login.config=./etc/login.conf - the configuration file of the JAAS !LoginModules

By default the command line references the file <openhabhome>/etc/login.conf which in turn configures a PropertyFileLoginModule that references the user configuration file login.properties. One should use all available LoginModule implementation here as well (see http://wiki.eclipse.org/Jetty/Tutorial/JAAS for further information).

The default configuration for login credentials for openHAB is the file <openhabhome>/configuration/users.cfg. In this file, you can put a simple list of "user=pwd" pairs, which will then be used for the authentication. Note that you could optionally add roles after a comma, but there is currently no support for different roles in openHAB.
Security Options

The security options can be configured through openhab.cfg. One can choose between

    ON - security is enabled generally
    OFF - security is disabled generally
    EXTERNAL - security is switched on for external requests (e.g. originating from the Internet) only

To distinguish between internal and external addresses one may configure a net mask in openhab.cfg. Every ip-address which is in range of this net mask will be treated as internal address must not be authorized though.

