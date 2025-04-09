from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random, time

limit = 500
tc = 1


def midpoint_circle_algorithm(center, radius):
    x, y = 0, radius
    p = 1 - radius

    plot_circle_points(center, x, y)

    while x <= y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
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


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, limit, 0, limit)


def callable(tc):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Midpoint Ellipse Drawing")
    init()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)
    start = time.time()
    while tc:
        center = (random.randint(100, limit - 100), random.randint(100, limit - 100))
        radius = random.randint(50, 100)
        midpoint_circle_algorithm(center, radius)
        tc -= 1
    end_time = time.time()
    print(f"Time : { end_time - start : .4f} sec")

    glEnd()
    glFlush()
    glutMainLoop()
