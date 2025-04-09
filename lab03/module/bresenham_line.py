from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random, time

limit = 500
t = 0

def bresenham(start, end):
    (x0, y0) = start
    (x1, y1) = end

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        glVertex2i(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)
    start_time = time.time()
    for _ in range(t):
        start = (random.randint(0, limit), random.randint(0, limit))
        end = (random.randint(0, limit), random.randint(0, limit))
        bresenham(start, end)
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
    glutCreateWindow(b"Bresenham Line Drawing")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
