import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import os as cmd

cmd.system('cls')

# Get user input for the equation type
layout = [[sg.Text("Enter the equation type (sine or cosine):")],
          [sg.InputText()],
          [sg.Button('OK', key='enter')]]

window = sg.Window('Equation Grapher').Layout(layout)
event, values = window.Read()
equation_type = values[0].lower()

# Get user input for the number
layout = [[sg.Text("Enter the number you want to find the {} of:".format(equation_type))],
          [sg.InputText()],
          [sg.Button('OK', key='enter')]]

window = sg.Window('Number input').Layout(layout)
event, values = window.Read()

try:
    number = float(values[0])
except ValueError:
    sg.Popup("Invalid number entered. Please enter a valid number.")
    cmd.system('python3 sincosinbackup.py')
    exit()
    
# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 100)

if equation_type == "sine":
    # Generate y values for sine
    y = np.sin(number*x)
    equation = "y = sin({}x)".format(number)
elif equation_type == "cosine":
    # Generate y values for cosine
    y = np.cos(number*x)
    equation = "y = cos({}x)".format(number)
else:
    sg.Popup("Invalid equation type entered. Please enter either 'sine' or 'cosine'.")
    exit()

# Use matplotlib to display the graph
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title(equation)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.grid(False)
plt.show()
