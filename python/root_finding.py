#!/usr/bin/env python

from util import sign

def test_endpoints(y1, y2):
    if sign(y1) == sign(y2):
        raise Exception(f"Cannot find root between {x1} and {x2}: function has same sign")


def naive_seq(f, x, dx):
    """
Silly little root finder. Just keeps walking along the function `f`, starting at the initial point `x`, incrementing by `dx`.
    """
    y = f(x)
    while True:
        if y == 0:
            return x
        else:
            # Assume all functions are increasing.
            x -= sign(y) * dx
        yield x

def bisection_seq(f, x1, x2):
    """
Given a function `f` of one variable and points `x1` and `x2` where `f(x)` has opposite signs, returns a sequence of points that converges to a root using the bisection method.
    """
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    while True:
        midpoint = (x1 + x2)/2
        y_midpoint = f(midpoint)

        if y_midpoint == 0:
            return midpoint

        if sign(y_midpoint) != sign(y1):
            x1, x2 = x1, midpoint
            # avoid unnecessary function calls
            y1, y2 = y1, y_midpoint 
        else:
            # guaranteed to be one or the other
            x1, x2 = midpoint, x2
            y1, y2 = y_midpoint, y2
        yield midpoint

def false_pos_seq(f, x1, x2):
    """
Given a function `f` of one variable and points `x1` and `x2` where `f(x)` has opposite signs, returns a sequence of points that converges to a root using the false position method.
    """
    y1, y2 = f(x1), f(x2)
    # make sure that endpoints are opposite signs
    test_endpoints(y1, y2)
    while True:
        false_root = (x1 * y2 - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)

        if y_false_root == 0:
            return false_root

        yield root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            y1, y2 = y1, y_false_root
        else:
            x1, x2 = false_root, x2
            y1, y2 = y_false_root, y2

def secant_seq(f, x1, x2):
    "Open root-finding method. Not guaranteed to converge."
    y1, y2 = f(x1), f(x2)
    while True:
        root = (x1 * y2 - x2 * y1)/(y2 - y1)
        y_root = f(root)
        if y_root == 0:
            return y_root
        yield root
        x1 = x2
        y1 = y2
        x2 = root
        y2 = y_root


        


def false_illinois_seq(f, x1, x2):
    """
Modified false position root solver, using the Illinois algorithm
    """
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    y_false_root_prev = 0
    while True:
        false_root = (x1 * y2  - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)
        if y_false_root == 0:
            return false_root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            if sign(y_false_root_prev) == sign(y_false_root):
                # Illinois addition: halve retained root
                y1, y2 = 0.5*y1, y_false_root
            else:
                y1, y2 = y1, y_false_root
        else:
            x1, x2 = false_root, x2
            if sign(y_false_root_prev) == sign(y_false_root):
                # Illinois addition
                y1, y2 = y_false_root, 0.5*y2
            else:
                y1, y2 = y_false_root, y2
        yield false_root
        y_false_root_prev = y_false_root
        
def false_bjorck_seq(f, x1, x2):
    """
Modified false position root solver, using the Anderson-Bjorck algorithm
    """
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    while True:
        false_root = (x1 * y2  - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)
        if y_false_root == 0:
            return false_root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            mod_term_p = 1 - y_false_root/y2
        else:
            x1, x2 = false_root, x2
        yield false_root

# open methods
# these require only one point to get started
# more calculus

def step_seq(f, u_0):
    "Creates a sequence of repeated applications of f to u_0"
    u = u_0
    while True:
        u = f(u)
        yield u
    

def newton_step(g, J, u_curr):
    "function g(u), jacobian matrix J(u), current guess u_curr"
    u_next = u_curr - solve(J(u), g(u))
    return u_next

def modified_newton(g, J_0, u_curr):
    "function g(u), initial jacobian matrix J_0 = J(u_0), current guess u_curr"
    u_next = u_curr - solve(J_0, g(u))
    return u_next

def damped_newton_step(g, J, alpha, u_curr):
    "reduce newton step to alpha * delta u"
    delta_u = - solve(J(u), g(u))
    return u_curr + alpha * delta_u

