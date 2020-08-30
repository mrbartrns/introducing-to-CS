# brute force
import sys

def decomposition(n):
    '''
    n: int
    return: int (constructor)
    '''
    constructor = 0
    for i in range(n):
        flag = False
        constructor = i
        copy = i
        remains = 0
        remain = 0
        quot = 0
        while not flag:
            quot = copy // 10
            remain = copy % 10
            remains += remain
            if quot == 0:
                flag = True
            else:
                temp = quot
                copy = temp
        if constructor + remains == n:
            return constructor
    return 0

n = int(sys.stdin.readline())
print(decomposition(n))