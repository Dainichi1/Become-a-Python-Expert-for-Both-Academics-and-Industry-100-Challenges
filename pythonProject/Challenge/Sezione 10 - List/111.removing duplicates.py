list1 = [int(x) for x in input('Enter numbers separated by space: ').split()]

print(list1)

list2 = []

for i in list1:
    if i not in  list2:
        list2.append(i)
print(list2)