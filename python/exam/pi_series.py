"""
exam: 2022-2023
question: 1
"""

import math
from util import rel_errors_seq

def pi_series():
    "Iterable with successive approximations to pi"
    i = 0
    tot = 0
    while True:
        i += 1
        tot += 1/i**2 # sum from i=1 to infinity of 1/i^2
        yield math.sqrt(6*tot)

def take_n(iter, n):
    "return sequence value after n terms"
    for i in range(n):
        curr = next(iter)
    return curr

def rel_err(iter, n):
    "return relative error after n terms"
    curr = 0
    for i in range(n):
        prev = curr
        curr = next(iter)
    return (curr - prev)/curr

def ans_a():
    n = [10, 100, 1000]
    return [take_n(pi_series(), n_p) for n_p in n]

def ans_b():
    approxs = ans_a()
    true_err = [math.pi - x for x in approxs]
    n = [10, 100, 1000]
    rel_errs = [rel_err(pi_series(), n_p) for n_p in n]
    return {
        "true": true_err,
        "rel": rel_errs
    }

if __name__=="__main__":
    print(ans_a())
    print(ans_b())
