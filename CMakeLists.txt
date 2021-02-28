cmake_minimum_required(VERSION 3.8)
project(CppNumericalSolvers)

add_definitions("-std=c++14")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(${PROJECT_SOURCE_DIR}/include)
