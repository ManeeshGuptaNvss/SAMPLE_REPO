fas=[12,3,1,2,89,78]
for i in range (len(fas)):
    j=i
    while j>0:
        if fas[j] <fas[j-1]:
            fas[j],fas[j-1]=fas[j-1],fas[j]
        else:
            break
        j-=1
print(fas)
