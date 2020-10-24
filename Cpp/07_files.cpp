#include <iostream>
#include <fstream>

int main() {
    // Create and open a text file
    std::ofstream myFile("filename.txt");

    // Write to the file
    myFile << "Files can be tricky, but it is fun enough!";

    // Close the file
    myFile.close();

    // Create a text string, which is used to output the text file
    std::string myText;

    // Read from the text file
    std::ifstream myReadFile("filename.txt");

    // Use a while loop together with the getline() function to read the file line by line
    while (getline (myReadFile, myText)) {
        // Output the text from the file
        std::cout << myText;
    }

    // Close the file
    myReadFile.close(); 
} 