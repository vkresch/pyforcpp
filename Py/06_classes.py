####################################################################################
# Class definition
class Car:    
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.velocity = 0
        self.acceleration = 0

    def accelerate(self, value):
        self.acceleration += value

    def __del__(self):
        print('Destructor called, Car deleted.')

car = Car() 
car.accelerate(10)
car.accelerate(4)
print(car.acceleration)
del car 

####################################################################################
# Encapsulation
# Python defines private/protected/public implicitly

class Person(object):
    def __init__(self, name, age): #constructor
        self.__name = name
        #data members/ attributes
        self.__age = age
    def get_person(self,):
        # member function
        return "<Person (%s, %s)>" % (self.__name, self.__age)

p = Person("John", 32)
 # p is an object of type Person
print("Type of Object:", type(p), "Memory Address:", id(p))
print(p.get_person())
# print(p.__name) # throws an error 

####################################################################################
# Polymorphism
# Polymorphism can be of two types:
# - An object provides different implementations of the method based on input parameters
# - The same interface can be used by objects of different types

# In Python, polymorphism is a feature built-in for the language. For example,
# the + operator can act on two integers to add them or can work with strings
# to concatenate them
a = "John" # string
b = (1,2,3) # tuple
c = [3,4,6,8,9] # list
print(a[1], b[0], c[2])

####################################################################################
# Inheritance
# - Inheritance indicates that one class derives (most of its) functionality from the parent class.
# - Inheritance is described as an option to reuse functionality defined in
# the base class and allow independent extensions of the original software
# implementation.
# - Inheritance creates hierarchy via the relationships among objects of different
# classes. Python, unlike Java, supports multiple inheritance (inheriting from
# multiple base classes).

class A:
    def a1(self):
        print("a1")
        
class B(A):
    def b(self):
        print("b")
b = B()
b.a1()

####################################################################################
# Abstraction
# - It provides you with a simple interface to the clients, where the clients can
# interact with class objects and call methods defined in the interface
# - It abstracts the complexity of internal classes with an interface so that the
# client need not be aware of internal implementations

class Adder:
    def __init__(self):
        self.sum = 0
    def add(self, value):
        self.sum += value

acc = Adder()
for i in range(99):
    acc.add(i)
print(acc.sum)


####################################################################################
# Composition
# - It is a way to combine objects or classes into more complex data structures or
# software implementations
# - In composition, an object is used to call member functions in other modules
# thereby making base functionality available across modules without
# inheritance

class A(object):
    def a1(self):
        print("a1")

class B(object):
    def b(self):
        print("b")
        A().a1()

objectB = B()
objectB.b()

####################################################################################
# this is self in python
# s.addCourse(3, 2.5) is like Student::addCourse(&s, 3, 2.5) (S.183 C++ for dummies)



####################################################################################
# static methods and class variables

####################################################################################
# constructors and destructors