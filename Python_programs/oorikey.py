def merge_sort(ls):
    print('Splitting',ls)
    if len(ls)>1:
        mid=len(ls)//2
        lh=ls[:mid]
        rh=ls[mid:]
        merge_sort(lh)
        merge_sort(rh)
        i=j=k=0
        while i<len(lh) and j< len(rh):
            if lh[i]<rh[j]:
                ls[k]=lh[i]
                i+=1
            else:
                ls[k]=rh[j]
                j+=1
            k+=1
        while i<len(lh):
            ls[k]=lh[i]
            i+=1
            k+=1
        while j<len(rh):
            ls[k]=rh[j]
            j+=1
            k+=1
    print('Merging',ls)
lis=[38,27,43,3,9,82,10]
merge_sort(lis)
print(lis)
            
