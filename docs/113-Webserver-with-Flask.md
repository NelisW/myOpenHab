# Flask web server on Raspberry Pi

## Install Flask


## Documentation
Flask documentation is available at http://flask-.readthedocs.io/en/stable/ (also in PDF/epub/mobi formats on the same website).

See also Miguel Grinberg's [Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

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
	app.run(debug = True, host="0.0.0.0",port=int("888"))

Use the host IP as `0.0.0.0` to accept requests from any IP address (if not given Flask only accept requests from localhost).  Set the port number you require (usually 80 for web pages).  If the port number is not set, the default port number assigned by Flask will be 5000.

Make the `run.py` file executable and execute the script to start the server.

	chmod a+x run.py
	./run.py

You can start the script every time the server reboots by using supervisord as described [here](https://github.com/NelisW/myOpenHab/blob/master/docs/107-Supervisord.md).



"""
port 5000 seems to run without sudo
python run.py
port 80 seems to require
sudo python run.py

Once the server is running, closing the run.pu script may not 
kill the server. If this is the case find the PID and kill it 
manually.

sudo lsof -i :80 -S
 where 80 is the port number

COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python  28911 root    3u  IPv4 855689      0t0  TCP *:http (LISTEN)
python  28916 root    3u  IPv4 855689      0t0  TCP *:http (LISTEN)
python  28916 root    6u  IPv4 855689      0t0  TCP *:http (LISTEN)

"""







https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/

http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

http://raspberryjamberlin.de/portfolio/install-flask-on-a-raspberry-pi/


https://www.fullstackpython.com/flask.html

http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

The book http://shop.oreilly.com/product/0636920031116.do


HTTP authentication is described [here](https://media.readthedocs.org/pdf/flask-httpauth/latest/flask-httpauth.pdf)