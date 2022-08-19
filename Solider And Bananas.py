k,n,w=map(int,input().split())
c=0
for i in range(1,w+1):
    s=k*i
    c=c+s
if c>n:
    print(c-n)
else:
    print(0)
