n,k=map(int,input().split())
s=0
for i in range(k):
    r=n%10
    if r!=0:
        n=n-1
    else:
        n=n//10
print(n)
