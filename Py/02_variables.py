####################################################################################
# Everything in python is an object and is dynamically checked at runtime (Reason for slow)
# int is an object not a real int like in C++

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

####################################################################################
# Strings
a = "first"
b = "first" 

print(id(a)) 
print(id(b)) 
print(a is b) # True

####################################################################################
# List are mutable
a = [10, 20, 30] 
b = [10, 20, 30] 
  
print(id(a)) 
print(id(b)) 
print(a is b) # False

####################################################################################
# Tuples are mutable and unique
a = (10, 20, 30, 30) # == (10, 20, 30)
b = (10, 20, 30) 
  
print(id(a))   
print(id(b))   
print(a is b) # False

####################################################################################
# Dictionary (key value pairs) (hash table) are mutable (json like)
a = {"A":10, "B":20, "C":30}
b = {"A":10, "B":20, "C":30} 
  
print(id(a))   
print(id(b))   
print(a is b) # False

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