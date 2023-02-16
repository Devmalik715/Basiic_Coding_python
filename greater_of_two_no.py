first = int(input("Enter the first no. : "))
second = int(input("Enter the second no. : "))

if first == second:
    print("both are equal")
elif first>second:
    print(first,"is greater")
else:
    print(second,"is greater")
    
print(max(first,second),"is greater")