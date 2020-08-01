secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# expected output: _pp_e
def getGuessedWord(secretWord: str, lettersGuessed:list) -> str:
    secretWordList = []
    for c in secretWord:
        if c not in lettersGuessed:
            secretWordList.append('_')
        else:
            secretWordList.append(c)
    result = ''.join(secretWordList)
    return result

print(getGuessedWord(secretWord, lettersGuessed))