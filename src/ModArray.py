def ModArray(arr,modval):
    res =0
    for i in range(len(arr)):
        res = (res*10+arr[i])%modval
    return res
arr=list(map(int,input().split()))
modval=int(input())
print(ModArray(arr,modval))