#pragma once
class shape
{
public:
    shape();
    virtual ~shape();

    virtual double calcArea();

protected:
    int   type;

private:
    int   id;
};

