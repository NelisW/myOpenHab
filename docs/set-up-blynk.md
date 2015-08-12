#Setting up for Blynk

http://www.blynk.cc/getting-started

##install wiring Pi

<http://wiringpi.com/download-and-install/>

git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
cd wiringPi
./build

run the gpio command to check the installation:
cd gpio
gpio -v
gpio readall


##install blynk library

<https://github.com/blynkkk/blynk-library/blob/master/docs/Platforms.md#linux-raspberry-pi>

git clone https://github.com/blynkkk/blynk-library.git
cd blynk-library/linux
./build.sh raspberry

to run:
sudo ./blynk --token=YourAuthToken

##blynk on github

Libraries and examples for embedded hardware to work with Blynk platform <http://www.blynk.cc/>

<https://github.com/blynkkk/blynk-library>

Very limited documentation

<https://github.com/blynkkk/blynkkk.github.io>

