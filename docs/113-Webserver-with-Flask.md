# Flask web server on Raspberry Pi

## Install Flask
Flask is a Python program and is installed using `pip` or also with `apt-get`.  The Flask manual recommends that you use a virtual environment to run Flask, but I don't believe it is necessary, especially so on the Raspberry Pi (unless you have reason to use different Python versions).

Install Flask with one of the following commands:

	sudo apt-get install flask
	sudo apt-get install python3-flask
	sudo pip install Flask

## Documentation
Flask documentation is available [here](http://flask-.readthedocs.io/en/stable/) (also in PDF/epub/mobi formats on the same website).

See also Miguel Grinberg's [Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) or his [book](http://shop.oreilly.com/product/0636920031116.do).


Introductory material [here](http://raspberryjamberlin.de/portfolio/install-flask-on-a-raspberry-pi/) and [here](https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/).


## Minimal 'Hello World' 

Create the following directory and file structure in your home directory

	[webserver]
		[app]
			[static]
			[templates]
			__init__.py
			views.py
		[temp]
		runFlask.py

with the following contents in each file:

`__init__.py`:

	from flask import Flask
	
	app = Flask(__name__)
	from app import views

`views.py`:

	from app import app
	@app.route('/')
	@app.route('/index')
	def index():
	    return "Hello, World!"
	    
`runFlask.py`:    
	#!/usr/bin/env python
	# -*- coding: utf8 -*-

	from app import app
	app.run(debug = True, host="0.0.0.0", port=int("888"))

Use the host IP as `0.0.0.0` to accept requests from any IP address on the network (if not given Flask only accept requests from localhost).  Set the port number you require (usually 80 for web pages).  If the port number is not set, the default port number assigned by Flask will be 5000.

Make the `run.py` file executable and execute the script to start the server.

	chmod a+x run.py
	./run.py

You can start the script every time the computer reboots by using supervisord as described [here](https://github.com/NelisW/myOpenHab/blob/master/docs/107-Supervisord.md), with the appropriate changes to the example files.

To confirm if the server is running, use the command

	sudo apt-get install lsof
	sudo lsof -i :888 -S

where `888` is the port number (replace with the port you are using). If the server is running on the port, `lsof` will respond with something like this:

	COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
	python  28911 root    3u  IPv4 855689      0t0  TCP *:http (LISTEN)
	python  28916 root    3u  IPv4 855689      0t0  TCP *:http (LISTEN)
	python  28916 root    6u  IPv4 855689      0t0  TCP *:http (LISTEN)

You can kill the server by killing the listed PIDs or by using supervisord (if started by supervisord).

## Server visibility

The server will only be visible on the local network (e.g., your wifi network).  To make it available for access from the internet, follow the instructions [here](https://github.com/NelisW/myOpenHab/blob/master/docs/110-Dynamic-DNS-remote-port-forwarding.md).


## References

https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/  

http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world  

http://raspberryjamberlin.de/portfolio/install-flask-on-a-raspberry-pi/  

https://www.fullstackpython.com/flask.html  

http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world  


HTTP authentication is described [here](https://media.readthedocs.org/pdf/flask-httpauth/latest/flask-httpauth.pdf)  