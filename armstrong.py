n=int(input("enter the number:"))
n1=n
s=0
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if s==n1:
    print(n1,"is armstrong number")
else:
    print(n1,"is not armstrong number")        