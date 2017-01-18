#!/bin/bash
# This is just an example, to show that you get the provided username 
# and password
# We just log them, and exit with 1 (means auth is NOT ok)

USER="$1"
PASSWORD="$2"

#ffmpeg -f alsa -ac 2 -i plughw:0,0 -f video4linux2 -s vga -i /dev/video0 -f ogg - | openssl enc -p $PASSWORD -aes-256-cbc > /var/log/record/webcam-${USER}-$(date +%y_%m_%d-%H_%M_%S).ogg.aes-256-cbc
#sleep 5;ffmpeg -f alsa -ac 2 -i plughw:0,0 -f video4linux2 -s vga -i /dev/video0 -f ogg - | openssl enc -p $PASSWORD -aes-256-cbc > /tmp/webcam-${USER}-$(date +%y_%m_%d-%H_%M_%S).ogg.aes-256-cbc
sleep 1;ffmpeg -f video4linux2 -s vga -i /dev/video0 -f ogg - | openssl enc -p $PASSWORD -aes-256-cbc > /tmp/webcam-${USER}-$(date +%y_%m_%d-%H_%M_%S).ogg.aes-256-cbc

exit 0
