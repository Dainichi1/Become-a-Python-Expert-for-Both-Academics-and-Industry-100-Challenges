s = 'aaaaaa\nbbbbbb\tcccccccc\rdddddddd\feeeeeeeeee'

print(s.splitlines())
print(s.splitlines(keepends=True))