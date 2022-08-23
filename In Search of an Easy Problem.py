n=int(input())
arr=[int(q) for q in input().split()]
f=0
for i in range(n):
    if arr[i]==1:
        f+=1
if f>0:
    print("HARD")
else:
    print("EASY")