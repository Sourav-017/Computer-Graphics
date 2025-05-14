from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window and clipping area dimensions
width, height = 600, 600
xmin, ymin, xmax, ymax = 200, 200, 400, 400

# Store lines as (x1, y1, x2, y2)
lines = []


def liang_barsky_clip(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel and outside
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 > u2:
        return None

    x1_clip = x1 + u1 * dx
    y1_clip = y1 + u1 * dy
    x2_clip = x1 + u2 * dx
    y2_clip = y1 + u2 * dy

    return (x1_clip, y1_clip, x2_clip, y2_clip)


def draw_line(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
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

    # Step 3: Draw clipped lines in orange
    for line in lines:
        clipped = liang_barsky_clip(*line)
        if clipped:
            draw_line(*clipped, color=(1.0, 0.5, 0.0))  # orange

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Liang-Barsky Line Clipping")
    init()
    generate_random_lines(10)
    glutDisplayFunc(display)
    glutMainLoop()


main()
