cmake_minimum_required(VERSION 3.0)
project(wrapper)
add_subdirectory(pybind11)
add_executable(wrapper main.cpp)
file(GLOB PYTHON_FILES "*.py")
file(COPY ${PYTHON_FILES} DESTINATION .)
target_link_libraries(wrapper pybind11::embed)