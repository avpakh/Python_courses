"""
Function for calulation of factorial with non-recursive methods
factorial()

>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
"""

def factorial(z):
    """Return the factorial of z, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(z) for z in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: z must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(40.1)
    Traceback (most recent call last):
        ...
    ValueError: z must be exact integer
 
    It must also not be ridiculously large:
    >>> factorial(2e100)
    Traceback (most recent call last):
        ...
    OverflowError: z too large
    """

    import math
    if not z >= 0:
        raise ValueError("z must be >= 0")
    if math.floor(z) != z:
        raise ValueError("z must be exact integer")
    if z+1 == z:  # catch a value like 1e300
        raise OverflowError("z too large")

   
    result = 1
    while z > 0:
        result *= z
        z -= 1
    return result
    
   
if __name__ == "__main__":
    import doctest
    doctest.testmod()
