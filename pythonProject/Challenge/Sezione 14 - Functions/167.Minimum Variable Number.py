def minimum (*val, low_limit = None):
    if low_limit is None:
        return min(val)
    else:
        L = [x for x in val if x >= low_limit]
        return min(L)

print (minimum(1,2,5,10,-5))



