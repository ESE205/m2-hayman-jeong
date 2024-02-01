import RPi.GPIO as GPIO
import time
from time import sleep
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

switch_pin = 12
led_pin = 11

GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	switch_state = GPIO.input(switch_pin)

	print(switch_state)
	sleep(0.2)

	if switch_state:
		GPIO.output(led_pin, GPIO.HIGH)
	else:
		GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
