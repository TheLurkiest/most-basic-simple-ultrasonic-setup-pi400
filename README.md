# most-basic-simple-ultrasonic-setup-pi400

# ...just for reference-- i THINK this code works, but havent really tested it in a while

# ...just make sure you've used pip/pip3 to install RPi.GPIO or whatever through the terminal, and then you can just run the code through the terminal with a command like:

python3 basicWorkingUltraSonicTest2.py

# there's mentions of a 'button' in the code, but any method of connecting/disconnecting the circuit between whatever pin you assign to button (GPIO 19 by default to start with) and any ground pin will function as a 'button' (for instance just touching a wire hooked up to GPIO 19 to any ground pin)

# ...and I know there's a mention of an 'led' variable, but I honestly don't remember of this most basic version of this code even includes what's needed to make that work at lighting up an LED or not, so I think it's probably ok to just ignore that
