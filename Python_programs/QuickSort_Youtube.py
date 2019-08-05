

def partition(l,h,li):
    pivot=li[l]
    i,j=l,h
    while i<j:
        while pivot<=li[i+1]:
            i+=1
        while pivot>li[j-1]:
            j-=1
        if i<j:
            li[i],li[j]=li[j],li[i]
    pivot,li[j]=li[j],pivot
    return j
def Quicksort(l,h,li):
    if l<h:
        j=partition(l,h,li)
        Quicksort(l,j,li)
        Quicksort(j+1,h,li)
lis=[2,4,1,39,3,9,38,28,14,35,22]
size=len(lis)
Quicksort(0,size-1,lis)

    

print(lis)
