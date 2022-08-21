n,h=map(int,input().split())
a=[int(q) for q in input().split()]
c=0
for  i in range(n):
    if a[i]>h:
        c+=2
    else:
        c+=1
print(c)
