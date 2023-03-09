import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import sympy

def clear():
    os.system('cls')

clear()

layout = [
    [sg.Text('f(x) = '), sg.Input('')],
    [sg.Button('Done'), sg.Button('Cancel')]
]

window = sg.Window('Function Grapher', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    # Parse the input string 
    expr = sympy.sympify(values[0].strip())

    # Create two ranges of x-values
    x_values_1 = np.linspace(-10, 0, 100)
    x_values_2 = np.linspace(10, 0, 100)

    # Evaluate the expression at each x-value
    y_values_1 = [expr.evalf(subs={'x': x}) for x in x_values_1]
    y_values_2 = [expr.evalf(subs={'x': x}) for x in x_values_2]

    # Plot the results
    mpl.pyplot.ioff()
    fig, ax = plt.subplots()
    ax.plot(x_values_1, y_values_1)
    ax.plot(x_values_2, y_values_2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_tick_params(labelsize=8, pad=2)
    ax.yaxis.set_tick_params(which='major', labelsize=8, pad=10)
    ax.xaxis.set_ticks(np.arange(-10, 11, 1))
    ax.yaxis.set_ticks(np.arange(-10, 11, 0.5))
    fig.set_size_inches(8, 6)
    plt.show()

clear()
window.close()