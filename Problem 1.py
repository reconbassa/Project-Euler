a = 1
elligible = []
def multiple_test(a):
    while a < 999:
        a += 1
        if a % 3 == 0 or a % 5 == 0:
            elligible.append(a)
            print(a, sum(elligible))

multiple_test(a)

