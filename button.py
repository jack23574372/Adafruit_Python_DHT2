#!/usr/bin/env python3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(26, GPIO.BOTH)
def my_callback():
    GPIO.output(22, GPIO.input(26))
GPIO.add_event_callback(26, my_callback)
