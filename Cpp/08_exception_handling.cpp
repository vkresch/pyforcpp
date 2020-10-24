#include <iostream> 
#include <exception>
#include <assert.h>
  
int main() 
{ 
    int x = 5; 
    int y = 0;
    int z;

    assert(y != 0);
    
    try { 
        if (y == 0){ 
            throw "Divide by zero error";
        } 
        z = x / y;
    } catch (int x) { 
        std::cout << "Exception Caught x: " << x << std::endl; 
    } catch (const char* error) {
        std::cout << error << std::endl;
    } catch (std::exception& e) {
        std::cout << "Standard exception: " << e.what() << std::endl;
    } catch(...) {
        std::cout << "Any exception caught!" << std::endl;
    }

    std::cout << "Final line executed" << std::endl; 
    return 0; 
} 
