"""Sniff the network for our Dash Button's ARP request and then start a yoga video"""
from __future__ import unicode_literals

import os
import psutil
import time
import youtube_dl

from scapy.all import *


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
            print "Deleting previous video"
            os.remove("/home/stephanie/Documents/yoga-button/yoga.mkv")

def video_exists():
    print "Checking if next video exists"

    if os.path.isfile("/home/stephanie/Documents/yoga-button/yoga.mkv"):
        print "Next video exists"
        return True
    else:
        print "Video doesn't exist--downloading next video in queue"
        download_next()
        return False

def download_next():
    """Download the next YouTube video in the queue"""
    with open('/home/stephanie/Documents/yoga-button/scheduler/schedule.txt', 'r') as f:
        next_video = f.readline().strip()

    print "Downloading next video: " + next_video

    ydl_opts = {
        "recodevideo": "mkv",
        "outtmpl": "/home/stephanie/Documents/yoga-button/yoga.%(ext)s"
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([next_video])

    print "Next video downloaded"

    print "Updating queue"

    with open('/home/stephanie/Documents/yoga-button/scheduler/schedule.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('/home/stephanie/Documents/yoga-button/scheduler/schedule.txt', 'w') as fout:
        fout.writelines(data[1:])

    print "Queue updated"

def arp_display(pkt):
    """Where the magic happens"""
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:9a:ce:38': # Smart Water
                print "Pushed Yoga Button"

                if not playing() and video_exists(): # Check that a video is not currently playing and that the video file exists
                    print "Turning on TV"
                    os.system("echo 'on 0' | cec-client -s -d 1") # Turn on the TV
                    print "Waiting for TV"
                    time.sleep(5)
                    print "Playing video"
                    cmd = "omxplayer /home/stephanie/Documents/yoga-button/yoga.mkv"
                    subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                elif video_exists():
                    kill_with_fire()
                    download_next()
                    print "Turning off TV"
                    os.system("echo 'standby 0' | cec-client -s -d 1") # Turn on the TV
            else:
                print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0) # count=0 means to sniff forever
