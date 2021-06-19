largest = 0
for i in range(900, 999):
    for ii in range(900, 999):
        if str(i * ii) == str(i * ii)[::-1] and i * ii > largest:
            largest = i * ii
print(largest)