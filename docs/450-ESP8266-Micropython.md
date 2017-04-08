# ESP8266 & MicroPython

## Download and deploying


<http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware>


 You can find this tool here: <https://github.com/espressif/esptool/>, or install it using pip:

    pip install esptool

Once installed copy the esptool.py file from the site-packages to your local working directory. If you ever update the esptool script, remember to copy the new version.

The serial port is selected using the -p option, like -p /dev/ttyUSB0 or -p COM1.

Using esptool.py you can erase the flash with the command:

    esptool.py --port /dev/ttyUSB0 erase_flash
    python esptool.py --port COM4 erase_flash

And then deploy the new firmware using:

    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
    python esptool.py --port COM4 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin

# Serial REPL

<https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/serial-terminal>

Communicate with the ESP8266 with a serial channel: 

    115200 baud 
    8 bits
    no parity
    1 stop bit
    no flow control
    UART0 (GPIO1=TX, GPIO3=RX) 

On Linux or Mac OSX the screen command can be used to connect to the serial port.  Run the following command to connect at 115200 baud: `screen /dev/tty.board_name 115200`. Where `/dev/tty.board_name` is the name of the board's serial port. When you're done using screen most versions of it allow you to exit by pressing Ctrl-a then k then y or pressing Ctrl-a then typing :quit and pressing enter.

<https://www.digikey.com/en/maker/blogs/programming-micropython-on-the-esp8266/57abec67b5c34eb398d8fe6ae6442f46>  
<http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html>

    print(help)

to get quick help from ESP

This should flash a LED, call `flash(pinno)` with the pin to toggle.  

    import machine
    import time
    def flash(pinno):
        pin = machine.Pin(pinno, machine.Pin.OUT)  # Set pinno as an output.
        for i in range(10):
            pin.low()     # Set pin low 
            time.sleep_ms(300)  # Delay for 300ms 
            pin.high()     # Set pin high 
            time.sleep_ms(300)

# Set up the wifi

## Access point mode
<http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware>
<http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html>

After a fresh install and boot the device configures itself as a WiFi access point (AP) that you can connect to. The ESSID is of the form `MicroPython-xxxxxx` where the x’s are replaced with part of the MAC address of your device (so will be the same every time, and most likely different for all ESP8266 chips). The password for the WiFi is `micropythoN` (note the upper-case N). Its IP address will be 192.168.4.1.

Access point mode can also be set up with: 

    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.active(True)         # activate the interface
    ap.config(essid='ESP-AP') # set the ESSID of the access point

## Station mode
<https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html>
<https://home-assistant.io/blog/2016/07/28/esp8266-and-micropython-part1/>

A useful function for connecting to your local WiFi network is:

    def do_connect():
        import network
        SSID = 'CJMSW'
        PASSWORD = 'whatever'
        # disable access point
        ap_if = network.WLAN(network.AP_IF)
        if ap_if.active():
            ap_if.active(False)
        # enable station mode
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(SSID, PASSWORD)
            while not wlan.isconnected():
                pass
        print('network config:', wlan.ifconfig())

## WebREPL

WebREPL allows you to use the Python prompt over WiFi, connecting through a browser. The latest versions of Firefox and Chrome are supported.  WebREPL client is hosted at <http://micropython.org/webrepl>. Alternatively, you can install it locally from <https://github.com/micropython/webrepl>.  Before connecting to WebREPL, you should set a password and enable it via a normal wired serial connection (improved security). Type

    import webrepl_setup

and follow instructions.  After reboot, it will be available for connection. If you disabled automatic start-up on boot, you may run WebREPL on demand using:

    import webrepl
    webrepl.start()



