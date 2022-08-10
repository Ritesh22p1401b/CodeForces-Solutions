n=int(input())
s=input()
s1=s.upper()
s3=set(s1)
c=0
for i in s3:
    x=ord(i)
    if 65<=x<=90:
        c+=1
if c==26:
    print("YES")
else:
    print("No")

