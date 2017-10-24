#!/usr/bin/env python3


import ev3dev.ev3 as ev3
from time import sleep

def chksum(n):
    return 7-((n+(n>>2)+(n>>4))&7)

MS_FWD  = 0
MS_REV  = 1
MS_STOP = 2

CP_C      = 99
CP_CSHARP = 100
CP_D      = 101
CP_DSHARP = 102
CP_E      = 103
CP_F      = 104
CP_FSHARP = 105
CP_G      = 106
CP_GSHARP = 107
CP_A      = 108
CP_ASHARP = 109
CP_B      = 110
CP_C_HI   = 111

PAUSE = 0.15

def vll1():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(0.02)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    sleep(0.04)

def vll0():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(0.04)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    sleep(0.02)

def vllinit():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(0.4)    

def vllstart():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    sleep(0.02)

def vllstop():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(0.02)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    sleep(0.06)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
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

def cp_pause():
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    sleep(PAUSE)

def play_tones():
    # only for CodePilot
    send(CP_C)
    cp_pause()
    send(CP_CSHARP)
    cp_pause()
    send(CP_D)
    cp_pause()
    send(CP_DSHARP)
    cp_pause()
    send(CP_E)
    cp_pause()
    send(CP_F)
    cp_pause()
    send(CP_FSHARP)
    cp_pause()
    send(CP_G)
    cp_pause()
    send(CP_GSHARP)
    cp_pause()
    send(CP_A)
    cp_pause()
    send(CP_ASHARP)
    cp_pause()
    send(CP_B)
    cp_pause()
    send(CP_C_HI)
    cp_pause()

ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)

vllinit()
sleep(2)
while True:
    send(MS_FWD)
    send(MS_REV)
    #play_tones()
