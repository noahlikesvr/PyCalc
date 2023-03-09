import math
import os
import time
import keyboard
import turtle

os.system('cls')

# # Globals
# wn = turtle.Screen()
# wn.bgcolor('white')
# wn.title('Pytha - Triangles!')

# STARTUP
def startup():

    os.system('cls')

    # Ask for input
    print('Solve for leg or hypotenuse?')
    ask = input('>>> ')
    if ask == 'leg':
        leg()
    elif ask == 'hypotenuse':
        hypotenuse()
    else:
        print('Invalid!')
        time.sleep(1)
        startup()

# Solves for hypotenuse
def hypotenuse():

    os.system('cls')

    # User input
    print('What is the length of your first leg?')
    a = float(input('>>> '))
    os.system('cls')
    print('What is the length of your second leg?')
    b = float(input('>>> '))
    os.system('cls')

    # Math
    asqr = int(a**2)
    bsqr = int(b**2)
    csqr = asqr + bsqr
    c = math.sqrt(asqr + bsqr)

    # # Calculate the angle opposite side a
    # angle = math.degrees(math.atan(b/a))

    # Show work
    eq = '(a^2)+(b^2)=c^2'
    step1 = str(a)+'^2'
    step2 = str(b)+'^2'
    step3 = (str(asqr),'+',str(bsqr),'=','c^2'.strip())
    step4 = (str(asqr+bsqr),'=','c^2')
    step5 = '√'+str(csqr)

    # Print work
    print(eq)
    print(step1)
    print(step2)
    print(step3)
    print(step4)
    print(step5)

    # Print sln
    print('--------------------')
    print('c = '+str(c))
    print('--------------------')

    # # Turtle / graph
    # turtle.penup()
    # turtle.goto(0,0)
    # turtle.pendown()
    # turtle.forward(b*7)
    # turtle.goto(0,0)
    # turtle.left(90)
    # turtle.forward(a*7)
    # turtle.goto(0,0)
    # turtle.right(90)
    # turtle.forward(b*7)
    # turtle.left(angle+90)
    # turtle.forward(c*7)
    # turtle.done()

    # Back to start / quit
    print('Press enter to continue or backspace to quit')
    while True:
        if keyboard.is_pressed('enter'):
            startup()
        if keyboard.is_pressed('backspace'):
            os.system('cls')
            break

# Solves for leg
def leg():

    os.system('cls')

    # User input
    print('What is the length of your hypotenuse?')
    c = int(input('>>> '))
    os.system('cls')
    print('What is the length of your leg?')
    a = int(input('>>> '))
    os.system('cls')

    # Math
    csqr = int(c**2)
    asqr = int(a**2)
    bsqr = csqr - asqr
    b = math.sqrt(csqr - asqr)

    # # Calculate the angle opposite side a
    # angle = math.degrees(math.atan(b/a))

    # Show work
    eq = '(c^2)-(a^2)=b^2'
    step1 = str(c)+'^2'
    step2 = str(a)+'^2'
    step3 = (str(csqr),'-',str(asqr),'=','b^2'.strip())
    step4 = (str(csqr-asqr),'=','b^2')
    step5 = '√'+str(bsqr)

    # Print work
    print(eq)
    print(step1)
    print(step2)
    print(step3)
    print(step4)
    print(step5)

    # Print sln
    print('--------------------')
    print('b = '+str(b))
    print('--------------------')
    
    # # Turtle / graph
    # turtle.penup()
    # turtle.goto(0,0)
    # turtle.pendown()
    # turtle.forward(b*7)
    # turtle.goto(0,0)
    # turtle.left(90)
    # turtle.forward(a*7)
    # turtle.goto(0,0)
    # turtle.right(90)
    # turtle.forward(b*7)
    # turtle.left(angle+90)
    # turtle.forward(c*7)
    # turtle.done()

    # Back to start / quit
    print('Press enter to continue or backspace to quit')
    while True:
        if keyboard.is_pressed('enter'):
            startup()
        if keyboard.is_pressed('backspace'):
            os.system('cls')
            break

# START
startup()