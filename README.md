# Installation
**[Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/)**  

`ssh pi@192.168.0.108`  

**Fixes an issue with locales on vanilla Raspbian Jessie**  
`sudo locale-gen en_US en_US.UTF-8 && sudo dpkg-reconfigure locales`  

`mkdir .ssh && cd .ssh && touch authorized_keys && chmod 600 authorized_keys && nano authorized_keys`

**On host machine:**  
`cat .ssh/id_rsa.pub`  
**Paste into authorized_keys**

`sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade && sudo apt-get autoremove`

`sudo raspi-config`  
**Expand filesystem**  
**Change user password**  
**Reboot if it doesn't automatically do so**  

`sudo apt-get -y install git youtube-dl omxplayer tcpdump python-scapy python-setuptools`

**If needed:**  
`sudo apt-get install tcpreplay wireshark`

`git clone https://github.com/jessemillar/yoga-button.git && cd yoga-button && mkdir videos && mkdir dependencies && cd dependencies && git clone https://github.com/willprice/python-omxplayer-wrapper.git && sudo python python-omxplayer-wrapper/setup.py install && cd .. && youtube-dl https://www.youtube.com/watch?v=X0c7shiwTUg --output "yoga.%(ext)s"`

# Todo
- CEC ability
- Video scheduler interface
- Make sure the video player quits after a video finishes
