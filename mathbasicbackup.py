import PySimpleGUI as sg
import numpy as np
import os
import sys

os.system('cls')

inputbox = 'Input text'
userin = ''
result = 0

layout1 = [
    [sg.Text(inputbox)],
    [sg.Text(result)],
    [sg.Button('('), sg.Button(')'), sg.Button('^')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
    [sg.Button('Clear'), sg.Button('Off')]
]

layout2 = [
    [sg.Button('√'), sg.Button('²'), sg.Button('³')]
]

layout = [
    [sg.TabGroup([[sg.Tab('Numpad', layout1), sg.Tab('Advanced', layout2)]])]
]

window = sg.Window('Calculator Window').Layout(layout)

while True:
    event, values = window.Read()

    if event == sg.WIN_CLOSED or event == 'Off':
        window.close()
        sys.exit()

    if event == '=':
        if userin.startswith('√'):
            result = np.sqrt(float(userin.replace('√', '')))
        else:
            try:
                result = eval(userin)
            except:
                result = 'Error'
                userin = str(result)

    elif event != 'TURN OFF' and event != 'Clear' and event != '^':
        userin += event
        inputbox = userin
    elif event == 'Clear':
        userin = ''
        result = 0
        inputbox = 'Input text'

    layout1 = [
        [sg.Text(inputbox)],
        [sg.Text(result)],
        [sg.Button('('), sg.Button(')'), sg.Button('^')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
        [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
        [sg.Button('Clear'), sg.Button('Off')]
    ]

    layout2 = [
        [sg.Button('√'), sg.Button('²'), sg.Button('³')]
    ]

    layout = [
        [sg.TabGroup([[sg.Tab('Numpad', layout1), sg.Tab('Advanced', layout2)]])]
    ]

    window.Close()
    window = sg.Window('Calculator Window').Layout(layout)

window.close()
sys.exit()