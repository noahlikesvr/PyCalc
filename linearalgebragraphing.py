import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import os as cmd

cmd.system('cls')

# Get user input for the equation
layout = [[sg.Text("Enter the linear equation (in the form y=mx+b):")],
          [sg.InputText()],
          [sg.Button('OK', key='enter')]]

window = sg.Window('Linear Equation Grapher').Layout(layout)
event, values = window.Read()
equation = values[0]

# Extract the coefficients from the equation
coefficients = equation.split('=')[1].split('x')
m = float(coefficients[0])
b = float(coefficients[1])

# Use numpy to generate x and y values for the linear equation
x = np.linspace(-20, 20, 100)
y = m * x + b

# Use matplotlib to display the graph
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title(equation)
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.grid(False)
plt.show()

cmd.system('cls')