from guizero import App, PushButton, Text
import RPi.GPIO as GPIO
import time
import os

def write(filename):
    file = open(filename,"w")

    file.write("import RPi.GPIO as GPIO\n")
    file.write("import time\n")
    file.write("GPIO.setmode(GPIO.BOARD)\n")
    file.write("GPIO.setup(12, GPIO.OUT)\n")
    file.write("GPIO.output(12, GPIO.HIGH)\n")
    file.write("time.sleep(1)\n")
    file.write("GPIO.output(12, GPIO.LOW)\n")
    file.close()

def run(filename):
    os.system("python ./"+filename)


filename = "program.py"
write(filename)
run(filename)
print("DONE")
