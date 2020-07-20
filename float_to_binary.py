x = float(input("Enter a decimal number between 0 and 1: "))
'''
power = 0
z = ((2 ** power) * x) % 1

while z != 0:
    y = str((2 ** power) * x - int((2 ** power) * x))
    print("Remainder = " + y)
    power += 1
    z = ((2 ** power) * x) % 1

num = int(x * (2 ** power))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(power - len(result)):
    result = '0' + result

result = result[0:-power] + '.' + result[-power]
print("The binary representaion of the decimal " + str(x) + ' is ' + str(result))
'''
# 내가 만드는 2진법 변환 코드

flag = True
ans = ''
while flag:
    x *= 2
    if x > 1:
        ans = ans  + str(1)    
        x = x - int(x)
    elif x < 1:
        ans = ans+ str(0)
    else:
        ans = ans + str(1)
        print(int(ans))
        flag = False
