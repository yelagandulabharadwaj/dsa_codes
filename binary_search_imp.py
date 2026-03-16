#applicable only for sorted list

def normal_implemnt(arr,n):
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    print(mid,low,high)
    while low<=high:
        if arr[mid]==n:
            return f"element found at: {mid}"
        elif mid<low or mid>high:
            print(mid,low,high)
            return f"element not found"
        elif arr[mid]>n:
            print('line 15',mid,low,high)
            high=((low+high)//2)-1
        else:
            print('line 18',mid,low,high)
            low=((low+high)//2)+1
        mid=low+(high-low)//2

    if arr[mid]==n:
        return f"element found at: {mid}"
    
def recursive(arr,n,low,high,mid):
    print('times logged')
    if low>high:
        return -1
    elif arr[mid]==n:
        return f"found element at {mid}"
    elif arr[mid]<n:
        low=mid+1
        mid=low+(high-low)//2
        return recursive(arr,n,low,high,mid)
    else:
        high=mid-1
        mid=low+(high-low)//2
        return recursive(arr,n,low,high,mid)

arr=[1,2,3,4,5,6,7,8,9]
n=int(input())
print(normal_implemnt(arr,n))
print(recursive(arr,n,0,len(arr)-1,(0+len(arr)-1)//2))