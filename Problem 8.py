line = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
product = 0
for s in range(987):
    numbers = line[s: s + 13]
    digit_list =[int(n) for n in numbers]
    pot1 = 1
    for n in digit_list:
        pot1 = pot1 * n
    if pot1 > product:
        product = pot1
print(product)



'''a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
# a - m will take the place of the first 13 numbers
# a1 - m1 will take the place of the next 13 numbers.
#first and second char will be compared and which ever is greater will be kept
a1 = 14
b1 = 15
c1 = 16
d1 = 17
e1 = 18
f1 = 19
g1 = 20
h1 = 21
i1 = 22
j1 = 23
k1 = 24
l1 = 25
m1 = 26

first_char = int(line[a]) * int(line[b]) * int(line[c]) * int(line[d]) * int(line[e])  * int(line[f])  * int(line[g]) * int(line[h]) * int(line[i]) * int(line[j]) * int(line[j]) * int(line[k]) * int(line[l]) * int(line[m])
second_char = int(line[a1]) * int(line[b1]) * int(line[c1]) * int(line[d1]) * int(line[e1])  * int(line[f1])  * int(line[g1]) * int(line[h1]) * int(line[i1]) * int(line[j1]) * int(line[j1]) * int(line[k1]) * int(line[l1]) * int(line[m1])
print('first character : ', first_char, 'second character : ', first_char)
while first_char < 1:
    a += 1
    b += 1
    c += 1
    d += 1
    e += 1
    f += 1
    g += 1
    h += 1
    i += 1
    j += 1
    k += 1
    l += 1
    m += 1
    if first_char < 1 or  first_char < 55199040:
        first_char = int(line[a]) * int(line[b]) * int(line[c]) * int(line[d]) * int(line[e]) * int(line[f]) * int(line[g]) * int(line[h]) * int(line[i]) * int(line[j]) * int(line[j]) * int(line[k]) * int(line[l]) * int(line[m])
        print(first_char)'''
