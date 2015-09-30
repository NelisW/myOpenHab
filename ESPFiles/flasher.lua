-- code originally by Rui Santos (I think!).
-- pin 3 is GPIO 0, or D3 on the nodeMCU, switch it off
gpio.mode(3,gpio.OUTPUT)
gpio.write(3,gpio.LOW)

-- pin 4 is GPIO 2, or D4 on the nodeMCU.
lighton4=0
pin=4
gpio.mode(pin,gpio.OUTPUT)
tmr.alarm(1,2000,1,function()
    if lighton4==0 then
        lighton4=1
        gpio.write(pin,gpio.HIGH)
    else
        lighton4=0
         gpio.write(pin,gpio.LOW)
    end
end)
