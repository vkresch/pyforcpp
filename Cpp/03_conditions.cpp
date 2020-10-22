#include <iostream>

int main(){
    int a = 5;
    std::string message = "";

    if(a > 5){
        message = "Greater than 5";
    } else if(a == 4){
        // Btw there is no else if keyword just the combination :)
        message = "Equals to 4";
    } else {
        message = "Not Greater than 5 and not equal to 4";
    }
    std::cout << message << std::endl;

    // Short way notation Tenary Operators
    // Should be used for two outcomes to not make it complex

    //Example for two statements
    message = a > 5 ? "Greater than 5" : "Not Greater than 5";
    std::cout << message << std::endl;

    // Example for three statements
    message = a == 4 ? "Equals to 4" : a > 5 ? "Greater than 5" : "Not Greater than 5 and not equal to 4";
    std::cout << message << std::endl;

    return 0;
}

// Switch statement
std::string numbers_to_strings(int argument){
    std::string return_string = "nothing"; 
    switch(argument) {
      case 0 :
        return_string = "zero";
        break;
      case 1 :
        return_string = "one";
        break;
      case 2 :
        return_string = "two";
        break;
      default :
        return_string = "nothing";
   }
}