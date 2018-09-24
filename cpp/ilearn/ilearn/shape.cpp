#include "shape.h"
#include <iostream>

shape::shape()
{
    std::cout << "shape::shape" << std::endl;
}

shape::~shape()
{
    std::cout << "shape::~shape" << std::endl;
}

//double shape::calcArea()
//{
//    std::cout << "shape::calcArea" << std::endl;
//    return 0;
//}