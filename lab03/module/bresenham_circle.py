from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random, time

limit = 500
t = 0 


def bresenham_circle(center, radius):
    x, y = 0, radius
    p = 3 - 2 * radius

    plot_circle_points(center, x, y)

    while x <= y:
        x += 1
        if p < 0:
            p = p + 4 * x + 6
        else:
            y -= 1
            p = p + 4 * (x - y) + 10

        plot_circle_points(center, x, y)


def plot_circle_points(center, x, y):
    cx, cy = center

    glVertex2i(cx + x, cy + y)
    glVertex2i(cx - x, cy + y)
    glVertex2i(cx + x, cy - y)
    glVertex2i(cx - x, cy - y)
    glVertex2i(cx + y, cy + x)
    glVertex2i(cx - y, cy + x)
    glVertex2i(cx + y, cy - x)
    glVertex2i(cx - y, cy - x)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)

    start_time = time.time()
    for _ in range(t):
        center = (random.randint(100, limit - 100), random.randint(100, limit - 100))
        radius = random.randint(50, 100)
        bresenham_circle(center, radius)
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
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham Circles")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
