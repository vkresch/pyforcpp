####################################################################################
# Simple function definiton
def say_hello():
    print("Hello world!")

# Explicit type definition and return definition
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

def mean_manual(seq):
    n = 0.0
    for x in seq:
        n += x
    return n/len(seq)

def mean_builtin(seq):
    return sum(seq)/len(seq)

# Prototyping is not needed

####################################################################################
# Call by Object Reference/assignment example
# https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/

# Call by value (immutable objects)  
string = "Global String"
  
def string_value(custom_string):      
    custom_string = "New Assignment"

def string_reference(object_custom_string):      
    object_custom_string.custom_string = "New Assignment"

# Call by reference (mutable objects)
class StringsType:
    def __init__(self, passed_string):
        self.custom_string = passed_string

mystring = StringsType(string)
print(mystring.custom_string)
string_reference(mystring)
print(mystring.custom_string) # "New Assignment"
print(mystring) # <__main__.StringsType object at 0x7f7078cf2da0>


####################################################################################
# Pass function address and run
other_mean_name = mean_manual
print(mean_manual) # <function mean_manual at 0x7f7078cfa0d0>

def ForEach(values, func):
    for value in values:
        func(value)


####################################################################################
# Python decorators (-> see 06_classes file)

####################################################################################
# Templates in python are implicit and builtin
# Means calculation of float or int are already considered

####################################################################################
# Return multiple values
def multiple_values(a, b):
    return a, b

c, d = multiple_values(1, 2)

####################################################################################
# Lambda functions
mean = lambda seq: sum(seq) / len(seq)

####################################################################################
# yield statement generate a Generator (yield does not break out of function like return)
def simple_generator_function():
    for i in range(3):
        yield i

generator = simple_generator_function()
print(generator) # <generator object simple_generator_function at 0x7fe0995fccf0>
# Iterate over generator (efficient)
# Iterators are list, tuples, ...
# Difference between iterator and generator is that generator frees memory on runtime
for g in generator:
    print(g) # Generates element and deletes it

####################################################################################
# main function
def main():
    rvec = [1, 2, 3, 4, 5]
    print(mean_manual(rvec))

if __name__=="__main__":
    main()