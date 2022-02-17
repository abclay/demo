"""
This is a normal file
"""

bad_formatting = [1, 2, {3: 4}]


def fib(num):
    """
    Return that fib num
    """
    if num <= 1:
        print(f"{num} == 1")
        return 1
    prev = 1
    cur = 1
    for _ in range(0, num - 1):
        prev, cur = cur, prev + cur
    print(f"{num} == {cur}")
    return cur


def main(num):
    """
    Prints the first N fibonacci numbers
    """
    for nth in range(num):
        print(f"{nth}: {fib(nth)}")


if __name__ == "__main__":
    main(10)
