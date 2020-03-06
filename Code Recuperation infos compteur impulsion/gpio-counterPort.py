#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import signal
import datetime

#verbose = True     # global variable

############################################################################################################
############################################################################################################

pin = sys.argv[0]

########## Main Loop
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
counter = 0
while True:
    i = 0
    # wait for pin going up
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    while i < 10 and not GPIO.input(pin) :
        time.sleep(0.001)
        i += 1
    if i == 10:
        counter += 1
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        print(date, "    Compteur:", counter, "Wh")
    GPIO.wait_for_edge(pin, GPIO.RISING)
############################################################################################################
############################################################################################################



