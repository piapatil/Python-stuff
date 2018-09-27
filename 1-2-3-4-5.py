print("Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.It \n was created by Guido van Rossum during 1985- 1990. \n \t Like Perl, Python source code is also available under the GNU General Public License (GPL). This \ntutorial gives enough understanding on Python programming language.")
print()

import sys
print ("this version we are using-> \n", sys.version) 

print()
import datetime
current= datetime.datetime.now()
print("current date time->",current)
print()

r=float(input("enter radius"))
area= 3.14*(r*r)
print("area of circle is->",area)
print()

fn=input("enter first name:")
ln=input("enter last name:")
print(ln+fn)