#include <iostream>

#include <cppoptlib/solver/bfgssolver.h>

int main() {
    const cppoptlib::BfgsSolver<cppoptlib::Problem<double>> scalar;
    std::cout << "The CppNumericalSolversPackageTest ran." << std::endl;
}
