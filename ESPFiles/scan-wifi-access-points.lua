--this file requires prior connection to the wifi

--https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout/using-nodemcu-lua
-- print ap list
function listap(t)
      for ssid,v in pairs(t) do
        authmode, rssi, bssid, channel = string.match(v, "(%d),(-?%d+),(%x%x:%x%x:%x%x:%x%x:%x%x:%x%x),(%d+)")
        print(ssid,authmode,rssi,bssid,channel)
      end
end
      
wifi.sta.getap(listap)