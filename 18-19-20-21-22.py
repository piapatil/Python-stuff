no1=int(input("enter first no:"))
no2=int(input("enter second no:"))
no3=int(input("enter third no:"))
if no1==no2 and no2==no3:
    add=no1+no2
    result=add+no3
    print("thrice of sum is:",result*result*result)
else:    
    add=no1+no2
    result=add+no3
    print("sum is:",result)
    
    
string=input("enter sentence:")
L=(list(string))

if L[0] is "Is":
    print(string)
else:
    print("Is"+string)
    

string=input("enter string:")
n=int(input("tell how many times to print:"))
for i in range(0,n):
    print(string)
    

n=int(input("enter no."))
if(n%2==0):
    print("even no")
else:
    print("odd")
    
L=[1,2,3,4,5,4,6,4]
count=0
for i in L:
    if(i==4):
        count+=1
print(count)