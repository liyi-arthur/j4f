#include <iostream>
#include "circle.h"
#include "rect.h"

void testVirtual()
{
    shape* s1 = new circle();
    shape* s2 = new rect();

    s1->calcArea();
    s2->calcArea();

    delete s1;
    delete s2;
}

int main(int argc, void* argv[])
{
    std::cout << "Welcome to ilearn!" << std::endl;

    testVirtual();
    return 0;
}