#!/usr/bin/env python3
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
i=0
while True:
	while i<10:
		i+=1
		LEDon = GPIO.output(26, 1)
		time.sleep(0.5)
		LEDoff = GPIO.output(26,0)   
		time.sleep(0.5)
