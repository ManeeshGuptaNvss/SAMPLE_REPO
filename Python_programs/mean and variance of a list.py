lis=[]
size=int(input('enter the size of the list:'))
for i in range(size):
    x=eval(input('enter a value:'))
    lis.append(x)
mean= sum(lis)/ size
print('mean:',mean)
lis2=[(x-mean)**2 for x in lis]
print(lis2)
variance=sum(lis2)/size
print('variance:  %.3f' %variance)
