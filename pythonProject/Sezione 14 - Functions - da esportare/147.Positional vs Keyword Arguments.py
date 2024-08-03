# Definizione della funzione
def net_sal(basic, allowance, deduction):
    print('basic:', basic)
    print('allowance:', allowance)
    print('deduction:', deduction)
    net = basic + allowance - deduction
    return net

# Chiamata della funzione con argomenti keyword
n = net_sal(deduction=2000, allowance=6000, basic=8000)
print('Net salary is:', n)

# Chiamata della funzione con argomenti sia posizionali che keyword
n = net_sal(8000, deduction=2000, allowance=6000)
print('Net Salary is:', n)
