#!/usr/bin/env python3
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
	if(GPIO.input(24)==1):
		LEDon = GPIO.output(17, 1)
	if(GPIO.input(24)==0):
		LEDoff = GPIO.output(17,0)
GPIO.cleanup()
