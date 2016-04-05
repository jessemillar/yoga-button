# Installation
**[Ubuntu Mate](https://ubuntu-mate.org/raspberry-pi/)**  

`ssh pi@192.168.0.108`  

`mkdir .ssh && cd .ssh && touch authorized_keys && chmod 600 authorized_keys && nano authorized_keys`  

**On host machine:**  
`cat .ssh/id_rsa.pub`  
**Paste into authorized_keys**  

**Re-size file system**  
`sudo fdisk /dev/mmcblk0`  
**Delete the second partition (d, 2), then re-create it using the defaults (n, p, 2, enter, enter), then write and exit (w)**
**Reboot the system, then:**  
`sudo resize2fs /dev/mmcblk0p2`  

`sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade && sudo apt-get autoremove`  

Follow Raspberry Pi instructions [here](https://github.com/Pulse-Eight/libcec).  

`sudo apt-get -y install python-scapy python-setuptools python-dbus && sudo pip install psutil && git clone https://github.com/jessemillar/yoga-button.git && cd yoga-button && chmod 755 start.sh && && youtube-dl https://www.youtube.com/watch?v=0Xdof3DtZuk --output "yoga.%(ext)s" --recode-video mkv && cd .. && sudo python sniffer.py`  



# Todo
- CEC ability
- Video scheduler interface
- Make sure the video player quits after a video finishes
