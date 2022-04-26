d=[{"V":"S001"}, 
{"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
d1=[]
d2=[]
for i in range(len(d)):
    d1.append(d[i])
    if d1[i] not in d2:
        d2.append(d[i])
print(d2)
