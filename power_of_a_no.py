'''base = float(input("Enter the value of base no. : "))
expo = float(input("Enter the value of expo no. : "))

temp =pow(base,expo)

print(temp)'''


base = float(input("Enter the value of base no. : "))
expo = int(input("Enter the value of expo no. : "))

result =1

i=1
while i<=expo:
    result = result*base
    i=i+1
    
print(result)