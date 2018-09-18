
#pragma once
#include "shape.h"
class rect :
    public shape
{
public:
    rect();
    ~rect();

    double calcArea();
};

