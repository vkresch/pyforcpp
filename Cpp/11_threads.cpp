#include <string>
#include <iostream>
#include <thread>
#include <vector>
#include <unistd.h>

// First Method
void greet_them(std::vector<std::string> people){
    for(std::string person : people){
        std::cout << "Hello Dear " << person << ". How are you?" << std::endl;
        sleep(1);
    }
}

// Second Method
void assign_id(std::vector<std::string> people){
    int i = 1;
    for(std::string person : people){
        std::cout << "Hey! "<< person <<", your id is "<< i << "." << std::endl;
        i++;
        sleep(1);
    }
}

// How to pass by reference: 
// https://stackoverflow.com/questions/34078208/passing-object-by-reference-to-stdthread-in-c11

int main()
{
    // Constructs the new thread and runs it. Does not block execution.
    std::vector<std::string> people = {"Richard", "Dinesh", "Elrich", "Gilfoyle", "Gevin"};

    // Create the threads
    std::thread t1(greet_them, people);
    std::thread t2(assign_id, people);

    // Makes the main thread wait for the new thread to finish execution, therefore blocks its own execution.
    t1.join();
    t2.join();
}