"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os
import psutil
import time

from scapy.all import *


def is_playing():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "omxplayer.bin":
            return True

    return False

def kill_with_fire():
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "omxplayer.bin":
            proc.kill()

def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"

                if not is_playing():
                    os.system("omxplayer /home/stephanie/Documents/yoga-button/videos/yoga.mkv")
                    # player.quit()
                    # os.system("echo 'standby 0' | cec-client -s -d 1") # Turn on the TV
                else:
                    kill_with_fire()
                    # os.system("echo 'on 0' | cec-client -s -d 1") # Turn on the TV
                    # time.sleep(8)
                    # player.play()
                    # os.system("killall omxplayer.bin")
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

# player = OMXPlayer('/home/stephanie/Documents/yoga-button/videos/yoga.mkv')
print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
