a,b=map(int,input().split())
c=0
while True:
    if a<=b:
        a=a*3
        b=b*2
        c+=1
    else:
        break
print(c)