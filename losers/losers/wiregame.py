#!/bin/python
 
import random
import RPi.GPIO as GPIO
from time import sleep
 
class WireGame:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def hit_wire(self):
        return not GPIO.input(18)

    def hit_end(self):
        return not GPIO.input(16)

    def cleanup(self):
        GPIO.cleanup()
