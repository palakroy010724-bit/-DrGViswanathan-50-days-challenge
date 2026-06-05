n=int(input("enter your integer:"))
factorial=1
if n<0:
    print("factorial for negative numbers does not exist")
elif n==0:
    print("factorial=","1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("factorial of your integer=", factorial)