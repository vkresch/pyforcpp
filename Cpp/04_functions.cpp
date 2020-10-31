#include <iostream>
#include <vector>

// ####################################################################################
// # Simple function definiton
void say_hello(){
    std::cout << 

void say_hello(std::string& name){
    std::cout << "Hello " << name << std::endl;
}"Hello world!" << std::endl;
}

auto mean_manual(const std::vector<int>& seq){
    auto n = 0.0;
    for(auto x: seq)
        n += x;
    return n/seq.size(); // Copy return
}

// ####################################################################################
// Call by value/reference
auto string_value(std::string custom_string){
    custom_string = "New Assignment";
}

void string_reference(std::string& custom_string){
    custom_string = "New Assignment";
}

// ####################################################################################
// # Define a function pointer
auto(*other_mean_name)(const std::vector<int>& seq) = mean_manual;

void ForEach(const std::vector<int>& values, void(*func)(int)){
    for(int value: values){
        func(value);
    }
}

// ####################################################################################
// # Templates in python are implicit and builtin
template <typename T>
auto mean_template(const std::vector<T>& seq){
    auto n = 0.0;
    for(auto x: seq)
        n += x;
    return n/seq.size();
}

// ####################################################################################
// # Return multiple values
struct Ints {
    int a, b;
};

Ints multiple_values(const int& a, const int& b){
    Ints ints;
    ints.a = a;
    ints.b = b;    
    return ints;
}

// ####################################################################################
// # Lambda functions
auto mean_lambda = [](const std::vector<int>& seq){
    return reduce(par_unseq, begin(seq), end(seq))/seq.size();
};

// ####################################################################################
// # main function
int main(){
    std::vector<double> rvec = {1, 2 ,3, 4 ,5};
    std::cout << mean_template(rvec) << std::endl;

    Ints intret = multiple_values(1, 2);
    std::cout << intret.a << ", " << intret.b << std::endl;
    return 0;
}