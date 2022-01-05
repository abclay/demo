"""
This is a normal file
"""


def main(num):
    """
    Prints the first N fibonacci numbers
    """
    prev = 1
    cur = 1
    print(f"1: {prev}")
    print(f"2: {cur}")
    for nth in range(3, num):
        prev, cur = cur, prev + cur
        print(f"{nth}: {cur}")


if __name__ == "__main__":
    main(10)
