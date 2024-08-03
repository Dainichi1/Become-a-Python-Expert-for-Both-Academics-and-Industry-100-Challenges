# ModuleOne.py

total_amount = 2000

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# Questo codice viene eseguito solo se il modulo viene eseguito direttamente
if __name__ == '__main__':
    print(__name__)
    print('From Module One', add(20, 30))
    print('From Module One', sub(50, 10))


