"""
This is a file with issues
"""

import os, sys, pathlib

camelCase = "should be snake_case"


def main(num):
    """
    Prints the first N fibonacci numbers
    """
    a = 1
    b = 1
    c = "unused"
    print(f"1: {a}")
    print(f"2: {b}")
    for nth in range(3, num):
        a, b = b, a + b
        print(f"{nth}: {b}")


if __name__ == "__main__":
    main(10)
