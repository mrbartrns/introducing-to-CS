#always think 'divide and conquer', 'decrease and conquer'

def isPalindrome(string):
    def toChar(string):
        ans = ''
        string = string.lower()
        for c in string:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans
    
    def isPal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and isPal(string[1: -1])
    
    return isPal(toChar(string))

print(isPalindrome('hi'))