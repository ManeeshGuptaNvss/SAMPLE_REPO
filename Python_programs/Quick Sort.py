def partition(arr,low,high):
    i = ( low-1 )        # index of smaller element
    pivot = arr[high]   # pivot
    print('pivot is' ,pivot)
    print(arr)
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            print('swapping', arr[i],arr[j])
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
    print('swapping',arr[i+1],arr[high])
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [10, 7, 8,5,2,3,98,88]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d\t" %arr[i],end='')

