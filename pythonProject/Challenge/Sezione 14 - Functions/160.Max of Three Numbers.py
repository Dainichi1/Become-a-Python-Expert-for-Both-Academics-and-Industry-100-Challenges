def max(a,b,c):
    mass = 0
    if a > b and a > c:
        mass = a
    elif b > a and b > c:
       mass = b
    else:
      mass = c
    return mass

v = max(10,152465,20)

print (v)

