# to use the tan, pi, we need to import python library math.
import math


def polysum(n, s):
    '''
    n: number of polygon, int, n > 0
    s: length of polygon, int, s > 0
    returns: sum of area and sqrt float, decimal 4 places

    '''
    # this is area equation
    area = (0.25 * n * (s ** 2))/(math.tan(math.pi / n))
    # this is perimeter equation
    perimiter = n * s

    # operator precedence: ** > +
    sum = area + perimiter ** 2
    
    # round(x, a) will return with a decimal places. I can also use ("%4f" %a)(String value)
    return round(sum, 4)
