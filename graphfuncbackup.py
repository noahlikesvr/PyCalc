import numpy as np
import sympy as sp
import PySimpleGUI as sg
import turtle
import os

def clear():
    os.system('cls')

clear()

# Define the initial function
x = sp.symbols('x')
f = -sp.Abs(x+3) - 6

# Create the PySimpleGUI window
layout = [
    [sg.Text('f(x) = '), sg.InputText('', key='function')],
    [sg.Button('Graph'), sg.Button('Exit')]
]
window = sg.Window('Graphing Calculator', layout)

running = True

while running:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        clear()
        window.close()
        exit()

    # Parse the function input and create a sympy expression
    try:
        f = sp.sympify(values['function'])
    except sp.SympifyError:
        sg.popup_error('Invalid function')
        continue

    # Define the x values to plot
    x_vals = np.linspace(-10, 10, 1000)

    # Evaluate f(x) for each x value
    y_vals = [sp.N(f.subs(x, i)) for i in x_vals]

    # Set up the turtle window
    graph_window = turtle.Screen()
    canvas = graph_window.getcanvas()  # or, equivalently: turtle.getcanvas()
    root = canvas.winfo_toplevel()
    graph_window.setup(800, 600)

    global llx
    global lly
    global urx
    global ury

    # update = 

    llx = -10
    lly = -10
    urx = 10
    ury = 10

    
    graph_window.setworldcoordinates(llx, lly, urx, ury)

    # Create a turtle to draw the graph and coordinates
    graph = turtle.Turtle()
    graph.speed(9)
    graph.penup()

    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Create a button to close the window
    close_button = turtle.Turtle()
    close_button.shape('square')
    close_button.shapesize(1.5, 1.5)
    close_button.color('red')
    close_button.penup()
    close_button.goto(-9, 9)
    close_button.onclick(lambda x, y: on_close())

    # Draw the x-axis line with coordinate labels
    graph.goto(-10, 0)
    graph.pendown()
    graph.goto(10, 0)
    for i in range(-10, 11):
        if i != 0:
            graph.goto(i, 0)
            graph.pendown()
            graph.goto(i, 0.2)
            graph.penup()
            graph.goto(i, -0.5)
            graph.write(str(i), align='center', font=("Arial", 8, "normal"))
    graph.penup()

    # Draw the y-axis line with coordinate labels
    graph.goto(0, -10)
    graph.pendown()
    graph.goto(0, 10)
    for i in range(-10, 11):
        if i != 0:
            graph.goto(0, i)
            graph.pendown()
            graph.goto(0.2, i)
            graph.penup()
            graph.goto(-0.5, i)
            graph.write(str(i), align='center', font=("Arial", 8, "normal"))
    graph.penup()

    # Plot the function f(x)
    graph.goto(x_vals[0], y_vals[0])
    graph.pendown()
    for i in range(1, len(x_vals)):
        graph.goto(x_vals[i], y_vals[i])

    # Add axis labels
    graph.penup()
    graph.goto(10.5, 0)
    graph.write('x', align='center', font=("Arial", 12, "bold"))
    graph.goto(0, 10.5)
    graph.write('y', align='center', font=("Arial", 12, "bold"))

    # Keep the graph window open until the user closes it
    sg.popup('Graphing Complete')

    clear()

    graph_window.mainloop()

clear()