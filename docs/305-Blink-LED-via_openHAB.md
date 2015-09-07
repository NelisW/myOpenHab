#Blinking a LED via openHAB

detail to follow


[Use a MAP](http://forum.mysensors.org/topic/1405/adding-a-light-switch-to-openhab-mqtt-gateway/2):

    Switch node1_sw1 "sw1" {mqtt=">[mysensors:MyMQTT/1/1/V_LIGHT:command:ON:1],>[mysensors:MyMQTT/1/1/V_LIGHT:command:OFF:0],<[mysensors:MyMQTT/1/1/V_LIGHT:command:MAP(1on0off.map)]"}
