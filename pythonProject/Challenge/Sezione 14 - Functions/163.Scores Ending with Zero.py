def sumZero (L):
    summ = 0
    for i in L:
        if i % 10 == 0:
            summ += i
    return summ

v = sumZero([200,4564,45,100])

print(v)

