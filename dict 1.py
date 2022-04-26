

# from typing import Counter


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)




d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
for i in d2 :
    if i in d1 :
        d1[i] = d1[i] +d2[i]
    else :
        d1[i] = d2[i]
print(d1)






