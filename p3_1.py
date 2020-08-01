secretWord: str = 'apple'
lettersGuessed: list = ['e', 'i', 'k', 'p', 'r', 's']

#문자열의 문자를 입력받고, 시크릿워드의 문자가 lettersGuessed에 모두 있다면, True 아니면 False
def isWordGuessed(secretWord:str, lettersGuessed:list) -> bool:
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True


print(isWordGuessed(secretWord, lettersGuessed))