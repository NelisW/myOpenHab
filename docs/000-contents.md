# Roadmap

This document serves as an overview to the home automation design described on this website.  
In completing my system I tried to document the process along the way (mainly as reference for myself, but also to assist others).  In some areas the documentation may be more complete and in other areas less so.  

The system is relatively complex, comprising many different technologies and software tools.  To succeed in reconstructing this project, you would require a working knowledge of the Linux operating system, together with a flair for electronics (but you need not be a specialist in either of these).  

The Internet is exceedingly successful in making information available, and what you see here is not new, just repackaged.  The Internet is however exceedingly weak in configuration and quality control.  In a dynamically changing environment most of the information on the Internet is old and to some extent not fully relevant.  You need to filter and evaluate before accepting Internet-based information.  This set of documents is an attempt to bring together the current information (August 2015).  The  information contained here is also subject to time expiry, it is at best a current snapshot.


## Overview

This repository serves to document my work in building my home automation system using readily available tools and technologies.  There are several well documented examples on the web but, as you probably also experienced, none of these are quite complete in the sense of what I wanted to do.  You would also find these notes lacking, for the same reason.

The point of departure is to use existing tools to the maximum extent; there is no point in repeating what someone else has already done.  To this end, my notes contain links to the web pages I used, together with very brief comments or notes to remind me of what I did.  

When I started on this project I had a reasonably good idea of what I wanted, but had no hardware to work with (except the Raspberry Pi [RPi]). The hardware was ordered, but still floating somewhere in the international mail system.  This forced me to look into architectures and tools before plunging into hardware details.  

A non-trivial home automation system has considerable  complexity.  There are communication protocols, control software, user-interface software and much more.  The design choices we make shifts the complexity around between the parts, but the sum total complexity remains the same.  Retrospectively, it became evident that our decision to use MQTT/openHAB/supervisor and associated libraries, simplified our communication protocols and coding (simple messages along specific topics), but it increased the complexity of infrastructure in terms of libraries and tools.  Someone else might decide that the overhead of installing and maintaining the infrastructure is too complex and go for a low footprint option; but that would require more coding and more complex messages during implementation. In the end, the effort is the same.

## Design options

![blockdiagram01.svg](images/blockdiagram01.svg)

The main components in the home automation are shown in the diagram above.  Most systems follow this architecture in broad terms, but there may be variations. In the home the automation server integrates the system via a communication network. This network can we wired or wireless.  In both cases there are potentially several different types of communication links, and these links can be mixed types as well.  Of key importance is the automation server's role of communication with the various devices on the network.  These devices include sensors (temperature, humidity, etc.) and controllers (power switches, servo motors, etc.).  The automation server is where it all comes together.  The server communicates to one or more cloud services on the Internet or via the GSM network.  Some home automation systems offer smart phone handset interfaces, which can be accessed via wireless technology on the local area network or on internet protocols via mobile networks.  If the phone is on a local area wireless network, the communication is directly with the automation server.

The home automation marketplace is highly competitive in the commercial as well as the open source spheres. There is no standard today, only stronger and weaker offerings.  The multitude of product offerings makes committing to a specific offering a very difficult call.  I made my calls and report on this, you may have different convictions and needs. To each his own.

The core of the system is the local automation server and the many clients actually doing the work.  This core is software based and should provide the integration between the units and the required monitoring and control functionality.  The scope and reach of this core part of the system is local to the home.  The better known offerings include:

- openHAB, providing a home server and an internet cloud, together with Android and IOS applications.

- [Domoticz](https://domoticz.com/),  a C++-based home automation server, for various operating systems, using HTML5 front-end. Not further investigated.

- [openRemote](http://openremote.org/display/HOME/OpenRemote)

- Souliss, providing a home server, but no cloud capability - use openHAB for cloud access.

- http://domotica-arduino.es/en/ mostly in Spanish.

Other sites of interest:

- http://www.ingeniousfool.net/

- http://www.homeautomationforgeeks.com/index.shtml

- http://www.mysensors.org/

- http://www.instructables.com/id/Uber-Home-Automation-w-Arduino-Pi/?ALLSTEPS  

- http://jonathangiles.net/blog/?p=1646

- [OpenEnergyMonitor](http://openenergymonitor.org/emon/) is not quite a home automation system, but relates to remote-access home energy management.  See here for a  [PV power management system](http://openenergymonitor.org/emon/mk2)

Commercial and open source offerings for cloud-based automation services abound. Ideally the home automation system should be able to provide cloud access for monitoring and control purposes, but it should not depend on access to the cloud for basic operation.  The cloud provides roaming access to part of all of the functionality available in the home.
Some of the free and open source offerings include:

- openHAB

- Home Automation Server is a relative newcomer  http://homeautomationserver.com/about

- Blynk and many other smart phone applications offer access to your IoT clients/devices but can not really be considered home automation servers.

- There are many commercial systems offering free access 'at the moment' but these services are not considered here.

- Numerous commercial systems are on offer, but were not considered here.

- Off-the-Internet servers, e.g., using GSM networks were not considered here, even though these may provide more secure environments.


The communication options for the local area network between the devices and the server are very wide.  These options include wired connections such as RS485, ethernet and other wired connections using a great many protocols including TCP/IP, I2C, ISP and many more.  There are also numerous wireless approaches that may be used.  Some of these offerings include: wifi, Zigbee, RF69, RF24, etc.


If there are many software offerings, there are even more hardware products.  Open source or DIY approaches could use Raspberry Pi's, Arduinos, ESP266, PIC, and numerous other cards.  We choose the ESP8266 as the main client controller because it provides a reasonably powerful microcontroller and a wifi interface at a reasonable price.

## File structure

The series of files in the `docs` directory of this repo serve to capture my experiences, actions and insights.  The files are not all in the same state of completion, some just contain links to web sites.

A number of smaller files are used, rather than one large file, to help help focus and direct access.  The files are using markdown for formatting: easily edited by any ACII editor, and equally easily rendered by a number of markdown renderers.

Files are grouped in number series in order to contain topics together.  The file sequence is more or less chronological in implementation sequence, but there is no requirement to strictly follow this sequence.

Filenames are constantly changing, attempting to find the best file numbers for different topics.

It is recommended that you read and construct the RPi, the MQTT and openHAB functionality as a single unit.

- 1xx describe various aspects of the Raspberry Pi installation and use.
- 2xx describe protocols and using these protocols (such as MQTT).
- 3xx describe the installation, set up and use of openHAB.
- 4xx describe RF technologies, hardware and software (mainly ESP8266)
- 5xx describe various clients (Android and web) that may be useful
- 6xx describe OpenEnergyMonitor (home and PV energy measurement)
- 7xx describe sensors for use in home automation
