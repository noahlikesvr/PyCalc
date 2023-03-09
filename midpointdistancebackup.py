import PySimpleGUI as sg
import numpy as np
import os

os.system('cls')

# Choose which we are doing
layout = [
    [sg.Button('Midpoint')],
    [sg.Button('Distance')]
]

window = sg.Window('Midpoint and Distance').Layout(layout)
event, values = window.Read()

if event == 'Midpoint':
    # X
    layout = [
        [sg.Text('Input x₁ and x₂')],
        [sg.Text('x₁: '), sg.Input('')],
        [sg.Text('x₂: '), sg.Input('')],
        [sg.Button('Next')]
    ]

    window = sg.Window('Midpoint reader (x)').Layout(layout)
    event, values = window.Read()

    x1 = float(values[0])
    x2 = float(values[1])

    # Y
    layout = [
        [sg.Text('Input y₁ and y₂')],
        [sg.Text('y₁: '), sg.Input('')],
        [sg.Text('y₂: '), sg.Input('')],
        [sg.Button('Next')]
    ]

    window = sg.Window('Midpoint reader (y)').Layout(layout)
    event, values = window.Read()

    y1 = float(values[0])
    y2 = float(values[1])

    # Math
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    # Popup stuff
    end = 'Midpoint: (' + str(x) + ', ' + str(y) + ')'
    eq = '''\n
       x₁ + x₂   y₁ + y₂
m = ------------ , ------------
            2             2
    '''
    step1 = '(' + str(x1) + '+' + str(x2) + ')' + ' / 2'
    step2 = '(' + str(y1) + '+' + str(y2) + ')' + ' / 2'
    step3 = '(' + str(x) + ')'
    step4 = '(' + str(y) + ')'

    sg.popup(eq + '\n' + step1 + '\n' + step2 + '\n' + step3 + '\n' + step4 + '\n' + end)

elif event == 'Distance':
    # X
    layout = [
        [sg.Text('Input x₁ and x₂')],
        [sg.Text('x₁: '), sg.Input('')],
        [sg.Text('x₂: '), sg.Input('')],
        [sg.Button('Next')]
    ]

    window = sg.Window('Distance reader (x)').Layout(layout)
    event, values = window.Read()

    x1 = float(values[0])
    x2 = float(values[1])

    # Y
    layout = [
        [sg.Text('Input y₁ and y₂')],
        [sg.Text('y₁: '), sg.Input('')],
        [sg.Text('y₂: '), sg.Input('')],
        [sg.Button('Next')]
    ]

    window = sg.Window('Distance reader (y)').Layout(layout)
    event, values = window.Read()

    y1 = float(values[0])
    y2 = float(values[1])

    # Math
    d = np.sqrt(((x2-x1)**2)+((y2-y1)**2))

    # Popup stuff
    eq = '√(x₂-x₁)²+(y₂-y₁)²'
    step0 = '√(' + str(x2) + '-' + str(x1) + ')² + (' + str(y2) + '-' + str(y1) + ')²'
    step1 = '√(' + str(x2 - x1) + ')² + (' + str(y2-y1) + ')²'
    step2 = '√' + str((x2 - x1)**2) + ' + ' + str((y2 - y1)**2)
    step3 = '√' + str((x2 - x1)**2+(y2 - y1)**2)

    sg.popup(eq + '\n' + step0 + '\n' + step1 + '\n' + step2 + '\n' + step3 + '\n' + 'Distance: ' + str(d))