epsilon = 0.01
y = 24.0
guess = y / 2.0
num_guess = 0

while abs(guess ** 2 - y) >= epsilon:
    num_guess += 1
    guess = guess - ((guess ** 2 - y) / (2 * guess))
    print(f"number of guesses: {num_guess}")
    print(guess)