#include <iostream>
#include "circle.h"
#include "rect.h"
#include "base.h"

void testVirtual()
{
    shape* s1 = new circle();
    shape* s2 = new rect();

    base  b1;

    std::cout << typeid(*s1).name() << std::endl;
    std::cout << typeid(*s2).name() << std::endl;

    std::cout << (typeid(*s1) == typeid(*s2)) << std::endl;

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