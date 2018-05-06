from guizero import App, PushButton, Text
import RPi.GPIO as GPIO
import time
import os

def openFile():
    print("WRITING")
    #file = open("program.py", "w")
    file.write("import RPi.GPIO as GPIO\n")
    file.write("import time\n")
    file.write("GPIO.setmode(GPIO.BOARD)\n")
    file.write("GPIO.setup(12, GPIO.OUT)\n")
    file.write("GPIO.output(12, GPIO.HIGH)\n")
    file.write("time.sleep(1)\n")
    file.write("GPIO.output(12, GPIO.LOW)\n")
    print("WRITTEN")

def run():
    file.write("GPIO.cleanup()\n")
    file.close()
    print("RUNNING")
    os.system("python ./program.py")
    print("RAN")




app = App(title = "Science Rendezvous May 2018")
file = open("program.py","w")
#writeButton = PushButton(app, command = write, text = "Write File")
runButton = PushButton(app, command = run, text = "Run Program")
startButton = PushButton(app, command = openFile, text = "Start New Program")
app.display()
