def iterPower(base, exp):
    '''
    DocString
    base^exp equals to base*base(number of exp)
    exp >= 0
    '''
    if exp == 0:
        return 1
    else:
        return base * iterPower(base, exp - 1)

print(iterPower(2, 4))