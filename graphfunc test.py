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
    [sg.Text('X Size (optional)'), sg.InputText('', key='coordx')],
    [sg.Text('Y Size (optional)'), sg.InputText('', key='coordy')],
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
    graph_window.setworldcoordinates(-10, -10, 10, 10)

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

    # Create a slider to control the zoom level
    def zoom(x, y):
        graph_window.setworldcoordinates(x, y, x + 10, y + 10)
        graph.clear()

        # Draw the x-axis line with coordinate labels
        graph.goto(x, 0)
        graph.pendown()
        graph.goto(x + 10, 0)
        for i in range(int(x), int(x + 11)):
            if i != 0:
                graph.goto(i, 0)
                graph.pendown()
                graph.goto(i, 0.2)
                graph.penup()
                graph.goto(i, -0.5)
                graph.write(str(i), align='center', font=("Arial", 8, "normal"))
        graph.penup()

        # Draw the y-axis line with coordinate labels
        graph.goto(x, y)
        graph.pendown()
        graph.goto(x, y + 10)
        for i in range(int(y), int(y + 11)):
            if i != 0:
                graph.goto(x, i)
                graph.pendown()
                graph.goto(x + 0.2, i)
                graph.penup()
                graph.goto(x - 0.5, i)
                graph.write(str(i), align='center', font=("Arial", 8, "normal"))
        graph.penup()

        # Plot the function f(x)
        graph.goto(x_vals[0], y_vals[0])
        graph.pendown()
        for i in range(1, len(x_vals)):
            graph.goto(x_vals[i], y_vals[i])

        # Add axis labels
        graph.penup()
        graph.goto(x + 10.5, 0)
        graph.write('x', align='center', font=("Arial", 12, "bold"))
        graph.goto(x, y + 10.5)
        graph.write('y', align='center', font=("Arial", 12, "bold"))

    zoom_slider = turtle.Turtle()
    zoom_slider.shape('square')
    zoom_slider.shapesize(1.5, 1.5)
    zoom_slider.color('green')
    zoom_slider.penup()
    zoom_slider.goto(9, 8.5)
    zoom_slider.onclick(zoom, btn=3)

    # Create a button to reset the zoom level
    def reset_zoom(x, y):
        graph_window.setworldcoordinates(-10, -10, 10, 10)
        graph.clear()

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

    reset_button = turtle.Turtle()
    reset_button.shape('square')
    reset_button.shapesize(1.5, 1.5)
    reset_button.color('blue')
    reset_button.penup()
    reset_button.goto(9, 7.5)
    reset_button.onclick(reset_zoom, btn=3)

    # Keep the graph window open until the user closes it
    sg.popup('Graphing Complete')

    clear()

    graph_window.mainloop()

clear()