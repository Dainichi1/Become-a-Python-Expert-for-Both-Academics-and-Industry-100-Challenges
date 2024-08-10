def pascal (n) :
    r = [1]
    for i in range (n):
        print(r)
        tr = [0] + r
        r = r + [0]
        nr = [x+y for x,y in zip (r,tr)]
        r = nr

print(pascal(4))