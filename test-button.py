# This script will change the lights, yay
import RPi.GPIO as GPIO
import time
import os

# north_blue: 23,
# north_green: 12,
# north_yellow: 16,
# north_red: 20,
# south_blue: 22,
# south_green: 6,
# south_yellow: 13,
# south_red: 26,

# setup the pi to do some things
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# define method to run when the event fires
right = True
left = False
def Shutdown(channel):
    print 'BUTTON HAS BEEN PRESSED'
    # GPIO.output(23, right)
    # GPIO.output(12, right)
    # GPIO.output(16, right)
    # GPIO.output(20, right)
    # GPIO.output(22, left)
    # GPIO.output(6, left)
    # GPIO.output(13, left)
    # GPIO.output(26, left)
    # right = not right
    # left = not left
# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(5, GPIO.FALLING, callback = Shutdown, bouncetime = 500)
# Now wait!
while True:
   time.sleep(0.01)

# message = input("Press enter to quit\n\n") # Run until someone presses enter
