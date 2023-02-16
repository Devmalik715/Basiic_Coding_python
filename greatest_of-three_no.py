first = int(input("Enter the first no. : "))
second = int(input("Enter the second no. : "))
third = int(input("Enter the third no. : "))

if first == second and second==third:
    print("all are equal")
elif first>second and first>third:
    print(first,"is greater")
elif second>first and second>third:
    print(second,"is greater")
else:
    print(third, "is greater")
    
print(max(first,max(second,third)),"is greater")