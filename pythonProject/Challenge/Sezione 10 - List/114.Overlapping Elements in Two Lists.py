list1 = [10,15,6,9,12,8,4]
list2 = [14,6,19,4,7,10,11]

list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            list3.append(list1[i])
print(list3)