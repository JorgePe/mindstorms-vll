#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

# Controlling the AT-AT from the 9574 Dark Side Devoloper Kit 
# video: https://youtu.be/tdrDTqwzdbI
#
# do not forget to configure outA as led:
# echo led > /sys/class/lego-port/port4/mode
# you should have this device under
# /sys/class/leds/
#
LED_DEVICE = 'ev3-ports:outA::brick-status'

def chksum(n):
    return 7-((n+(n>>2)+(n>>4))&7)

MS_FWD  = 0
MS_REV  = 1
MS_STOP = 2
MS_BEEP = 4

PAUSE = 0.15

def vll1():
    led.brightness =  100
    sleep(0.02)
    led.brightness = 0
    sleep(0.04)

def vll0():
    led.brightness = 100
    sleep(0.04)
    led.brightness = 0
    sleep(0.02)

def vllinit():
    led.brightness = 100
    sleep(0.4)    

def vllstart():
    led.brightness = 0
    sleep(0.02)

def vllstop():
    led.brightness = 100
    sleep(0.02)
    led.brightness = 0
    sleep(0.06)
    led.brightness = 100
    sleep(0.12)

def send(command):
    vllstart()
    v = (chksum(command) << 7 ) + command
    i = 0x200
    while i>0 :
        if v & i:
            vll1()        
        else:
            vll0()
        i = i >> 1
    vllstop()

def pause():
    led.brightness = 100
    sleep(PAUSE)


led =  ev3.Led(name_pattern=LED_DEVICE)
led.brightness = 0

btn = ev3.Button()

vllinit()
sleep(2)
print("Ready")
send(MS_BEEP)
pause()

while True:
    if btn.left:
        send(MS_REV)
        pause()
    elif btn.right:
        send(MS_FWD)
        pause()
    elif btn.up:
        send(MS_BEEP)
        pause()
