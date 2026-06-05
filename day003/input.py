n=int (input("enter your integer:"))
count=0
while n>0:
    count= count+1
    n=n//10

print("number of digits the given number has=",count)