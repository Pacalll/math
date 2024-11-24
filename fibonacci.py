import math

def fibonacci_range_loop(n):
    """
        This function calculates the Fibonacci sequence iteratively by storing
        each number in a list. It starts with the base cases (0 and 1) and builds
        the sequence by adding the two previous numbers.

        Args:
            n (int): The number of Fibonacci numbers to generate.

        Returns:
            fib_list: A list containing the first n Fibonacci numbers.
    """
    fib_list = []
    for x in range(n):
        if x == 0 or x == 1:
            fib_list.append(x)
        else:
            fib_list.append(fib_list[x-1] + fib_list[x-2])
    return fib_list

def fibonacci_range_recursive(n, fib_list):
    """
        This recursive function calculates the Fibonacci sequence by appending
        numbers to the given list until it reaches the desired length. It handles
        base cases (0 and 1) explicitly and calculates subsequent numbers by
        summing the last two elements of the list.

        Args:
            n: The number of Fibonacci numbers to generate.
            fib_list (list): A list to store Fibonacci numbers.

        Returns:
            list: A list containing the first n Fibonacci numbers.
    """
    if len(fib_list) == n:
        return fib_list

    if len(fib_list) == 0 or len(fib_list) == 1:
        fib_list.append(len(fib_list))
    else:
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fibonacci_range_recursive(n, fib_list)

def fibonacci(n):
    """
        Calculates the nth Fibonacci number using Binet's formula.
        Binet's formula is based on the golden ratio and allows direct calculation
        of Fibonacci numbers without iterative or recursive methods.

        Args:
            n (int): The position (n) in the Fibonacci sequence to calculate.

        Returns:
            The nth Fibonacci number as a floating-point value.
    """
    return (golden_ratio()**n - neg_golden_ratio()**n) / math.sqrt(5)
def golden_ratio():
    """
        Calculates the positive golden ratio value.
        The golden ratio is defined as (1 + sqrt(5)) / 2, approximately equal to 1.618.

        Returns:
            The positive golden ratio value as a floating-point value.
    """
    return (1 + math.sqrt(5)) / 2
def neg_golden_ratio():
    """
        Calculates the negative golden ratio value.
        The negative golden ratio is defined as (1 - sqrt(5)) / 2, approximately equal to -0.618.

        Returns:
            The negative golden ratio value as a floating-point value.
    """
    return (1 - math.sqrt(5)) / 2