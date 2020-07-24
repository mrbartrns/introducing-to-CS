def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    count = 0
    # Your code here
    if a >= b:
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                count = i

    else:
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                count =i
    
    return count

print(gcdIter(3, 3))