def pr(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return (i+1)
def Qs(a,low,high):
    if low<high:
        pi=pr(a,low,high)
        Qs(a,low,pi-1)
        Qs(a,pi+1,high)
a1=[10,7,8,9,1,5]
n=len(a1)
Qs(a1,0,n-1)
print(a1)
