from guizero import App, PushButton, Text, TextBox
import RPi.GPIO as GPIO
import time
import os

isLoop = False
isLoopTwo = False

def openFile():
    codeText.clear()
    print("WRITING")
    #file = open("program.py", "w")
    file.write("import RPi.GPIO as GPIO\n")
    file.write("import time\n")
    file.write("GPIO.setmode(GPIO.BOARD)\n")
    file.write("GPIO.setup(12, GPIO.OUT)\n")


def run():
    codeText.clear()
    codeText.append("Running Your Program!  Look at the Board!")
    file.write("GPIO.cleanup()\n")
    file.close()
    print("RUNNING")
    os.system("python ./program.py")
    print("RAN")

def lightOn():
    if isLoop:
        file.write("\tGPIO.output(12, GPIO.HIGH)\n")
        codeText.append("\tTurn Light On\n")
    elif isLoopTwo:
        file.write("\t\tGPIO.output(12, GPIO.HIGH)\n")
        codeText.append("\t\tTurn Light On\n")
    else:
        file.write("GPIO.output(12, GPIO.HIGH)\n")
        codeText.append("Turn Light On\n")

def lightOff():
    if isLoop:
        file.write("\tGPIO.output(12, GPIO.LOW)\n")
        codeText.append("\tTurn Light Off\n")
    elif isLoopTwo:
        file.write("\t\tGPIO.output(12, GPIO.LOW)\n")
        codeText.append( "\t\tTurn Light Off\n")     
    else:
        file.write("GPIO.output(12, GPIO.LOW)\n")
        codeText.append("Turn Light Off\n")

def lightSleep():
    global txt
    if isLoop:
        file.write("\ttime.sleep(" + txt + ")\n")
        codeText.append("\tWait " + txt + " seconds\n")
    elif isLoopTwo:
        file.write("\t\ttime.sleep(" + txt + ")\n")
        codeText.append("\t\tWait " + txt + " seconds\n")
    else:
        file.write("time.sleep(" + txt + ")\n")
        codeText.append("Wait " + txt + " seconds\n")
                        

def looping():
##    window = Tk()
##    User_input = Entry()
##    User_input.pack()
##    window.mainLoop()
##    user_number = User_input.get()
##    print(user_number)
##    forTextBox.enabled = True
##    time.sleep(10)
##    x = forTextBox.get()
    global txt
    print(txt)
    if isLoop:
        file.write("\tfor x in range(0," + txt + "):\n")
        global isLoopTwo
        isLoopTwo = True
        codeText.append("\tDo this " + txt + " times:\n")
    else:
        file.write("for x in range(0," + txt + "):\n")
        global isLoop
        isLoop = True
        codeText.append("Do this " + txt + " times:\n")

def endLooping():
    if isLoopTwo:
        global isLoopTwo
        isLoopTwo = False
    if isLoop:
        global isLoop
        isLoop = False

def goLooping():
    forTextBox.visible = True
    submitButton.visible = True
    global wantLoop
    wantLoop = True

def submitText():
    global txt
    global wantTime
    global wantLoop
    txt = forTextBox.get()
    if int(txt) > 5:
        txt = "5"
    submitButton.visible = False
    forTextBox.visible = False
    if wantLoop:
        wantLoop = False
        looping()
    if wantTime:
        wantTime = False
        lightSleep()

def goSleep():
    forTextBox.visible = True
    submitButton.visible = True
    global wantTime
    wantTime = True

app = App(title = "Science Rendezvous May 2018")
file = open("program.py","w")

txt = ""
wantLoop = False
wantTime = False
#writeButton = PushButton(app, command = write, text = "Write File")

startButton = PushButton(app, command = openFile, text = "Start Program")
lightOnButton = PushButton(app, command = lightOn, text = "Turn Light On")
lightOffButton = PushButton(app, command = lightOff, text = "Turn Light Off")
lightSleepButton = PushButton(app, command = goSleep, text = "Wait")
startLoopButton = PushButton(app, command = goLooping, text = "Start For Loop")
endLoopButton = PushButton(app, command = endLooping, text = "End For Loop")
runButton = PushButton(app, command = run, text = "Run Program")
forTextBox = TextBox(app, visible = False)
submitButton = PushButton(app, command = submitText, text = "Submit", visible = False)
codeText = Text(app, text = "Press Start Program To Begin")
app.display()
