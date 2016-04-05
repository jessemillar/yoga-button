"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
import os
import psutil
import time

from scapy.all import *


player = "" # A holder variable for reasons
downloader = "" # Another holder

def playing():
    """Check if the video player is currently running"""
    print "Checking for currently-playing video"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "omxplayer.bin":
            print "Currently-playing video found"
            return True

    print "No currently-playing video"
    return False

def kill_with_fire():
    """Kill the video player"""
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == "omxplayer.bin":
            print "Terminating video player"
            proc.kill()

def download_next():
    """Download the next YouTube video in the queue"""
    with open('/home/stephanie/Documents/yoga-button/scheduler/schedule.txt', 'r') as f:
        next_video = f.readline().strip()

    print "Downloading next video: " + next_video

    os.remove("/home/stephanie/Documents/yoga-button/yoga.mkv")
    cmd = "youtube-dl " + next_video + " --output '/home/stephanie/Documents/yoga-button/yoga.%(ext)s' --recode-video mkv"
    downloader = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)

def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"

                if not playing():
                    print "Turning on TV"
                    os.system("echo 'on 0' | cec-client -s -d 1") # Turn on the TV
                    print "Waiting for TV"
                    time.sleep(8)
                    print "Playing video"
                    cmd = "omxplayer /home/stephanie/Documents/yoga-button/videos/yoga.mkv"
                    player = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                else:
                    kill_with_fire()
                    download_next()
                    print "Turning off TV"
                    os.system("echo 'standby 0' | cec-client -s -d 1") # Turn on the TV
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
