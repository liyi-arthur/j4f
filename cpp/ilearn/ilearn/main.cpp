#include <iostream>
#include "circle.h"

void testVirtual()
{
    shape* s1 = new circle();
    s1->calcArea();
    delete s1;
}

int main(int argc, void* argv[])
{
    std::cout << "Welcome to ilearn!" << std::endl;

    testVirtual();
    return 0;
}