animals = { 'a': ['aadvrark'], 'b':['baboon'], 'c':['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(animals):
    count = 0
    for k in animals:
        count += len(animals[k])
    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    biggestKey = ''
    if aDict == {}:
        return None
    else:
        for k in aDict:
            if count < len(aDict[k]):
                count = len(aDict[k])
                biggestKey = k
        return biggestKey
print(biggest({}))

#list와 array의 차이: list는 같은 여러 종류의 데이터 타입을 담을 수 있는 반면, array는 한종류만 가능

def fib_efficient(n:int, d:dict): #n is for key in dict
    ans = 0
    if n in d:
        return d[n]
    else:
        ans += fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans

d = {1: 1, 2: 2}