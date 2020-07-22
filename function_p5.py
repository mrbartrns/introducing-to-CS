def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    count = 0
    # Your code here
    if a >= b:
        if a % b == 0:
            count = b
            return count
        else:
            return gcdRecur(a, b - 1)
    else:
        if b % a == 0:
            count = a
            return count
        else:
            return gcdRecur(a - 1, b)

# other things
def gcdRecur2(a, b):
    if a == b:
        return a
    else:
        if a > b:
            if b == 0:
                return a
            else:
                return gcdRecur2(b, a % b)
        else:
            if a == 0:
                return b
            else:
                return gcdRecur2(b % a, a)

print(gcdRecur2(3, 4))