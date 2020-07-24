def fourthPower(x):
    """
    x: int or float
    """
    # I have to practice like this style
    return square(square(x))

def square(x):
    return x * x

print(fourthPower(3))