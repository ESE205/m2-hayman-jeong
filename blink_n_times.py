import argparse
import RPi.GPIO as GPIO
import time
import sys

led_pin = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

parser = argparse.ArgumentParser()
parser.add_argument('--n', default=5)
args = parser.parse_args()

DELAY = 1

init = time.time()
last = init
itrs = 0
is_on = False

while itrs < int(args.n):
	if last + DELAY < time.time():
		is_on = not is_on

		if not is_on:
			itrs += 1

		GPIO.output(led_pin, GPIO.HIGH if is_on else GPIO.LOW)
		last = time.time()
