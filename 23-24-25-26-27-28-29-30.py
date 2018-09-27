string=[]
string=input("enter string:")
n=int(input("how many copies:"))
first_two_letters=string[:2]
if(len(string)<=2):
    for i in range(0,n):
        print(string)
else:
    for i in range(0,n):
        print(first_two_letters)
    
 
letter=input("enter letter:")
vowel=['a','e','i','o','u']
if letter in vowel:
    print("It's vowel")
else:
    print("consonent")
    
    
group=[1,2,3,4,5,6]
n=int(input("enter no. to search"))
if n in group:
    print("found")
else:
    print("not found")
    
    
print("printing histogram")
data=['2','3','5','1','6']
for i in data:
    print("#"* int(i))

L=['p','i','a']
result=''
for i in L:
    result+=(i)
print(result)
    

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
958,743, 527]

for i in numbers:
    if i==237:
        print(i)
        break
    elif i%2==0:
        print(i)
 
list_1 = set(["White", "Black", "Red"])
list_2 = set(["Red", "Green"])
print(list_1.difference(list_2))



b=int(input("enter value of base"))
h=int(input("enter value of height"))
area=(b*h)/2
print(area)