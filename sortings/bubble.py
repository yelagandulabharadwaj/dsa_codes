arr=[5,7,3,2,8,11,6,15]
passed=0
arr=[1,2,3,4,5,6,7]
for i in range(0,len(arr)-1):
    c=0
    for j in range(0,len(arr)-1-i):
        if (arr[j]>arr[j+1]):
            c+=1
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
    passed+=1
    if c==0:
        break
print(arr)
print(passed)