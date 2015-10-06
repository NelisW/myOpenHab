#MQTT in lua


<http://www.nodemcu.com/docs/mqtt-module/>
<http://www.nodemcu.com/docs/mqtt-client-module/>

`mqtt.Client(clientid, keepalive, user, pass)` creates an  mqtt client. It returns an mqtt client.

- clientid: the client id.
- : keepalive second, a number.
- user: user name, a string.
- pass: user password, a string.

`mqtt:lwt(topic, message, qos, retain)` setup Last Will and Testament (optional)
Broker will publish a message with qos = 0, retain = 0, data = "offline"
to topic "/lwt" if client don't send keepalive packet. Returns nil.

- topic: the topic to publish to, String.
- message: the message to publish, Buffer or String.
- qos: qos level, default 0.
-retain: retain flag, default 0.



`mqtt:connect( host, port, secure, function(client) )` Connects to the broker specified by the given host, port, and secure options. Returns nil.

- host: host domain or ip, string.
- port: number, broker port.
- secure: 0 or 1, default 0.
- function(client): when connected, call this function.


`mqtt:close()` close connection to the broker. Returns nil.


`mqtt:publish( topic, payload, qos, retain, function(client) )` Publish a message. Returns nil.

- topic: the topic to publish to, string
- message: the message to publish, string
- qos: qos level, default 0
- retain: retain flag, default 0
- function(client): callback fired when PUBACK received.

`mqtt:subscribe(topic, qos, function(client, topic, message))` Subscribe to a topic or topics. Returns nil.

- topic: a string topic to subscribe to
- qos: qos subscription level, default 0
- function(client, topic, message): callback fired when message received.

`mqtt:on(event, function(client, [topic], [message]))` Register callback function to event. Returns nil.

- event: string, which can be: `connect`, `message`, `offline`
- function cb(client, [topic], [message]): callback function. The first param is the client.
- If event is "message", the 2nd and 3rd param are received topic and message in string.

**Example code 1**
<http://www.nodemcu.com/docs/mqtt-module/>

    -- init mqtt client with keepalive timer 120sec
    m = mqtt.Client("clientid", 120, "user", "password")

    -- setup Last Will and Testament (optional)
    -- Broker will publish a message with:
    -- qos = 0, retain = 0, data = "offline" 
    -- to topic "/lwt" if client don't send keepalive packet
    m:lwt("/lwt", "offline", 0, 0)

    m:on("connect", function(con) print ("connected") end)
    m:on("offline", function(con) print ("offline") end)

    -- on publish message receive event
    m:on("message", function(conn, topic, data) 
      print(topic .. ":" ) 
      if data ~= nil then
        print(data)
      end
    end)

    -- for secure: m:connect("192.168.11.118", 1880, 1)
    m:connect("192.168.11.118", 1880, 0, function(conn) 
        print("connected") 
    end)

    -- subscribe topic with qos = 0
    m:subscribe("/topic",0, function(conn) 
        print("subscribe success") 
    end)

    -- publish a message with data = hello, QoS = 0, retain = 0
    m:publish("/topic","hello",0,0, function(conn) 
        print("sent") 
    end)

    m:close();
    -- you can call m:connect again


**Example code 2**

<https://github.com/nodemcu/nodemcu-firmware>

	-- init mqtt client with keepalive timer 120sec
	m = mqtt.Client("clientid", 120, "user", "password")
	
	-- setup Last Will and Testament (optional)
	-- Broker will publish a message with qos = 0, retain = 0, data = "offline"
	-- to topic "/lwt" if client don't send keepalive packet
	m:lwt("/lwt", "offline", 0, 0)
	
	m:on("connect", function(con) print ("connected") end)
	m:on("offline", function(con) print ("offline") end)
	
	-- on publish message receive event
	m:on("message", function(conn, topic, data)
	  print(topic .. ":" )
	  if data ~= nil then
	    print(data)
	  end
	end)
	
	-- m:connect( host, port, secure, auto_reconnect, function(client) )
	-- for secure: m:connect("192.168.11.118", 1880, 1, 0)
	-- for auto-reconnect: m:connect("192.168.11.118", 1880, 0, 1)
	m:connect("192.168.11.118", 1880, 0, 0, function(conn) print("connected") end)
	
	-- subscribe topic with qos = 0
	m:subscribe("/topic",0, function(conn) print("subscribe success") end)
	-- or subscribe multiple topic (topic/0, qos = 0; topic/1, qos = 1; topic2 , qos = 2)
	-- m:subscribe({["topic/0"]=0,["topic/1"]=1,topic2=2}, function(conn) print("subscribe success") end)
	-- publish a message with data = hello, QoS = 0, retain = 0
	m:publish("/topic","hello",0,0, function(conn) print("sent") end)
	
	m:close();  -- if auto-reconnect == 1, will disable auto-reconnect and then disconnect from host.
	-- you can call m:connect again


**Example code 3**

<https://www.cloudmqtt.com/docs-nodemcu.html>

	-- initiate the mqtt client and set keepalive timer to 120sec
	mqtt = mqtt.Client("client_id", 120, "username", "password")
	
	mqtt:on("connect", function(con) print ("connected") end)
	mqtt:on("offline", function(con) print ("offline") end)
	
	-- on receive message
	mqtt:on("message", function(conn, topic, data)
	  print(topic .. ":" )
	  if data ~= nil then
	    print(data)
	  end
	end)
	
	mqtt:connect("hostname", port, 0, function(conn) 
	  print("connected")
	  -- subscribe topic with qos = 0
	  mqtt:subscribe("my_topic",0, function(conn) 
	    -- publish a message with data = my_message, QoS = 0, retain = 0
	    mqtt:publish("my_topic","my_message",0,0, function(conn) 
	      print("sent") 
	    end)
	  end)
	end)



**Example code 4**
<http://www.esp8266.com/viewtopic.php?f=24&t=5616>
How to reconnect when the connection is lost.


##DS18B20 with MQTT and Lua

<http://www.esp8266.com/viewtopic.php?f=19&t=3418>
<https://github.com/beckdac/esp8266_lua_mqtt_ds18b60>


-------------



https://github.com/nodemcu/nodemcu-firmware

https://primalcortex.wordpress.com/2015/02/06/nodemcu-and-mqtt-how-to-start/

https://primalcortex.wordpress.com/2015/02/13/esp8266-nodemcu-and-mqtt-event-subscription-load-testing/

https://primalcortex.wordpress.com/2015/02/13/esp8266-nodemcu-and-mqtt-event-publishing-queueing/

https://primalcortex.wordpress.com/2015/02/24/mqtt-publishing-on-the-esp8266/

Not nodeMCU: <https://olimex.wordpress.com/2015/05/15/esp8266-evb-lua-mqtt-example/>


Not nodeMCU: <https://github.com/geekscape/mqtt_lua>

[Lua quick reference](https://gist.github.com/tylerneylon/5853042)  

