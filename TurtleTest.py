from turtle import *
from random import randint
import time

sw = 600
sh = 800
s=getscreen()
s.bgcolor('black')
s.setup(600,800)
t=getturtle()
t.color('white')
t.width(6)
t.speed(0)

tWriter = Turtle()
tWriter.hideturtle()
tBadLetters = Turtle()
tBadLetters.hideturtle()

fontS = int(sh*0.035)
displayText = ""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
diplayWord = ""
fails = 6
gameDone = False

sWords = ['zebra', 'gymnastics', 'football', 'innovation', 'python', \
          'aspiration', 'cow tipping', 'young blood', 'orange', \
          'alligator', 'carosel', 'alphabet', 'lets get this bread', \
          'morgan freeman', 'thomas the tank engine']

def makeDisplay():
    global displayWord, secretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters used " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawRLeg()
    if fails == 2:
        drawLLeg()
    if fails == 1:
        drawLArm()
    if fails == 0:
        drawRArm()

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the word."
    guess = s.textinput(boxTitle, "Enter your guess for the word.")
    if guess == secretWord:
        displayText("Correct")
        gameDone = True
    else:
        displayText("Incorrect")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()

def playGame():
    global fails, gameDone, lettersCorrect, lettersWrong, alpha
    while gameDone == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("Incorrect." + theGuess + " only one letter please.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("Incorrect." + theGuess + " not a letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        else:
            displayText("Incorrect. " + theGuess + " is not in the word.")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Incorrect letters: " + lettersWrong)
            displayText(displayWord)
            fails -=1
            updateHangmanPerson()
                        

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sw*0.4), -int(sh*0.4))
    tWriter.pendown()
    tWriter.color('white')
    tWriter.write(newText, font=('Arial', fontS, 'bold'))

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sw*0.4), int(sh*0.4))
    tBadLetters.pendown()
    tBadLetters.color('white')
    tBadLetters.write(newText, font=('Arial', fontS, 'bold'))

def chooseWord():
    global secretWord
    secretWord = sWords[randint(0,len(sWords) -1)]

def drawGallows():
    t.color('white')
    t.penup()
    t.goto(-int(sw*0.25), -int(sh*0.25))
    t.pendown()
    t.forward(int(sw*0.6))
    t.backward(int(sw*0.1))
    t.left(90)
    t.forward(int(sw*0.75))
    t.left(90)
    t.forward(int(sw*0.25))
    t.left(90)
    t.forward(int(sw*0.125))

def drawHead():
    t.color('blue')
    t.right(90)
    t.circle(int(sw*0.0625))
    t.penup()
    t.left(90)
    t.forward(int(sw*0.125))
    t.pendown()

def drawTorso():
    t.color('blue')
    t.forward(int(sh*0.2))

def drawRLeg():
    t.color('blue')
    t.left(35)
    t.forward(int(sw*0.125))
    t.backward(int(sw*0.125))
    t.right(35)

def drawLLeg():
    t.color('blue')
    t.right(35)
    t.forward(int(sw*0.125))
    t.backward(int(sw*0.125))
    t.left(215)
    t.forward(int(sh*0.15))

def drawLArm():
    t.color('blue')
    t.right(120)
    t.forward(int(sw*0.125))
    t.backward(int(sw*0.125))
    t.right(60)

def drawRArm():
    t.color('blue')
    t.left(300)
    t.forward(int(sw*0.125))
    t.backward(int(sw*0.125))
    t.left(60)

drawGallows()
drawHead()
drawTorso()
drawRLeg()
drawLLeg()
drawLArm()
drawRArm()

#GAME BEGIN

time.sleep(1)
t.clear()
t.left(90)
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Incorrect letters:" + lettersWrong)
playGame()
