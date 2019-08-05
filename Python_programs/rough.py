def partition(a,low,high):
    i=low-1
    
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
def Quick(lis,low,high):
    if low<high:
        pi=partition(lis,low,high)
        Quick(lis,low,pi-1)
        Quick(lis,pi+1,high)
lis=[90,19,1,12,34,89]
Quick(lis,0,len(lis)-1)
print(lis)
