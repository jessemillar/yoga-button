"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os
import psutil
import time

from scapy.all import *


player = ""
cmd = "omxplayer /home/stephanie/Documents/yoga-button/videos/yoga.mkv"

def playing():
    """Check if the video player is currently running"""
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "omxplayer.bin":
            return True

    return False

def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"

                if not playing():
                    # os.system("omxplayer /home/stephanie/Documents/yoga-button/videos/yoga.mkv")
                    player = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                    # os.system("echo 'standby 0' | cec-client -s -d 1") # Turn on the TV
                else:
                    os.killpg(os.getpgid(player.pid), signal.SIGTERM)  # Send the signal to all the process
                    # os.system("echo 'on 0' | cec-client -s -d 1") # Turn on the TV
                    # time.sleep(8)
                    # os.system("killall omxplayer.bin")
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
