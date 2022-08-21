n=int(input())
p=0
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    p=p-a
    p=p+b
    arr.append(p)
print(max(arr))

    



    
