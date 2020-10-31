# PyWrapper
### Preparation
```
mkdir projectName
cd projectName
git clone https://github.com/pybind/pybind11
sudo apt-get install virtualenv
virtualenv vpython python3
source vpython/bin/activate
pip install pybind11
```

### Code
- write your python functions in different files ```intFuncs.py, floatFuncs.py, stringFuncs.py, ...```
```
def doadd(a, b):
    return a+b

def dosub(a, b):
    return a-b

def domul(a, b):
    return a*b

def dodiv(a, b):
    return a/b

def doconcatenate(a, b):
    return a + b

...
```
- write your ```main.cpp```
```
// Embeding the interpreter into c++
// https://pybind11.readthedocs.io/en/master/advanced/embedding.html

#include <pybind11/embed.h>
#include <iostream>
#include <string>

// Define namespace for pybind11
namespace py = pybind11;
using namespace pybind11::literals;

// Define a struct for testing
struct Person
{
    std::string name;
    int age;
    float salary;
};


int main() {
    // Initialize the python interpreter
    py::scoped_interpreter python;

    // ###################################################################
    // IMPORT
    // ###################################################################

    // Import all the functions from scripts by file name in the working directory
    py::module intFuncs = py::module::import("intFuncs");
    py::module floatFuncs = py::module::import("floatFuncs");
    py::module stringFuncs = py::module::import("stringFuncs");
    py::module arrayFuncs = py::module::import("arrayFuncs");
    py::module classFuncs = py::module::import("classFuncs");
    
    // ###################################################################
    // INPUT
    // ###################################################################

    // Execute all the functions from C++
    py::object result = intFuncs.attr("doadd")(1, 2);
    py::object result2 = floatFuncs.attr("dodiv")(9, 2);
    py::object result3 = stringFuncs.attr("doconcatenate")("My name is ", "Tester");
    std::cout << "\n-------------------------------- \n";

    // Tuple - Just iterate a tuple
    auto atuple = py::make_tuple(1234, "hello", "hello", "hello");    
    arrayFuncs.attr("iterateList")(atuple);
    std::cout << "-------------------------------- \n";

    // List - Just iterate a list
    // TODO Find a way to create a list from the start
    py::list alist = py::make_tuple("Jim", "Spock", 2);
    arrayFuncs.attr("iterateList")(alist);
    std::cout << "-------------------------------- \n";

    // Dict - Just iterate the keys form a dict with the same list function 
    auto adict = py::dict("Jim"_a=1, "Spock"_a=2);
    arrayFuncs.attr("iterateList")(adict);
    std::cout << "-------------------------------- \n";

    // Testing if methods and attributes can be accessed
    py::object Vehicle = classFuncs.attr("Vehicle"); // Equivalent to "from classFuncs import Vehicle"
    py::object car = Vehicle();
    py::object vehiclename = car.attr("getName")();
    py::object vehiclename2 = car.attr("name");

    // Test if structs can be passed as arguments to python functions
    Person p1;
    p1.name = "Tester";
    p1.age = 25;
    p1.salary = 1000.123;
    auto alist2 = py::make_tuple(p1.name, p1.age, p1.salary);
    arrayFuncs.attr("iterateList")(alist2);
    std::cout << "-------------------------------- \n";


    // ###################################################################
    // OUTPUT
    // ###################################################################

    // Make a casting from python objects to real C++ Types
    int n = result.cast<int>();
    float n2 = result2.cast<float>();
    std::string n3 = result3.cast<std::string>();
    std::string name = vehiclename.cast<std::string>();
    std::string name2 = vehiclename2.cast<std::string>();

    // Print out the results to the console
    std::cout << "1 + 2 = " << n << "\n";
    std::cout << "9 / 2 = " << n2 << "\n";
    std::cout << n3 << "\n";
    std::cout << "productname: " << name << "\n";
    std::cout << "productname: " << name2 << "\n";


    return 0;
}
```

### Compile
- write a ```touch CMakeLists.txt```
```
cmake_minimum_required(VERSION 3.0)
project(projectName)
add_subdirectory(pybind11)
add_executable(projectName main.cpp)
target_link_libraries(projectName PRIVATE pybind11::embed)
```

- run these commands to compile and execute the source code
```
cmake .
make
./projectName
```
