#very imp

#for loop
low,high = input("enter two numbers").split()
for i in range(int(low),int(high)+1):
    print(i,end=" ")
    if i%13==0:
        break
    
#while loop

list1 =list(map(int,input("enter two no.").split()))
print(list1)

low=list1[0]
high=list1[1]
while low<=high:
    print(low,end=" ")
    
    if low%13==0:
        break
    low+=1