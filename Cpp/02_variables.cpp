#include <iostream>
#include <tuple>
#include <map>

int main(){
    // ####################################################################################
    // Int address
    int a = 42;
    int b = 42;
    std::cout << "Address a: " << &a << std::endl;
    std::cout << "Address b: " << &b << std::endl;

    // ####################################################################################
    // String address
    std::string c = "first";
    std::string d = "first";
    std::cout << "Address c: " << &c << std::endl;
    std::cout << "Address d: " << &d << std::endl;

    // ####################################################################################
    // Array or Vectors
    int array1[3] = {10, 20, 30};
    int array2[3] = {10, 20, 30};
    std::cout << "Address array1: " << array1 << std::endl;
    std::cout << "Address array2: " << array2 << std::endl;

    // ####################################################################################
    // Tuples
    std::tuple <char, int, float> tuple_a; 
    tuple_a = std::make_tuple('a', 10, 15.5); 

    // Printing initial tuple values using get() 
    std::cout << "The values of tuple_a are: "; 
    std::cout << std::get<0>(tuple_a) << ", " << std::get<1>(tuple_a); 
    std::cout << ", " << std::get<2>(tuple_a) << std::endl; 

    // ####################################################################################
    // Map
    std::map<std::string, int> a_dict;
    a_dict.insert(std::make_pair("A", 10));
    a_dict.insert(std::make_pair("B", 20));
    a_dict["C"] = 30;

    // Print the map dictionary
    std::map<std::string, int>::iterator it = a_dict.begin();
    while(it != a_dict.end()){
        std::cout << it->first << ": "<< it->second << std::endl;
        it++;
    }

    // And so on vectors and other containers
    // Vectors are more similar to python list since it has same kind of methods append push_back
    return 0;
}
