numbers=input("enter numbers seprated by comma")
L=numbers.split(",")
print(list(L))
print(tuple(L))
print()

file=input("enter file name")
name=[]
name= file.split('.')
output=(name[1:2])
print("xtension is",output)

'''-------------------------------------------'''

list=['black','white','grey','black&white']
print("first item is",list[:1])
print("last item is",list[3:4])

'''------------------------------------------'''

date=(11,12,2018)
l=[]
l=list(date)
d=(l[0:1])
m=(l[1:2])
y=(l[2:3])
print("exam will strt from",d,"/",m,"/",y)
'''----------------------------------------------'''

n=int(input("give any no"))
A=(n*n)
B=(A*n)
C=(B*n)
print(C)