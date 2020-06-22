# sample-server

To read more about the SAMPLE project, see [sample-main repository](https://github.com/Dinuirar/sample-main)  

This server is intended to run on Raspberry Pi 4. It was tested on 64-bit Ubuntu 19, but I guess it would be easier to set up on 32-bit Raspbian ; )  
If you want to use it on 64-bit Ubuntu 19:  
- install *raspi-config* following the instructions from [FalcoGer's answer on askubuntu](https://askubuntu.com/questions/1130052/enable-i2c-on-raspberry-pi-ubuntu):
  - `sudo add-apt-repository ppa:ubuntu-pi-flavour-makers/ppa`
  - edit `/etc/apt/sources.list.d/ubuntu-pi-flavour-makers-ubuntu-ppa-eoan.list` with some command-line text editor (for example `nano` or `vim`) and add this line:  
 `deb http://ppa.launchpad.net/ubuntu-pi-flavour-makers/ppa/ubuntu bionic main`
  - `sudo apt update`
  - `sudo apt install raspi-config` 
- enable I2C (for communication with BME280) and PiCamera using *raspi-config* (note that at the moment of writing this README there was a bug causing entries in menu to be offset by one with respect to what is being displayed)
- to install raspistill tool use the instructions from [James Kingdon on armbian forum](https://forum.armbian.com/topic/4764-running-32-bit-applications-on-aarch64/)
  - add an armhf architecture to dpkg `dpkg --add-architecture armhf`
  - `apt-get update`
  - `apt-get install libc6:armhf libstdc++6:armhf`
  - `cd /lib`
  - `ln -s arm-linux-gnueabihf/ld-2.23.so ld-linux.so.3`
- and install [userland](https://github.com/raspberrypi/userland) libraries (rememeber to run `./buildme --aarch64` ;) )

# Dependencies
NOTE:  
`ADDRESS` is the address of the server in LAN. It is just an IP address of your Pi, so something like `192.168.1.206`. If you are accessing the server from your RPi you can also use `localhost` instead of an actual address.

To run *sample-server* on local machine:  
- download dependencies from *requirements.txt* (using *sudo pip3 install -r requirements.txt*)  
- run `./start-server.sh`  
- you can visit sample-server pages on `ADDRESS:80/index`.  
Telemetry/telecommand endpoints are documented using swagger.ui which is available on `ADDRESS:80`  
Visiting `ADDRESS:80/photo` triggers taking a photo with a camera.

Note:  
You can generate `requirements.txt` file using a command `pip3 freeze > requirements.txt`


Thanks to Matt Hawkins for a BME280 Python driver! 
It was intended for Python 2, but it turned out that with Python3 it works like charm (after adding some parenthesis).
You can read how to use this driver (and find download link for it) on the website:
https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/
