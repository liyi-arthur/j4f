#include "rect.h"
#include <iostream>

rect::rect()
{
    std::cout << "rect::rect" << std::endl;
}

rect::~rect()
{
    std::cout << "rect::~rect" << std::endl;
}

double rect::calcArea()
{
    std::cout << "rect::calcArea" << std::endl;
    return 0;
}