#include "circle.h"
#include <iostream>

circle::circle()
{
    std::cout << "circle::circle" << std::endl;
}

circle::~circle()
{
    std::cout << "circle::~circle" << std::endl;
}

double circle::calcArea()
{
    std::cout << "circle::calcArea" << std::endl;
    return 0;
}