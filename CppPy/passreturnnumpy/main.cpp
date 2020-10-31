// Embeding the interpreter into c++
// https://pybind11.readthedocs.io/en/master/advanced/embedding.html

#include <pybind11/embed.h>
#include <pybind11/eigen.h>
#include <pybind11/numpy.h>
#include <iostream>
#include <string>
#include <eigen3/Eigen/Dense>

// Define namespace for pybind11
namespace py = pybind11;
using namespace pybind11::literals;

// using MatrixXdR = Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>;


int main() {
    // Initialize the python interpreter
    py::scoped_interpreter python;

    // Import all the functions from scripts by file name in the working directory
    py::module numpyfunc = py::module::import("numpyfuncs");

    // Initialize matrices
    Eigen::MatrixXf a(2,2);
    a << 1.2, 2.2,
        3.1, 4.1;
    Eigen::MatrixXf b(2,2);
    b << 2.1, 3.3,
        1.1, 4.1;
    
    // Call the python function
    py::object result = numpyfunc.attr("add_arrays")(a, b);

    // Eigen::MatrixXf d = Eigen::Ref<const MatrixXdR>(result);

    // Make a casting from python objects to real C++ Eigen Matrix type
    Eigen::MatrixXd c = result.cast<Eigen::MatrixXd>();
    std::cout << "Here is the matrix c:\n" << c << std::endl;

    return 0;
}