#!/usr/bin/env python3

# requires sudo

from pylibftdi import BitBangDevice
from time import sleep

FTDI_SN = 'A105BPAX'      # Serial Number of the FTDI device, see dmesg
DIRECTION = 0xFF          # all output

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
    bb.port = 1
    sleep(0.02)
    bb.port = 0
    sleep(0.04)

def vll0():
    bb.port = 1
    sleep(0.04)
    bb.port = 0
    sleep(0.02)


def vllinit():
    bb.port = 1
    sleep(0.4)    


def vllstart():
    bb.port = 0
    sleep(0.02)

def vllstop():
    bb.port = 1
    sleep(0.02)
    bb.port = 0
    sleep(0.06)
    bb.port = 1
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
     bb.port = 1
     sleep(PAUSE)

# auto_detach = False is needed as a workaround to prevent
# segmentation faults when accessing the FTDI device
# see pylibftdi issue #25

bb = BitBangDevice(FTDI_SN, auto_detach=False)
bb.direction = DIRECTION
bb.port = 0

vllinit()
sleep(2)

while True:
    send(MS_FWD)
    send(MS_REV)



