def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    # g번째 문자가 char와 동일하다면, 참을 반환
    # 그렇지 않다면, 문자가 1개이하인지 확인 -> 거짓을 반환
    # 그렇지 않다면, ord(char)가 aStr[g] 보다 큰지 작은지 확인
    # 크다면, high를 g로 설정, 작다면, low를 g로 설정.
    low: int = 0
    high: int = len(aStr)
    g: int = int((low + high) / 2)
    check = ord(char) == ord(aStr[g])
    if check:
        return True
    else:
        if len(aStr) <= 1:
            return False
        else:
            if ord(char) > ord(aStr[g]):
                low = g
                return isIn(char, aStr[low:high])
            else:
                high = g
                return isIn(char,aStr[low:high])

print(isIn('e', 'abcdef'))