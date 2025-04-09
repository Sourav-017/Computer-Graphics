from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random, time

limit = 500
t = 0


def dda(start, end):
    (x0, y0) = start
    (x1, y1) = end

    dx = x1 - x0
    dy = y1 - y0

    steps = max(abs(dx), abs(dy))

    x_inc = dx / float(steps)
    y_inc = dy / float(steps)

    x, y = x0, y0
    for _ in range(steps):
        glVertex2i(round(x), round(y))
        x += x_inc
        y += y_inc


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) 
    glPointSize(1.0)
    glBegin(GL_POINTS)
    start_time = time.time()
    for _ in range(t):
        start = (random.randint(0, limit), random.randint(0, limit))
        end = (random.randint(0, limit), random.randint(0, limit))
        dda(start, end)
    end_time = time.time()
    print(f"Time : { end_time - start_time : .4f} sec")

    glEnd()
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, limit, 0, limit)


def callable(tc):

    global t
    t = tc
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"DDA Line Drawing")
    init()
    glutDisplayFunc(display)
    glutMainLoop()