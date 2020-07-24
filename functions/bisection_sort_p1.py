x = 100
low = 0
high= x
g = int((low + high) / 2)
check = True

print(f"Please think of a number between {low} and {x}!")
while check:
    print(f"Is your number {g}?")
    print("Enter 'h' to indicate the guess is too high.", end=" ")
    print("Enter 'l' to indicate the guess is too low.", end=" ")
    print("Enter 'c' tp indicate I guessed correctly.", end=" ")
    string: str = input()
    if string == 'h':
        high = g
        g = int((low + high) / 2)
    elif string == 'l':
        low = g
        g = int((low + high) / 2)
    elif string == 'c':
        print(f"Game over. Your secret number was: {g}")
        check = False
    else:
        print("Sorry, I did not understand your input.")

# test