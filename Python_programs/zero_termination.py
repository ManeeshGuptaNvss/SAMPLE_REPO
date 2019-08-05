i=1
li=[]
k,pos,neg=-1,0,0
while i<2 :
    n=int(input('enter an integer:'))
    k=k+1
    if n==0 :
        break
    else:
      li.append(n)
print(li)
print('size of list :',k)
for i in range(0,k) :
    if (li[i]>0) :
        pos+=1
    else :
        neg+=1
print('Number of positive numbers in the list:',pos,'\n Number of negative numbers in the list:',neg)
        


    
