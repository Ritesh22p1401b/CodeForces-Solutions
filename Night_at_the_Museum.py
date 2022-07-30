s=input()
c,q=0,0
a,b=0,0
for i in s:
    if 97<=ord(i)<=110:
        c=ord(i)-97
        a=a+c
    elif 111<=ord(i)<=122:
        q=122-ord(i)
        b=b+q
print(a+b)


