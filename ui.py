from guizero import App, PushButton, Text
import RPi.GPIO as GPIO
import time
import os
from program.py import *

def write(filename):
    file = open(filename,"w")

    file.write("import RPi.GPIO as GPIO\n")
    file.write("import time\n")
    file.write("GPIO.setmode(GPIO.BOARD)\n")
    file.write("GPIO.setup(12, GPIO.OUT)\n")
    file.write("def program():\n")
    file.write("\tGPIO.output(12, GPIO.HIGH)\n")
    file.write("\ttime.sleep(1)\n")
    file.write("\tGPIO.output(12, GPIO.LOW)\n")
    file.close()


filename = "program.py"
write(filename)
program()
print("DONE")
