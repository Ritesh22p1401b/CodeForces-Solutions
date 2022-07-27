m,n=map(int,input().split())
if m%2==0 and n%2==0:
    a=m//2
    b=n//1
    f=a*b
    print(f)
elif m%2==0 and n%2!=0:
    a = m // 2
    b = n // 1
    f = a * b
    print(f)
elif n%2==0 and m%2!=0:
    a = m // 1
    b = n // 2
    f = a * b
    print(f)
elif m%2!=0 and n%2!=0:
    a=m*n
    f=a//2
    print(f)
    
