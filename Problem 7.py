
count = 0
for x in range(2, 1000000 +1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            count += 1
            print(x, count)
            if count == 10001:
                print(x, 'HERE IS THE MAGIC NUMBER')
