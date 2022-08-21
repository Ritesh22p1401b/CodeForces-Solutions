a=input()
b=input()
c=""
l=len(a)
i=0
while i<l:
    if a[i]==b[i]:
        c=c+"0"
    elif a[i]!=b[i]:
        c=c+"1"
    i+=1
print(c)
