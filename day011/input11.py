num=int(input("enter your integer:"))
if num==0:
    print("digital root of your integer:",0)
elif num%9==0:
    print("digital root of your integer:",9)
else:
    print("digital root of your integer:",num%9)
    
     
