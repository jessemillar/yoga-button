"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os
import time

from omxplayer import OMXPlayer
from scapy.all import *


def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"

                if player.is_playing():
                    player.quit()
                    os.system("echo 'standby 0' | cec-client -s -d 1") # Turn on the TV
                else:
                    os.system("echo 'on 0' | cec-client -s -d 1") # Turn on the TV
                    time.sleep(8)
                    player.play()
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

player = OMXPlayer('videos/yoga.mkv')
print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
