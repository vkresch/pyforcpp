####################################################################################
# Everything in python is an object and is dynamically checked at runtime (Reason for slow)
# int is an object not a real int like in C++
import sys

####################################################################################
# int/float
a = 42
b = 42

# Returns the actual location  
# where the variable is stored 
print(id(a)) 

# Returns the actual location  
# where the variable is stored 
print(id(b)) 

# Returns true if both the variables 
# are stored in same location 
print(a is b) # True
print("---------------")

####################################################################################
# Strings
a = "first"
b = "first" 

print(id(a)) 
print(id(b)) 
print(a is b) # True
print("---------------")

####################################################################################
# List are mutable
a = [10, 20, 30] 
b = [10, 20, 30] 

print(dir(a))  
print("Size of list:", sys.getsizeof(a))
print(id(a)) 
print(id(b)) 
print(a is b) # False

print("---------------")

####################################################################################
# Tuples are immutable are smaller and faster and cannot be changes 
# at runtime
a = (10, 20, 30, 30) 
b = (10, 20, 30) 
c = 10, 20, 30 # you can leave out the paranthesis
# With tuples you can return multiple values in python
x, y, z = (1, 2, 3)

print(dir(a))  
print("Size of tuple:", sys.getsizeof(a))
print(id(a))   
print(id(b))   
print(a is b) # False
print("---------------")

####################################################################################
# Dictionary (key value pairs) (hash table) are mutable (json like)
a = {"A":10, "B":20, "C":30}
b = {"A":10, "B":20, "C":30} 
  
print(dir(a)) 
print("Size of dic:", sys.getsizeof(a))
print(id(a))   
print(id(b))   
print(a is b) # False
print("---------------")

####################################################################################
# To make python code faster use static typed Cython (used by numpy)
# Python by C-like static typing *.pyx

####################################################################################
# Operators + - * / % ** //

# Comparison Operators == != < > >= <=

# Assignment Operators = += -= *= /= %= **= //=

# Logical Operators and (&&) or (||) not (!)

# Memberships Operators in not in

# Identity Operators is is not

# Bitwise Operators & | ^ ~ << >>