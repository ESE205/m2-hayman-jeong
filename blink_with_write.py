import RPi.GPIO as GPIO
import time
from time import sleep
import argparse
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

BLINK_DELAY = 1

switch_pin = 12
led_pin = 11
is_on = False
next_blink = 0
nitr = 0

GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

parser = argparse.ArgumentParser()
parser.add_argument("--time", default=100)
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

DEBUG = args.debug

init = time.time()
finish = init + int(args.time)

while time.time() < finish:
	is_blinking = GPIO.input(switch_pin)

	if is_blinking and time.time() > next_blink:
		is_on = not is_on
		GPIO.output(led_pin, GPIO.HIGH if is_on else GPIO.LOW)

		next_blink = time.time() + BLINK_DELAY

		with open("out.txt", "a") as f:
			f.write(f"{time.time()-init}\t{'on' if is_on else 'off'}")

		if DEBUG:
			print(f"time: {time.time()-init}\tnitr: {nitr}\tstate: {'on' if is_on else 'off'}")
	elif time.time() > next_blink:
		GPIO.output(led_pin, GPIO.LOW)

	nitr += 1

if DEBUG:
	print("Program terminated")

GPIO.cleanup()
