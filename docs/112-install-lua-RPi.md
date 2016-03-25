# lua on RPi

https://bigdanzblog.wordpress.com/2015/04/16/installing-lua-on-raspberry-pi-and-getting-it-running/

lua is already installed on RPi

	rpi/~:lua
	Lua 5.1.5  Copyright (C) 1994-2012 Lua.org, PUC-Rio
	>

	rpi/~:whereis lua
	lua: /usr/bin/lua5.1 /usr/bin/lua /usr/bin/X11/lua5.1 /usr/bin/X11/lua /usr/share/lua /usr/share/man/man1/lua.1.gz
	rpi/~:
	
If it is not installed do:

	sudo apt-get update
	sudo apt-get install lua5.1

I also need the networking module. That is installed with:

	sudo apt-get install lua-socket

Find other lua modules:

	apt-cache search '^lua-.*'
	
Now create a simple test program such as this helloworld:

	rpi/lua:vi helloworld

	# !/usr/bin/lua

	print ('hello world')

Make it executable:

	rpi/lua:chmod 755 helloworld
	
and finally try it out:

	rpi/lua:./helloworld
	hello world
	rpi/lua:
	
<hr>

<http://andre-simon.de/doku/rpi_gpio_lua/en/rpi_gpio_lua.php>


	
