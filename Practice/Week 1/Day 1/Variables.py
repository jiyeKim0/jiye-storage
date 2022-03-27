#Python Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

A = 5
B = "John"
print(type(A))
print(type(B))

#Single Quotes & Double Quotes for string variables are the same.

c = 4
C ="Sally"
# C will not overwitre c

#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 2myvar = "John" / my-var = "John" / my var = "John" (can't be variables)

#Assign Muliple Values
numbers = 1,2,3,4,5 # 패킹
print(numbers)

fruits = ["apple", "banana", "cherry"]
d, e, f = fruits
print(d)
print(e)
print(f)

#Output Variables
n1 = "Python"
n2 = "is"
n3 = "awesome"
print (n1,n2,n3)

# x = 5, y = "John" / print(x + y) is invalid
nb = 5
w = "John"
print (nb,w)

#Global Variables
T = "awesome"

def myfunc():
  print(T)

myfunc() #run myfunc #print awesome
print(T) #print T Global Variables #print awesome

#Local Variables
P = "awesome"

def fn():
  P = "fantastic"
  print("Python is " + P)

fn() #run fn #Python is fantastic #Local Variables
print("Python is " + P) #Python is awesome #Global Variables

#Global Keyword - case_1
def myfunc2():
  global v
  v = "fantastic"

myfunc2()

print("Python is " + v) #print Python is fantastic

#Global Keyword - case_2
j = "awesome"

def myfunc3():
  global j
  j = "fantastic" #Global Variable "j=awesome" changed into "j=fantastic"

myfunc3()

print("Python is " + j)
