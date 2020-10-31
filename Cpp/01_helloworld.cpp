#include <iostream>

// ####################################################################################
// Simple way run script
int main(){
    std::cout << "Hello World" << std::endl;
    return 0;
}

// ####################################################################################
// Pass arguments to main
int main(int argc, char *argv[]){
    std::cout << "Hello " << argv[1] << std::endl;
    return 0;
}