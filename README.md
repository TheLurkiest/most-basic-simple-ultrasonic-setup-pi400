# most-basic-simple-ultrasonic-setup-pi400

# ...just for reference-- i THINK this code works, but havent really tested it in a while

# ...just make sure you've used pip/pip3 to install RPi.GPIO or whatever through the terminal, and then you can just run the code through the terminal with a command like:

python3 basicWorkingUltraSonicTest2.py

# there's mentions of a 'button' in the code, but any method of connecting/disconnecting the circuit between whatever pin you assign to button (GPIO 19 by default to start with) and any ground pin will function as a 'button' (for instance just touching a wire hooked up to GPIO 19 to any ground pin)

# ...and I know there's a mention of an 'led' variable, but I honestly don't remember of this most basic version of this code even includes what's needed to make that work at lighting up an LED or not, so I think it's probably ok to just ignore that

# --------------------------------------------------

# the .png image file has been modified so that it matches the code (in terms of which wires connect to which GPIO # pins) but obviously any connections that go to "Ground" work just as well when connected to any other pins labeled "Ground" and any GPIO number pins can be connected to instead of the ones shown in that .png file so long as the variables for GPIO pin numbers assigned within the 'basicWorkingUltraSonicTest2.py' file are ALSO changed (i.e. 'SR04_trigger_pin = 20', 'SR04_echo_pin = 21', 'button = 19')

# ...and just to note; although the .png image file shows the jumper cables connecting directly to the raspberry pi itself, it's probably much easier to just attach everything through the breakout board / ribbon cable (since all of the GPIO numbers are clearly labeled on the breakout board)
