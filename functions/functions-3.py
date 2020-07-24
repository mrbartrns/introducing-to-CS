'''
def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)


print(a(3>2, a, b))
'''

# 함수는 내가 호출을 한 뒤에야 만들어진다. 따라서 호출 되기 전까지는 함수가 실행되지 않는다. a = 3이 실행된 뒤에야 f(x) 가 실행되므로, 이미 a 값이 바뀐 뒤이다.
a = 10
def f(x):
    return x + a

a = 3
f(1)