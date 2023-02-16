num = input("How much elements u want to add in array ?")

print("\nEnter",num,"numbers")
n=int(num)
arr=[]
for i in range(n):
    element =input()
    arr.append(element)
    
    
print("\nThe list is: ")
for i in range(n):
    print((arr[i]),end=" ")