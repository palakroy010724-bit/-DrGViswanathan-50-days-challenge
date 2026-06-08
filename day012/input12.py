l1=list(map(int,input("enter list 1:").split(",")))
l2=list(map(int,input("enter list 2:").split(",")))
l=l1+l2
l.sort()
print("merged sorted linked list:", l)
