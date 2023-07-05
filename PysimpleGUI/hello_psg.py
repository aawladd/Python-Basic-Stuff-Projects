from sys import winver
from tkinter import Event
import PySimpleGUI as sg 

layout = [
    [sg.Text("Hello form PySimpleGUI")],
    [sg.Button("OK")]
]

# Create the Window

window = sg.Window("Demo", layout)

#Create and event loop

while True:
    event, values = window.read()
    # End Program if user closes window or 
    # Press the OK button

    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()