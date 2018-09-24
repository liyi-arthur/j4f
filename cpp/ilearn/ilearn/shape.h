#pragma once
class shape
{
public:
    shape();
    virtual ~shape();

    virtual double calcArea()=0;

protected:
    int   type;

private:
    int   id;
};

