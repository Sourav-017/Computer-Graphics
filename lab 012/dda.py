from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

limit = 500


def dda(start, end):
    (x0, y0) = start
    (x1, y1) = end

    # Calculate the differences in x and y
    dx = x1 - x0
    dy = y1 - y0

    # Calculate the number of steps required for the line
    steps = max(abs(dx), abs(dy))

    # Calculate the increment in x and y
    x_inc = dx / float(steps)
    y_inc = dy / float(steps)

    # Plot the points along the line
    x, y = x0, y0
    for _ in range(steps):
        glVertex2i(round(x), round(y))
        x += x_inc
        y += y_inc


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glPointSize(1.0)
    glBegin(GL_POINTS)

    n = 100  # Number of lines
    for _ in range(n):
        start = (random.randint(0, limit), random.randint(0, limit))
        end = (random.randint(0, limit), random.randint(0, limit))
        dda(start, end)

    glEnd()
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    gluOrtho2D(0, limit, 0, limit)  # Define 2D coordinate system


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 1000)
glutCreateWindow(b"DDA Line Drawing")
init()
glutDisplayFunc(display)
glutMainLoop()
