def genPrimes():
    primes = [2]
    num = 2
    yield 2
    while True:
        num += 1
        for i in primes:
            if num % i != 0:
                primes.append(num)
                yield num
                break
            else:
                break

g = genPrimes()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))