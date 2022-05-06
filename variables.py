#!/bin/python3
#there is no command to declare a variable,they are created when you assign a value to them
a = 5 #x is a variable of type int
b = "cadena" #y is a variable of type string

#the variable types can be changed with casting

c=str(4)  #a variable of type string
d=int(4) #a variable of type int
e=float(4) #a variable of type float

#also you can check the variable's type by using the function type()

print(str(a)+" is a "+str(type(a)))
print(b+" is a "+str(type(b)))
print(c+" is a "+str(type(c)))
print(str(d)+" is a "+str(type(d)))
print(str(e)+" is a "+str(type(e)))

#do not forget that variables are case-sensitive
A = 6
print(str(a)+" "+str(A))


#a variable cant contain - or space,nor start  with a number


#in python you can assign multiple values to multiple variables in a single line
var1,var2,var3= 4,"cad",2.2
#one value to multiple variables
var4=var5="ena"
print(var4+" "+var5)
#also you can do unpacking,where you can copy the values of a collection to multiple variables
col1=["cad1","cad2","cad3"]
x,y,z=col1
print(x,y,z)
print(x+y+z)
