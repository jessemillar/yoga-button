"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os
import subprocess

from omxplayer import OMXPlayer
from scapy.all import *


def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1:  # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38':  # Smart Water
                print "Pushed Yoga Button"
                player.play_pause()
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

player = OMXPlayer('yoga.mp4')
print sniff(prn=arp_display, filter="arp", store=0, count=0)
