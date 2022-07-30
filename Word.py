n=input()
b,s=0,0
for i in n:
    if 65<=ord(i)<=90:
        b+=1
    else:
        s+=1 
if b>s:
    x=n.upper()
    print(x)
else:
    d=n.lower()
    print(d)