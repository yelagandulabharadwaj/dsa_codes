arr=[5,7,3,2,8,11,6,15]

for i in range(1,len(arr)):
    j=i-1
    k=arr[i]
    while(k<arr[j] and j>-1):
        arr[j+1]=arr[j]    
        j-=1
    arr[j+1]=k
print(arr)