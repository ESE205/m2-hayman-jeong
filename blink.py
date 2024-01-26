import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
import sys
import argparse
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

parser = argparse.ArgumentParser()
parser.add_argument("--n", default=15)
args = parser.parse_args()

ITER_COUNT = int(args.n)
pin1 = 11

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

while ITER_COUNT > 0: # Run ITER_COUNT times
   ITER_COUNT -= 1 # Decrement counter
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   sleep(1)                     # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   sleep(1)                     # Sleep for 1 second
GPIO.cleanup()
