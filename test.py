lst1 = [1, 3, 4, 6, 7, 9]
lst2 = [1,2,4,5,9,10]
r = []
for i in lst1:
    for j in lst2:
        if i == j:
            r.append(i)
print(r)