def diff (a,b):
    if abs(a-b) <= 5:
        return True
    else:
        return False

v = diff(5,8)

print(v)