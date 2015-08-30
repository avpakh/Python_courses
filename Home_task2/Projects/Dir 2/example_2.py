"""

Function for calulation sq. equation with Vietta teorema
roots()

>>> sqroots(1,7,10)
(-2, -5)
>>> sqroots(15,-11,2)
(0.400, 0.333)
>>> sqroots(2,3,-2)
(-2.0, 0.5)


"""
def sqroots(a,b,c):
    # determination of determinant
    discr = b**2 - 4*a*c
    if discr < 0:
        print " the equation roots can't be solved"
        return () 
    import random
    # getting roots for teorema rules in case if a=1
    if a == 1:
        while True:
            x1 = random.randrange(0,2*abs(c)) - abs(c)
            x2 = random.randrange(0,2*abs(c)) - abs(c)
            if  (x1 * x2 == c) and ((x1 + x2) == - b):
                print 'x1=',x1
                print 'x2=',x2
                return x1,x2
                break    
    else:
        # getting roots for teorema rules in case if a <>1
         c = c * a
         while True:
            t1 = random.randrange(0,2*abs(c)) - abs(c)
            t2 = random.randrange(0,2*abs(c)) - abs(c)
            if (t1 * t2 == c) and ((t1 + t2) == - b):
                x1=float(t1)/a
                x2=float(t2)/a
                print 'x1= %*.*f' %(7,5,x1)
                print 'x2= %*.*f' %(7,5,x2)
                return x1,x2 
                break

if __name__ == "__main__":
    import doctest
    doctest.testmod()
