def count (phrase):
    upper = 0
    lower = 0

    for i in phrase:
        if i.islower():
            lower += 1
        else:
            upper += 1
    return lower,upper



v = count('fsdfsAAAAdfs')

print(v)