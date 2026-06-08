num=int(input("enter number:"))
summ=0
for i in range(1,num):
    if num%i==0:
        summ=summ+i
if summ==num:
    print("true")
else:
    print("false")

