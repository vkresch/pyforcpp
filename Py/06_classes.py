####################################################################################
# Class definition
# In python class works like a struct in C++, everything is public
# self is like this in C++
class Car:    
    def __init__(self, type_name):
        print('Constructor called.')
        self.type_name = type_name
        self.position_x = 0
        self.position_y = 0
        self.velocity = 0
        self.acceleration = 0

    def accelerate(self, value):
        self.acceleration += value

    # Dunder / Magic method which can be overwritten like __init__
    # https://docs.python.org/3/reference/datamodel.html
    def __del__(self):
        print('Destructor called, Car deleted.')

car = Car("BMW") 
print("Acceleration:", car.acceleration)
car.accelerate(20)
print("Acceleration:", car.acceleration)
del car
print("-----")

####################################################################################
# Encapsulation
# Python defines private/protected/public implicitly

class Person(object):
    def __init__(self, name, age): #constructor
        self._name = name
        #data members/ attributes
        self._age = age
        print(f"Created person {self._name}!")

    def get_person(self):
        # member function
        return f"<Person ({self._name}, {self._age})>"
        # return "<Person (%s, %s)>" % (self._name, self._age)

    def greet(self):
        print("Hi I am a normal person!")

    def __del__(self):
        print(f"Killing person {self._name} {self._age}!")

john = Person("John", 32)
 # john is an object of type Person
print("Type of Object:", type(john), "Memory Address:", id(john))
print(john.get_person())
print(john._name) # does not throw an error because _name is protected
# this is just a convention
del john
print("-----")

####################################################################################
# Inheritance
# - Inheritance indicates that one class derives (most of its) functionality from the parent class.
# - Inheritance is described as an option to reuse functionality defined in
# the base class and allow independent extensions of the original software
# implementation.
# - Inheritance creates hierarchy via the relationships among objects of different
# classes. Python, unlike Java, supports multiple inheritance (inheriting from
# multiple base classes). 
# Be careful of diamond problem:
# https://www.programmerinterview.com/c-cplusplus/diamond-problem/

class Student(Person):
    def __init__(self, name, age, idnumber):
        Person.__init__(self, name, age)
        self.__idnumber = idnumber 
        # self.__name = name # If private you need to specify it again
        # self.__age = age
        print(f"Created student {self._name}!")

    def get_student(self):
        return f"<Student ({self._name}, {self._age}, {self.__idnumber})>"

    def greet(self):
        print("Hi I am a student!")

    def __del__(self):
        super().__del__()
        print(f"Killing student {self._name} {self._age} {self.__idnumber}!")

student_jonny = Student("Jonny", 45, 123456)
print(student_jonny.get_person())
print(student_jonny.get_student())
# print(student_jonny.__idnumber) # throws an error
del student_jonny
print("-----")

####################################################################################
# Polymorphism
# Polymorphism can be of two types:
# - An object provides different implementations of the method based on input parameters
# - The same interface can be used by objects of different types

# In Python, polymorphism is a feature built-in for the language. For example,
# the + operator can act on two integers to add them or can work with strings
# to concatenate them
a = "John" + "huhuh" # string
b = (1,2,3) + (3, 2, 1) # tuple
c = [3,4,6,8,9] + [3, 2, 1]# list
d = 2 + 3
e = 2.32 + 3.14

class Teacher(Person):
    def __init__(self, name, age):
        self.__name = name # If private you need to specify it again
        self.__age = age
        print(f"Created teacher {self.__name}!")
        Person.__init__(self, name, age)

    def get_student(self):
        return f"<Teacher ({self.__name}, {self.__age})>"

    def greet(self):
        print("Hi I am a teacher!")

    def __del__(self):
        super().__del__()
        print(f"Killing teacher {self.__name} {self.__age}!")

def poly_func(person):
    person.greet()

anna = Student("Anna", 22, 654321)
peter = Teacher("Peter", 58)
poly_func(anna)
poly_func(peter)
del anna
del peter
print("-----")

####################################################################################
# Abstract Classes
# - It provides you with a simple interface to the clients, where the clients can
# interact with class objects and call methods defined in the interface
# - It abstracts the complexity of internal classes with an interface so that the
# client need not be aware of internal implementations

from abc import ABC, abstractmethod 
class Animal(ABC): 
  
    @abstractmethod
    def move(self): 
        pass
    
class Snake(Animal): 
  
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
  
    def move(self): 
        print("I can bark")   
          
snake = Snake() 
snake.move()  
dog = Dog() 
dog.move() 
# A = Animal() # throws an error
print("-----")

####################################################################################
# Composition
# - It is a way to combine objects or classes into more complex data structures or
# software implementations
# - In composition, an object is used to call member functions in other modules
# thereby making base functionality available across modules without
# inheritance

class Motor():
    count = 0 # Static type kind of

    def __init__(self):
        self.increment()
        self.rpm = 1000

    def start(self):
        print("Brrrrrrrrrrrr!")

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def decrement(cls):
        cls.count -= 1

    @staticmethod
    def info():
        print("This is a motor class!")

    @property
    def rpm_meth(self):
        if self.rpm > 100:
            return self.rpm
        else:
            raise Exception(f"RPM {self.rpm} is not higher than 100.")

    def __del__(self):
        self.decrement()

class Vehicle():
    def __init__(self):
        self.motor = Motor()

bmw = Vehicle()
bmw.motor.start()
bmw.motor.info()
print(bmw.motor.count)
print(bmw.motor.rpm_meth, "rpm") # Access like a property with error handling

# del bmw

audi = Vehicle()
audi.motor.start()
audi.motor.info()
print(audi.motor.count)
print("-----")

####################################################################################
# Decorators Explained
def myWrapper(func):
    def myInnerFunc():
        print("Inside wrapper.")
        func()
    return myInnerFunc
 
def myFunc():
    print("Hello from func!")
 
wrapped_myFunc=myWrapper(myFunc)
wrapped_myFunc()
print("--")

@myWrapper
def myFunc2():
    print("Hello from func2!")

myFunc2()
