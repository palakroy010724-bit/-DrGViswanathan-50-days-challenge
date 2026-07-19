n=int(input("enter lower limit:"))
m=int(input("enter upper limit:"))
i=n
count=0
while i<m:
    i=i+1
    if i%2==1:
        count=count+1
print("number of odd numbers:",count)
        
