# brute force
import sys

def blackJack(n: int, m: int, arr:list):
    '''
    n: number of cards
    m: maximum number
    arr: number of cards list
    '''
    i = 0
    j = i + 1
    k = j + 1
    res = 0
    for i in range(len(arr) - 2):
        if res == m:
            break
        else:
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    temp = arr[i] + arr[j] + arr[k]
                    if temp > res and temp <= m:
                        res = temp
    return res

# print(blackJack(5, 21, [5, 6, 7, 8, 9]))
# print(blackJack(10, 500, [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]))

n, m = map(int, sys.stdin.readline().split())
arr = [int(i) for i in sys.stdin.readline().split()]
print(blackJack(n ,m ,arr))