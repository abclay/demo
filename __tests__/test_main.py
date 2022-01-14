from demo import main


def test_main():
    assert main.fib(0) == 1
    assert main.fib(1) == 1
    assert main.fib(2) == 2
    assert main.fib(3) == 3
