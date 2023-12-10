#!/usr/bin/env python

from itertools import takewhile, islice, starmap
from util import converge_error

def exp_maclaurin(x):
    """
    Returns an infinite sequence of successive terms in the maclaurin expansion of e^x
    """
    next_term = next_part = n = 1
    while True:
        yield next_term
        # x^n / n!
        next_part *= x/n
        # summation of x^n/n!
        next_term += next_part
        n += 1

def exp_maclaurin_err(x, e_c):
    """
    Given a point x and an acceptable error cutoff e_c, computes exp(x) at that point, convergent within e_c
    """
    gen = exp_maclaurin(x)
    result, terms = converge_rel_error(gen, e_c)
    return result
