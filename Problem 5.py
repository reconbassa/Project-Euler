
'''def primeFactorizer(n, p, factors):
    if n < 2:
        return factors
    if n % p == 0:
        n = n/p
        factors.append(p)
        return primeFactorizer(n, p, factors)
    else:
        p += 1
        return primeFactorizer(n, p, factors)
mFactors = []
for x in range(1, 21):
    pfactors = []
    pfactors = primeFactorizer(x, 2, pfactors)
    mFactors += pfactors
print(mFactors)'''

def factors(a, b, c):
    if a < 2:
        return c
    if a % b == 0:
        a = a / b
        c.append(b)
        return factors(a, b, c)
    else:
        b += 1
        return factors(a, b, c)
afactors = []
for n in range(1, 21):
    bfactors = []
    bfactors = factors(n, 2, bfactors)
    afactors += bfactors
print(afactors)




