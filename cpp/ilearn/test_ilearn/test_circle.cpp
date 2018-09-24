//test.cpp²âÊÔº¯Êý
#include "gtest/gtest.h"
#include "circle.h"

TEST(test_circle, case1)
{
    circle  c;
    EXPECT_EQ(0, c.calcArea());
}

