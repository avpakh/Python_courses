"""

Function for invert keys and values invert_dict()

>>> invert_dict({'a': 1,'b': 2,'c': 1})
{1: ['a', 'c'], 2: ['b']}

"""

def invert_dict(d):
    dict = {}
    for keys, values in d.iteritems():
        dict.setdefault(values, []).append(keys)
    return dict

d = {'a': 1,'b': 2,'c': 1}
print d     
print invert_dict(d)
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
