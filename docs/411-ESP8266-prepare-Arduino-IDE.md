#ESP8266 on Windows 7 with Arduino IDE

##Install Arduino IDE

The Arduino IDE can be used to build and download ESP8266 software.

<http://www.instructables.com/id/ESP8266-ESP-12Standalone-Blynk-101/?ALLSTEPS>    
<http://www.instructables.com/id/ESP8266-Arduino-IDE-164-Portable-Full-Quick-Instal/?ALLSTEPS>    
<http://www.esp8266-projects.com/2015/06/esp8266-arduino-ide-v164-portable.html>  

1. You have to have an internet connection to execute the procedure below.
1. Download and install the Arduino IDE from here: <https://www.arduino.cc/en/Main/Software>. You can download the exe for installation (usually in your USER directory). Alternatively you can create a portable installation by  downloading the zip file and unzip in the directory of your choice.
2. If you downloaded and unzipped the zip file, Windows will not know of the software. Create a shortcut to the IDE and place it in QuickLaunch or in the Start Menu.
2. Create directory where you want to place all your working files.  This can be anywhere on your PC.  
3. Open the IDE and navigate to the Files-Preferences dialog box.  Copy the location of your working directory into the edit box that is marked with `Sketchbook location` (top of the following picture).

  ![''](images/arduino-ide-file-prefs.png)
3. While in the preferences dialog, note the location on your PC where the IDE stores your user-specific information, right at the bottom of the dialog window.  There is a `preferences.txt` file where you can set additional preferences that are not presented in the dialog box.

4. Install the ESP8266 support for IDE:  
- Open the Arduino IDE and navigate to File-Preferences
- In the `Additional boards manager URLs` paste this link:  <http://arduino.esp8266.com/stable/package_esp8266com_index.json> (an alternative url is <https://adafruit.github.io/arduino-board-index/package_adafruit_index.json>). Click the OK button to close the dialog box.  You wil do well to regularly check for updates to these files, development takes place at a brisk pace.
- Navigate to Tools-Board and then click on `Board Manager...`. A new dialog box will open. Scroll down to the ESP8266 entry, click on it and click `Install`. The IDE will now download the ESP board definitions (this software is not part of the Arduino IDE product offering, but uses the Arduino IDE's ability to load new board definitions).  
- After the installation is complete the version number should be shown, together with all the new board definitions contained in the package. Depending on the version you downloaded the board definitions may be different from the list shown here.
   ![''](images/arduino-ide-esp8266-installed.png)


- Once the board definitions are installed they will be available as selections on the Boards menu entry, as shown here:

  ![''](images/arduino-ide-install-8266.png)


---------------------------------------------------------
##Prepare the FTDI 

We used a [sparkfun FTDI Basic 3.3V](https://www.sparkfun.com/products/9873) but any equivalent USB to serial converter can be used.  Make sure to use a 3.3 V device to be compatible with the 3.3 V ESP 8266 device.

[Install the drivers 1](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/all)

[Install the drivers 2](http://www.ftdichip.com/Drivers/VCP.htm)

##FTDI card pinout

The pin definitions are shown on the silkscreen on the left side of the PCB.

![''](images/Sparkfun-basic-FTDI.jpg)

##Finding the COM port for the FTDI

https://www.youtube.com/watch?v=hou4okcCX7E

Open Computer Management > System Tools > Device Manager > Ports (COM & LPT).  
Identify the port number xx next to the text 'USB Serial Port (COMxx).

![''](images/id-com-port-windows7.PNG)

