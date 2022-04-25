# Imports------------------------------------------------------------------------

import PySimpleGUI as sg
import random
import os

# Score-&-random-num-------------------------------------------------------------

score = 45
ans = random.randint(1, 10)

# Setup--------------------------------------------------------------------------

layout = [
    [sg.Text("Number Guesser!", size=(13, 1))],
    [sg.Text("Score:"), sg.Text(str(score), key="-SCORE-")],
    [sg.Button("1"), sg.Button("2"), sg.Button("3")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6")],
    [sg.Button("7"), sg.Button("8"), sg.Button("9")],
    [sg.Text("Start Guessing!", size=(13, 3), key="-RESULT-")]
]

window = sg.Window('', layout)

# Logic--------------------------------------------------------------------------

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == str(ans):
        score = score + 25
        window["-SCORE-"].update(str(score))
        window["-RESULT-"].update("YAY!                You guessed it!!")
        ans = random.randint(1, 10)

    else:
        score = score - 5
        window["-SCORE-"].update(str(score))
        window["-RESULT-"].update("No.               That's not it...")

    if score <= 0:
        sg.popup("Your score reached zero! You loose! :(", title="Oh No!")
        break

window.close()
