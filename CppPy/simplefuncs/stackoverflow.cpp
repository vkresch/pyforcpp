// Embeding the interpreter into c++
// https://pybind11.readthedocs.io/en/master/advanced/embedding.html


#include <pybind11/embed.h>
#include <iostream>
#include <string>

// Define namespace for pybind11
namespace py = pybind11;

class Vehiclee
{ 
    // Access specifier 
    public: 
  
    // Data Members 
    int vehicle_id;
    std::string vehicle_name; 
    std::string vehicle_color;
      
    // Member Functions() 
    void printname() 
    { 
       std::cout << "Vehicle id is: " << vehicle_id; 
       std::cout << "Vehicle name is: " << vehicle_name; 
       std::cout << "Vehicle color is: " << vehicle_color; 
    } 
}; 


int main() {
    // Initialize the python interpreter
    py::scoped_interpreter python;

    // Import all the functions from scripts by file name in the working directory
    py::module simpleFuncs = py::module::import("simpleFuncs");   

    // Test if C++ objects can be passed into python functions
    Vehiclee car1;
    car1.vehicle_id = 1234;
    car1.vehicle_name = "VehicleName";
    car1.vehicle_color = "red";
    py::object car1 = py::cast(car1);   
    simpleFuncs.attr("simplePrint")(car1);
    
    return 0;
}