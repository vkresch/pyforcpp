####################################################################################
# while loop (similar C++ loop)
array = [1, 2, 3] # list
j = 0
while j < 3:
    print(array[j])
    j += 1
print("----")

####################################################################################
# for loop
# Non pythonic way
for i in range(0, len(array)):
    print(array[i])
print("----")

# iterate over range
for el in array:
    print(el)
print("----")

for idx, el in enumerate(array):
    print(idx, ":",el)
print("----")

# iterate over dictionary
dic = {0: "zero", 1: "one", 2: "two"}
for key, value in dic.items():
    print(key, ":", value)
print("----")

# no do while loops but like switch statements they can be emulated

####################################################################################
# Difference between an iterator and a generator
def simple_generator_function():
    for i in range(3):
        yield i

generator = simple_generator_function()
generator2 = simple_generator_function()
# iterate over generator (efficient)
for g1 in generator:
    print(g1) # Generates element and deletes it

# You cant iterate twice over a generator
# This would print nothing since the generator is void
for g2 in generator:
    print(g2)

# Create an iterator
iterator = list(generator2) # deep copy of an generator to an iterator
print(iterator)
print("----")
####################################################################################
# List/Dict Comprehension optimization
# Get all the even numbers from the list
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list_normal = []
for el in example_list:
    if el % 2 == 0:
        even_list_normal.append(el)
print(even_list_normal)

# Equivalent and more efficient way to populate list
# List comprehension
even_list_comprehension = [el for el in example_list if el % 2 == 0] 
print(even_list_comprehension)
print("----")

# Generator comprehension
even_generator_comprehension = (el for el in example_list if el % 2 == 0)
print(even_generator_comprehension)
print("----")

# Tuple comprehension
even_generator_tuple = tuple(el for el in example_list if el % 2 == 0)
print(even_generator_tuple)
print("----")

# Dictionary comprehension
example_dict = {1: "A", 2: "B", 3: "C", 4: "D"}
even_list_comprehension = {key:el for key, el in example_dict.items() if key % 2 == 0}
print(even_list_comprehension)
print("----")

####################################################################################
# Improve performance of loops via ctypes (Outlook pybind11)