
def fib(n):
   
    if n<0:
        print("incorrect input,n cannot be negative")
    elif n==0:
        return n
    elif n==1:
        return n 
    else:
        return fib(n - 1) + fib(n - 2)
n=int(input("enter input integer n:"))

print("fibonacci series:")
for i in range(n):
    print(fib(i) , end=" ")

