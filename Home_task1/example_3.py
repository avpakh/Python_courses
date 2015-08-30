"""

Function for determination  of prime numbers by Sieve of Eratosthenes from 2 to N
eranumbers()

>>> eranumbers(2)
[2]
>>> eranumbers(3)
[2, 3]
>>> eranumbers(5)
[2, 3, 5]
"""

def eranumbers(lim):
    """Return the list of prime numbers from range 2..n.

    >>> eranumbers(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 2

    """

    import math
    # verify condition for input number 
    if not lim >= 2:
        raise ValueError("n must be >= 2")
    # determine of prime numbers  
    is_prime = [False] * 2 + [True] * (lim - 1) 
    for n in range(int(lim**0.5 + 1.5)): 
        if is_prime[n]:
            for i in range(n*n, lim+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
