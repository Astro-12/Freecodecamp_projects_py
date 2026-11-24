#Implementation of bisection method
'''
The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. It works by narrowing down an interval where a root lies until it converges to a value within a specified tolerance.
For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the difference between the upper and lower bounds is less than or equal to 0.01.
'''
def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if number in (0, 1):
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        square = mid * mid

        if abs(high - low) <= tolerance:
            root = mid
            break

        if square < number:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {max_iterations} iterations")
        return None

    print(f"The square root of {number} is approximately {root}")
    return root
