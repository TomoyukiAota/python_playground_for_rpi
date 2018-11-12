#! /usr/bin/env python3.6

import time, signal, sys
import Adafruit_ADS1x15

GAIN = 1

adc = Adafruit_ADS1x15.ADS1015()

while True:
    volts = adc.read_adc(0, gain=GAIN) / 500.0

    if volts > 1:
        print("Well Lighted : " + str(volts) + "V")
    else:
        print("Dark : " + str(volts) + "V")
    
    time.sleep(1)