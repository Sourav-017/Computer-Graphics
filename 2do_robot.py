from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

length1 = 4
length2 = 5

start = (10, 10)
goal = (16, 16)


square_center = (30, 30)
square_size = 4


solution = None


def deg_to_rad(deg):
    return deg * math.pi / 180


def forward_kinematics(x0, y0, theta1, theta2):
    rad1 = deg_to_rad(theta1)
    x1 = x0 + length1 * math.cos(rad1)
    y1 = y0 + length1 * math.sin(rad1)

    rad2 = deg_to_rad(theta1 + theta2)
    x2 = x1 + length2 * math.cos(rad2)
    y2 = y1 + length2 * math.sin(rad2)

    return (x1, y1), (x2, y2)


def line_intersects_square(p1, p2, square_center, size):
    cx, cy = square_center
    half = size / 2
    sx1, sy1 = cx - half, cy - half
    sx2, sy2 = cx + half, cy + half

    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def intersect(A, B, C, D):
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

    corners = [(sx1, sy1), (sx2, sy1), (sx2, sy2), (sx1, sy2)]

    for i in range(4):
        if intersect(p1, p2, corners[i], corners[(i + 1) % 4]):
            return True
    return False


def find_solution():
    global solution
    for t1 in range(0, 360, 1):
        p1, p2 = forward_kinematics(*start, t1, 0)
        if not line_intersects_square(
            start, p1, square_center, square_size
        ) and not line_intersects_square(p1, p2, square_center, square_size):
            for t2 in range(0, 360, 1):
                p1, p2 = forward_kinematics(*start, t1, t2)
                if not line_intersects_square(
                    start, p1, square_center, square_size
                ) and not line_intersects_square(p1, p2, square_center, square_size):
                    dist = math.hypot(p2[0] - goal[0], p2[1] - goal[1])
                    if dist <= 0.5:
                        solution = (t1, t2, p1, p2)
                        return


def draw_square(center, size):
    cx, cy = center
    half = size / 2
    glColor3f(1, 0, 0)  # Red
    glBegin(GL_QUADS)
    glVertex2f(cx - half, cy - half)
    glVertex2f(cx + half, cy - half)
    glVertex2f(cx + half, cy + half)
    glVertex2f(cx - half, cy + half)
    glEnd()


def draw_point(x, y, r=5, color=(0, 1, 0)):
    glColor3f(*color)
    glPointSize(r)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_line(p1, p2, color=(0, 0, 1)):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(*p1)
    glVertex2f(*p2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_square(square_center, square_size)

    draw_point(*goal, r=6, color=(0, 1, 0))

    if solution:
        t1, t2, j1, end = solution
        draw_line(start, j1, (0, 0, 1))
        draw_line(j1, end, (0, 0, 1))
        draw_point(*start, r=4, color=(1, 1, 0))
        draw_point(*j1, r=4, color=(0, 1, 1))
        draw_point(*end, r=6, color=(1, 0, 1))

    glFlush()


def main():
    find_solution()
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b" Arm")
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 30, 0, 30)

    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
