#include <iostream>
#include <array>

int main(){
    // ####################################################################################
    // Iterate an array in a while loop
    int array[3] = {1, 2, 3}; 
    int j = 0;
    while(j < 3){
        std::cout << array[j] << std::endl;
        j++;
        continue;
        std::cout << "Gets never executed!!" << std::endl;
    }
    std::cout << "----" << std::endl;

    // ####################################################################################
    // Iterate an array in a for loop
    for(int i=0; i<3; i++){
        std::cout << array[i] << std::endl;
        break; // break out of the loop
    }
    std::cout << "----" << std::endl;

    // ####################################################################################
    // Iterate over a range in for loop (vector, map)
    std::array<int, 5> rvec = {1, 2 ,3, 4 ,5};
    for (auto it = rvec.begin(); it != rvec.end(); ++it){
        std::cout << *it << std::endl;
    }
    std::cout << "----" << std::endl;

    // ####################################################################################
    // Loop over container elements (vector, map)    
    for(int& element: rvec){
        std::cout << element << std::endl;
    }
    return 0;
}