def  partition(lis,low,high):
    
    pivot= lis[low]
    i=low+1
    j=high
    flag=False
    while not flag:
        while i<=j and lis[i]<=pivot:
            i+=1
        while j>=i and lis[j]>=pivot:
            j-=1
        if i>j:
            flag=True
        else:
            print('swapping',lis[i],lis[j])
            lis[i],lis[j]=lis[j],lis[i]
    print('swapping',lis[j],lis[low])
    lis[j],lis[low]=lis[low],lis[j]
    return j
def QuickSort(lis,low,high):
    if low<high:
        k=partition(lis,low,high)
        QuickSort(lis,low,k-1)
        
        QuickSort(lis,k+1,high)

lis2=[9,7,8,1,2,3,4]

QuickSort(lis2,0,len(lis2)-1)
print(lis2)
