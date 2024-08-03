s1 = input ('Enter the first string: ')
s2 = input ('Enter the second string: ')

sort1 = sorted(s1)
sort2 = sorted(s2)



if len(sort1) == len(sort2) and sort1 == sort2:
    print ('anagram')
else:
    print ('not anagram')
