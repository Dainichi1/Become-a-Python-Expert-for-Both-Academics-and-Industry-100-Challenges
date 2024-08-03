def add(a, b, c):
    return a + b + c

print(add(10, 5, 2))  # Output: 17
print(add(10, 5))     # Questo darà un errore perché mancano argomenti

def add(a, b=0, c=0):
    return a + b + c

print(add(5, 7))          # Output: 12
print(add(a=10, b=5, c=2))  # Output: 17
print(add(b=5, c=2, 10))    # Questo darà un errore, l' argomento '10' deve essere nominato


def net_sal(basic, allowance, deduction):
    net = basic + allowance - deduction
    return net

n = net_sal(deduction=2000, allowance=6000, basic=8000)
print('Net salary is:', n)

n = net_sal(8000, deduction=2000, allowance=6000)
print('Net salary is:', n)


def add(a, b, c, d, e, f):
    return a + b + c + d + e + f

result = add(2, 5, 9, 7, 3, 8)  # Tutti argomenti posizionali
print(result)  # Output: 34

result = add(f=8, c=9, b=5, e=7, d=3, a=2)
print(result)  # Output: 34

# Funzione con argomenti misti posizionali e keyword
def add(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f

result = add(2, 5, d=7, f=4, e=9, c=6)
print(result)  # Output: 33
