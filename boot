import PySimpleGUI as sg
import os
import sys

os.system('cls')

# Get input on where to go
layout = [
    [sg.Text('Where do you want to go?')],
    [sg.Button('Pythagorean Theorem (no click-gui)')],
    [sg.Button('Graph linear algebra')],
    [sg.Button('Graph sine and cosine')],
    [sg.Button('Midpoint and distance')],
    [sg.Button('Calculator interface (beta)')],
    [sg.Button('Function grapher (beta)')],
    [sg.Text()],
    [sg.Button('Exit')]
]

window = sg.Window('Area select', size=(225, 250)).Layout(layout)
event, values = window.Read()

if event == 'Pythagorean Theorem (no click-gui)':
    window.Close()
    os.system('python pythagorean.py')

elif event == 'Graph linear algebra':
    window.Close()
    os.system('python3 linear.py')

elif event == 'Graph sine and cosine':
    window.Close()
    os.system('python3 sincosin.py')

elif event == 'Midpoint and distance':
    window.Close()
    os.system('python3 midpointdistance.py')

elif event == 'Calculator interface (beta)':
    window.Close()
    os.system('python3 mathbasic.py')

elif event == 'Function grapher (beta)':
    window.Close()
    os.system('python3 graphfunc.py')
    
if event == 'Exit':
    window.Close()
    sys.exit()

sys.exit()