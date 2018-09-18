#pragma once
#include "shape.h"
class circle :
    public shape
{
public:
    circle();
    ~circle();

    double calcArea();
};

