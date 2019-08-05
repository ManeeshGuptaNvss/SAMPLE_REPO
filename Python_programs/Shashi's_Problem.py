lis=[]
size=int(input('size of list:'))
for i in range(size):
    x=int(input( ))
    lis.append(x)
print(lis)
countlis=[ ]

for k in range (size):
    count=0
    for j in range (size):
        if lis[k] is lis[j]:
            count+=1
    countlis.append(count)
print(countlis)
m=countlis.index((max(countlis)))
print(lis[m])

            
