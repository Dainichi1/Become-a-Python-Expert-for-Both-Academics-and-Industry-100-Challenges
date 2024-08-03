
fav1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']
sum = []

for i in range(len(fav1)):
    for j in range(len(fav2)):
       if fav1[i] == fav2[j]:
           sum.append (i+j) # esempio : indice 0 + indice 1 = 1
min_index_sum = min(sum) 
min_index = sum.index(min_index_sum) #indice del numero minore in sum : indice è 2 (il numero minore è 3)
print(fav1[min_index], min_index_sum)


