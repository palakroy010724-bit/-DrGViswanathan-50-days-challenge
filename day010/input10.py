arr= list(map(int,input("enter list(seperatd by commas):").split(",")))
n=len(arr)

m=(n//2)
L=[]
for i in range(m,n):
    mid= arr[i]
    L.append(mid)
print("middle element:",L)