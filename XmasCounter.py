# Import tools to underline text
from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text, HTML

# Import the GUI tools
import PySimpleGUI as sg

# Get today's day and make it a number
from datetime import date
today = date.today().day

# Find the number of days until Christmas
daysLeft = 24 - today
daysLeft = str(daysLeft)

# Underline the number of days until Christmas
prompt = "There are <u>" + daysLeft + "</u> days left until Christmas! 🎅"

layout = [[sg.Text(
    "There are " + daysLeft + " days left until Christmas!",
    font=("Helvetica", 13, "underline"),
    size=(30, 5)
)]],

if daysLeft == "0":
    window = sg.Window(
        "It's Christmas! 🎅",
        layout,
        size=(200, 0)
    )
else:
    window = sg.Window(
        "There are " + daysLeft + " days left until Christmas! 🎅",
        layout,
        size=(350, 0)
    )

event, values = window.read()
window.close()

# Print the number of days until Christmas
print_formatted_text(HTML(prompt))

