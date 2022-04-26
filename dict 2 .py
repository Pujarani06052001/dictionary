# k= 'w3resource'
# i=0
# a={}
# c=0
# while i<len(k):
#     c+=1
#     a[k[i]]=c
# i+=1
# print(a)



k= 'w3resource'
b =list(k)
c={}
for i in k:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)