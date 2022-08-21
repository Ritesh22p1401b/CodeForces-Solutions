n=int(input())
arr=[]
c=1
for i in range(n):
    a=int(input())
    arr.append(a)
for j in range(n-1):
    if arr[j]!=arr[j+1]:
        c+=1
   
print(c)

