n=int(input("enter the number:"))
n1=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if s==n1:
    print(n1,"is palindrome number")
else:
    print(n1,"is not palindrome number")  