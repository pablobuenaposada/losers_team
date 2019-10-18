#!/bin/python
 
import random
import RPi.GPIO as GPIO
from time import sleep

class ServoGame:

    def __init__():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        p = GPIO.PWM(4, 50)
        p.start(6)

    def run_game(self):
        max_val = 15.50
        min_val = 2.70
        middle = 7.60
        pin = 7.60
        offset = 0.10

        self.p.ChangeDutyCycle(middle)
        sleep(3)

        try:
          while True:
            if GPIO.input(18) == False:
                pin = pin + 0.1
            if GPIO.input(16) == False:
                pin = pin - 0.1
            random_pin_min = pin-offset
            random_pin_max = pin+offset
            if random_pin_min < min_val:
                random_pin_min = min_val
            if random_pin_max > max_val:
                random_pin_max = max_val
            if pin > middle:
                pin = random.uniform(pin, random_pin_max)
            else:
            pin = random.uniform(random_pin_min, pin)


            self.p.ChangeDutyCycle(pin)
            sleep(0.051)
         
        except KeyboardInterrupt:  
          self.p.stop()
          GPIO.cleanup()
