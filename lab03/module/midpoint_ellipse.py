from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random, time

width, height = 800, 800


def midpoint_ellipse(A, B, xc, yc):
    x = 0
    y = B

    p = (B**2) - (A**2 * B) + (0.25 * A**2)
    dx = 0
    dy = 2 * A**2 * B

    while dx < dy:
        four_symmetry_plot(xc, yc, x, y)
        x += 1
        dx = dx + (2 * (B**2))
        if p < 0:
            p = p + dx + (B * B)
        else:

            y -= 1

            dy -= 2 * A**2
            p = p + dx + (B * B) - dy
    four_symmetry_plot(xc, yc, x, y)

    p = ((B**2) * ((x + 0.5) ** 2)) + ((A**2) * ((y - 1) ** 2)) - (A**2 * B**2)

    while y >= 0:
        y -= 1
        dy = dy - (2 * A**2)

        if p >= 0:
            p = p - dy + (A**2)
        else:
            x += 1
            dx += 2 * B**2
            p += dx - dy + (A**2)
        four_symmetry_plot(xc, yc, x, y)


def four_symmetry_plot(xc, yc, x, y):
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc - x, yc + y)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)

    xc = random.randint(100, width - 100)
    yc = random.randint(100, height - 100)
    B = random.randint(10, 50)
    A = random.randint(B + 1, 100)

    midpoint_ellipse(A, B, xc, yc)

    glEnd()
    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, width, 0, height)


def callable(tc):

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Midpoint Ellipse Drawing")
    init()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glBegin(GL_POINTS)
    start = time.time()
    while tc:
        xc = random.randint(100, width - 100)
        yc = random.randint(100, height - 100)
        B = random.randint(30, 100)
        A = random.randint(30, 100)
        midpoint_ellipse(A, B, xc, yc)
        tc -= 1
    end_time = time.time()
    print(f"Time : { end_time - start : .4f} sec")

    glEnd()
    glFlush()
    glutMainLoop()
