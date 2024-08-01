list1=['A','B','C','D','E','A','B','E','B','D','B','E']

result = []

for i in list1:
    if i not in result:

        result.append(i)
        summ =list1.count(i)
        result.append(summ)
print(result)