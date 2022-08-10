n=int(input())
s=input()
a=0
for i in range(0,len(s)-1):
    if s[i] ==s[i+1]:
        a+=1
    else:
        pass
print(a)
