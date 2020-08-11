import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def getAvailableLetters(lettersGuessed):
    asciilist = [c for c in string.ascii_lowercase]
    if lettersGuessed == []:
      return string.ascii_lowercase
    else:
      for c in lettersGuessed:
          if c in asciilist:
              asciilist.remove(c)
      result = ''.join(asciilist)
      return result

print(getAvailableLetters(lettersGuessed))