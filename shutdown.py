# Lets run this script to shut down the pi
import RPi.GPIO as GPIO
import time
import os

# setup the pi to do somet things
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# define method to run when the event fires
def Shutdown(channel):
   os.system("sudo shutdown -h now")
# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(5, GPIO.FALLING, callback = Shutdown, bouncetime = 500)
# Now wait!
while True:
   time.sleep(0.01)
