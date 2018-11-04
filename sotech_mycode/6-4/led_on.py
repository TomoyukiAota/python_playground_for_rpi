#! /user/bin/env python3.6

import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

GPIO.output(4, GPIO.HIGH)     # turn LED on
# GPIO.output(4, GPIO.LOW)    # turn LED off