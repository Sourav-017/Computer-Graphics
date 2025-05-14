from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window and clipping area dimensions
width, height = 600, 600
xmin, ymin, xmax, ymax = 200, 200, 400, 400

# Store lines as (x1, y1, x2, y2)
lines = []

# Bit codes
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8


def compute_code(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code


def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2:
            break
        else:
            code_out = code1 if code1 else code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None


def draw_line(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
    glColor3f(1.0, 1.0, 1.0)  # default white color
    gluOrtho2D(0, width, 0, height)  # orthographic projection


def generate_random_lines(n=10):
    for _ in range(n):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        lines.append((x1, y1, x2, y2))


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Step 1: Draw original lines in white
    for line in lines:
        draw_line(*line, color=(1, 1, 1))

    # Step 2: Draw clipping rectangle in green
    glColor3f(0, 1, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

    # Step 3: Draw clipped lines in red (on top of previous lines)
    for line in lines:
        clipped = cohen_sutherland_clip(*line)
        if clipped:
            draw_line(*clipped, color=(1, 0, 0))

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Cohen-Sutherland Line Clipping")
    init()
    generate_random_lines(10)
    glutDisplayFunc(display)
    glutMainLoop()


main()
