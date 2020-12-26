#Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#cach 2
x = "test"
def myexample():
    print("This is " + x)

myexample()
print("tet la mot van hoa " + x)

#Bien cuc bo
def globalmyfuc():
    global x
    x = "this a variable global"

globalmyfuc()

print("this is" + x)