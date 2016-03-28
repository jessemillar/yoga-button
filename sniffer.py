"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os

from omxplayer import OMXPlayer
from scapy.all import *


def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"
                os.system("echo 'on 0' | cec-client -s") # Turn on the TV

                if player.is_playing():
                    player.quit()
                else:
                    player.play()
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

player = OMXPlayer('videos/yoga.m4a')
print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
