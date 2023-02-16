


#num = int(input("enter the number: "))

'''if num%2 ==0:
    print("even")
    
else:
    print("odd")'''
    
'''def isEven(num):
    num&1 is 1,then odd,else even
    return not(num & 1)

isEven(34)'''

def isEven(num):
    
    #n&1 is 1, then odd, else even
    return not(num & 1)


num = int(input("Insert a number:"))
print("Even" if isEven(num) else "Odd")
    
    