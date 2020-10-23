#include <iostream>

// ####################################################################################
// class/struct definition
class Car {
    public:
        Car(std::string type_name) : m_type_name(type_name) {
            std::cout << "Car constructor called." << std::endl;   
        }
        virtual ~Car(){
            std::cout << "Car destructor called, Car deleted." << std::endl;           
        }
        std::string m_type_name = "default type";
        float position_x = 0.0f;
        float position_y = 0.0f;
        float velocity = 0.0f;
        float acceleration = 0.0f;

        void accelerate(const float& value){
            acceleration += value;
        }
};

// ####################################################################################
// # Encapsulation
// # Python defines private/protected/public implicitly
class Person {
    public:
        Person(const std::string& name, const int& age) : m_name(name), m_age(age){
            std::cout << "Creating person " << m_name << "." << std::endl;
        }
        virtual ~Person(){
            std::cout << "Killing person " << m_name << "." << std::endl;
        }
        std::string get_person(){
            std::string str_age = std::to_string(m_age);
            return "<Person (" + m_name + ", " + str_age + ")>";
        }
        virtual void greet(){
            std::cout << "Hi I am a normal person!" << std::endl;
        };
    protected:
        std::string m_name;
        int m_age;
};

// ####################################################################################
// Inheritance
// Be careful of diamond problem:
// https://www.programmerinterview.com/c-cplusplus/diamond-problem/
class Student : public Person {
    public:
        Student(const std::string& name, const int& age, const int& idnumber)
        : Person(name, age), m_idnumber(idnumber){
            std::cout << "Created student " << m_name << std::endl;
        }
        ~Student(){
            std::cout << "Killing student " << m_name << " " << m_age << " " << m_idnumber << std::endl;
        }
        std::string get_student(){
            std::string str_age = std::to_string(m_age);
            std::string str_idnumber = std::to_string(m_idnumber);
            return "<Student (" + m_name + ", " + str_age + ", " + str_idnumber + ")>";
        }
        void greet(){
            std::cout << "Hi I am a student!" << std::endl;
        }
    protected:
        int m_idnumber;
};

// ####################################################################################
// # Polymorphism

class Teacher : public Person {
    public:
        Teacher(const std::string& name, const int& age)
        : Person(name, age){
            std::cout << "Created teacher " << m_name << std::endl;
        }
        ~Teacher(){
            std::cout << "Killing teacher " << m_name << " " << m_age << std::endl;
        }
    void greet(){
            std::cout << "Hi I am a teacher!" << std::endl;
        }
};

void poly_func(Person* person){
    person->greet();
}

// ####################################################################################
// # Abstract Classes
class Animal {
    public:
        virtual void move() = 0;
};

class Snake : public Animal {
    public:
    void move(){
        std::cout << "I can crawl" << std::endl;
    }
};

class Dog : public Animal {
    public:
    void move(){
        std::cout << "I can bark" << std::endl;
    }
};

// ####################################################################################
// Composition
class Motor {
    public:
        static int count;
        Motor(){
            ++count;
        }
        ~Motor(){
            --count;
        }
        void start(){
            std::cout << "Brrrrrrrrrrrr!" << std::endl;
        }
        static int howMany(){
            return count; 
        }
};

// Initialize static member of class Motor
int Motor::count = 0;

class Vehicle {
    public:
        Motor motor;
};

int main(){
    // Stack allocation
    // Car car = Car("BMW");
    // Car car("BMW");
    // Car(&car, "BMW"); // the self is like the address to the object in C++

    // Heap allocation
    Car* car = new Car("BMW");
    std::cout << "Acceleration: " << car->acceleration << std::endl;
    car->accelerate(20); // Car::accelerate(&car, 20);
    std::cout << "Acceleration: " << car->acceleration << std::endl;
    delete car;
    std::cout << "-----" << std::endl;

    // ####################################################################################
    // Encapsulation
    Person* john = new Person("John", 32);
    std::cout << "Memory Address: " << john << std::endl;
    std::cout << john->get_person() << std::endl;
    // std::cout << john->m_name << std::endl; // throws an error because m_name is private
    delete john;
    std::cout << "-----" << std::endl;

    // ####################################################################################
    // Inheritance
    Student* student_jonny = new Student("Jonny", 45, 123456);
    std::cout << student_jonny->get_person() << std::endl;
    std::cout << student_jonny->get_student() << std::endl;
    delete student_jonny;
    std::cout << "-----" << std::endl;

    // ####################################################################################
    // Polymorphism
    Person* anna = new Student("Anna", 22, 654321);
    Person* peter = new Teacher("Peter", 58);
    std::cout << anna->get_person() << std::endl;
    poly_func(anna);
    poly_func(peter);
    delete anna;
    delete peter;
    std::cout << "-----" << std::endl;

    // ####################################################################################
    // Abstract classes
    Snake* snake = new Snake(); 
    snake->move();
    delete snake;

    Dog* dog = new Dog();
    dog->move();
    delete dog;
    // Animal animal(); // Throws an error instance of abstract class not allowed
    std::cout << "-----" << std::endl;

    // ####################################################################################
    // Composition
    Vehicle* bmw = new Vehicle();
    bmw->motor.start();
    std::cout << bmw->motor.count << std::endl;
    // delete bmw;

    Vehicle* audi = new Vehicle();
    audi->motor.start();
    std::cout << audi->motor.count << std::endl;
    delete audi;

    return 0;
}