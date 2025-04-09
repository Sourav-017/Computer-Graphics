import time
import sys

import dda_line
import bresenham_line
import midpoint_circle
import midpoint_ellipse
import bresenham_circle


def run_test_case(algorithm, num_cases):

    if algorithm == "dda_line":
        dda_line.callable(num_cases)

    elif algorithm == "bresenham_line":
        bresenham_line.callable(num_cases)

    elif algorithm == "midpoint_circle":
        midpoint_circle.callable(num_cases)

    elif algorithm == "midpoint_ellipse":
        midpoint_ellipse.callable(num_cases)

    elif algorithm == "bresenham_circle":
        bresenham_circle.callable(num_cases)

    else:
        print("Unknown algorithm:")
        sys.exit(1)


def main():
    print("Select a drawing algorithm:")
    print("1. DDA Line Drawing")
    print("2. Bresenham Line Drawing")
    print("3. Midpoint Circle Drawing")
    print("4. Midpoint Ellipse Drawing")
    print("5. Bresenham Circle Drawing")

    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice not in range(1, 6):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    algorithm_map = {
        1: "dda_line",
        2: "bresenham_line",
        3: "midpoint_circle",
        4: "midpoint_ellipse",
        5: "bresenham_circle",
    }
    algorithm = algorithm_map[choice]

    num_cases = int(input("Enter the number of test cases to run: "))

    run_test_case(algorithm, num_cases)

    
if __name__ == "__main__":
    main()
