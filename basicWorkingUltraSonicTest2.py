# all the wiring here is pretty self explanatory, just look at the GPIO 
# numbers on pin diagrams for the pi to see which numbers match the ones
# here in the code.  The one thing to mention not already made obvious by just
# looking at the numbers in the code here, is that 'echo' on the ultrasonic
# sensor connects via a 1k ohm resistor to GPIO 21-- and that a 2k ohm resistor
# forms an alternate path AFTER the 1k ohm resistor, connecting back to ground
# as an alternative to connecting back up to GPIO 21

#import all of the libraries here 
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#set mode for GPIO
GPIO.setmode(GPIO.BCM)

# Ultrasonic pin assignments
SR04_trigger_pin = 20
SR04_echo_pin = 21

# Set up the SR04 pins
GPIO.setup(SR04_trigger_pin, GPIO.OUT)
GPIO.setup(SR04_echo_pin, GPIO.IN)
GPIO.output(SR04_trigger_pin, GPIO.LOW)

#create variable for button
button = 19
#setup button as input
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Remember what the button was so we can see if it changed
prevButton = GPIO.input(button)
prevPressTime = time.time()
nextDist = time.time() - 1

def distance(metric):
        # set Trigger to HIGH
        GPIO.output(SR04_trigger_pin, GPIO.HIGH)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(SR04_trigger_pin, GPIO.LOW)

        startTime = time.time()
        stopTime = time.time()

        # Get the returnb pulse start time
        while 0 == GPIO.input(SR04_echo_pin):
                startTime = time.time()

        # Get the pulse length
        while 1 == GPIO.input(SR04_echo_pin):
                stopTime = time.time()

        elapsedTime = stopTime - startTime
        # The speed of sound is 33120 cm/S or 13039.37 inch/sec.
        # Divide by 2 since this is a round trip
        if (1 == metric):
                d = (elapsedTime * 33120.0) / 2   # metric
        else:
                d = (elapsedTime * 13039.37) / 2   # english

        return d

#wrap our code in a try block for error handling
try:

  #create variables for LEDs and set them to out
  led = 4
  GPIO.setup(led, GPIO.OUT)
  #create a loop that checks for button input
  while True:
    input_state = GPIO.input(button)
    #if button pressed, light up timed LEDs
    if input_state == False:
      print('Button Pressed')
      print('debug test 1')
      if time.time() > nextDist:
        print("Distance=", distance(False))
        d = int(100 * distance(False)) / 100
        m = str(d) + " in."
        print("m=", str(m))
      time.sleep(0.2)
      GPIO.output(led, 1)
      time.sleep(0.5)
    else:
      GPIO.output(led, 0)

#execute this code if CTRL + C is used to kill python script
except KeyboardInterrupt:
  print("You've exited the program")
#execute code inside this block as the program exits
finally:
  GPIO.cleanup()

