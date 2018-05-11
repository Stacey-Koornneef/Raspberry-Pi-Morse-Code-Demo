'''
Author: Stacey Koornneef
Last Modified May 11, 2018
'''

from guizero import App, PushButton, Text, TextBox
import RPi.GPIO as GPIO
import time
import os

isLoop = False
isLoopTwo = False

'''
This function is run when the Start Program button is pressed.  It starts
    the program that is being written by the user.  It opens the file
    and writes the lines that import necessary libraries and sets up the
    GPIO board on the Raspberry Pi
'''
def openFile():
    codeText.clear()
    print("WRITING")
    file.write("import RPi.GPIO as GPIO\n")
    file.write("import time\n")
    file.write("GPIO.setmode(GPIO.BOARD)\n")
    file.write("GPIO.setup(12, GPIO.OUT)\n")


'''
This function is run when the Run button is pressed.  It writes the lines of
    code that closes the GPIO connection, then closes the file itself.  It
    then runs the program by connecting to the operating system.
'''
def run():
    codeText.clear()
    codeText.append("Finished")
    file.write("GPIO.cleanup()\n")
    file.close()
    print("RUNNING")
    os.system("python ./program.py")
    print("RAN")

'''
This function is run when the Turn Light On button is pressed.  It writes the
    code to the program that will turn the LED on and it writes pseudo code
    onto the ui for the user
'''
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

'''
This function is run when the Turn Light Off button is pressed.  It writes the
    code to the program that will turn the LED off and it writes pseudo code
    onto the ui for the user
'''
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

'''
This function is run when the Wait button is pressed.  It writes code to the
    program that will cause the program to pause between commands
'''
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
                        
'''
This function is run when the Start For Loop button is pressed.  It writes
    code to the program that will allow it to loop a user-specified amount.
    It also tells the rest of the program how many loops it's in
'''
def looping():
    global txt
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

'''
This function is run when the End For Loop button is pressed.  It tells the
    rest of the program that the loop is done
'''
def endLooping():
    if isLoopTwo:
        global isLoopTwo
        isLoopTwo = False
    if isLoop:
        global isLoop
        isLoop = False

'''
This function is used to tell the submitText function that the submitted
    number is for looping.  It also sets the text box and button
    to visible for the user to see
'''
def goLooping():
    forTextBox.visible = True
    submitButton.visible = True
    global wantLoop
    wantLoop = True

'''
This function is run when either the Wait button or the Start For Loop button
    is pressed.  It takes in a user input and then makes the inpout box and button invisible
    again.  It then sends the input to either looping or sleeping
'''
def submitText():
    global txt
    global wantTime
    global wantLoop
    txt = forTextBox.get()
    if int(txt) > 6:
        txt = "6"
    submitButton.visible = False
    forTextBox.visible = False
    if wantLoop:
        wantLoop = False
        looping()
    if wantTime:
        wantTime = False
        lightSleep()

'''
This function is used to tell the submitText function that the submitted
    number is for sleeping.  It also sets the text box and button
    to visible for the user to see
'''
def goSleep():
    forTextBox.visible = True
    submitButton.visible = True
    global wantTime
    wantTime = True

'''
This creates the visualization
'''
app = App(title = "Visualizing Morse Code with an LED")
file = open("program.py","w")

txt = ""
wantLoop = False
wantTime = False


'''
These are all the buttons seen on the application
'''
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
