#This program contains functions that evaluate formulas used in geometry
#
#Connor Whiteside
#August 30, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))


def parallelogram_area(b,h):
    a = b * h
    return a

def trapeziod_area(a,b,h):
    a = a + b / 2 * h
    return a

def volume_prism(l,w,h):
    v = 1/2 * l * w * h
    return v

def volume_cone(r,h):
    v = math.pi * r ** 2 * h / 3
    return v

def volume_sphere(r):
    v = 4 / 3 * math.pi * r ** 3
    return v

def sa_rectangular_prism (w,l,h):
    a = 2 * (w * l + h * l + h * w)
    return a
    
def sa_sphere(r):
    a = 4 * math.pi * r ** 2
    return a

def hyp_triangle(a,b):
    c = a ** 2 + b ** 2
    return c**(1/2)

def herons_formula (a,b,c):
    s = (a + b + c)/2
    return math.sqrt (s * (s - a) * (s - b) * (s - c)) 
