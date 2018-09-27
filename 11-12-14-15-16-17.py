my_func=input("enter function name:")
print(help(my_func))


import calendar
m=int(input("month:"))
y=int(input("year:"))
print(calendar.month(y,m))


from datetime import date
f=date(2017,7,20)
l=date(2017,7,11)
ans=f-l
print(ans.days)


radius=int(input("give radius"))
r=radius*radius*radius

form=4*3.14*r
vol=form/3
print("volume of sphere is",vol)


no=int(input("give no"))
if(no<17):
    ans=17-no
    print("diff is",ans)
else:
    ans=no-17
    output=ans*2
    print("double of diff is",output)


no=int(input("give no"))
if(no<=100):
    print("no between 0 to 100")
elif(no>100 and no<=1000):
    print("no between 101 to 1000")
elif(no>1000 and no<=2000):
    print("no between 1001 to 2000")
else:
    print("extending range")















    
    
    
    
    
    
    
    

