def partition(low,high,arr):
    i=low+1
    j=high
    pivot=arr[low]
    while True:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>=low and arr[j]>pivot:
            j-=1
        
        if i>=j:
            break
        arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick(low,high,arr):
    if low<high:
        pi=partition(low,high,arr)
        quick(low,pi-1,arr)
        quick(pi+1,high,arr)

arr=[7,5,11,2,3]
quick(0,len(arr)-1,arr)
print(arr)