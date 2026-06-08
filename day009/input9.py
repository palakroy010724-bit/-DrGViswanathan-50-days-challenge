num=list(map(int,input("enter elements of list(with missing element):").split(",")))
n=len(num)
act_sum= n*(n+1)/2
arr_sum= num[0]
for i in range(1,n):
    arr_sum=arr_sum+num[i]
miss_num= act_sum-arr_sum
print("missing number:",miss_num)
