n=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(0, len(arr)):
    print(str(arr[i])+" ",end='')
