#!/usr/bin/env python

# util.py

# Sequence converging utilities

def converge_rel_error(iterable, e_c, max_terms = 1_000_000_000):
    """
Given an iterable that converges on a number, computes successive values of the iterable until the fractional error term `e_a` is less than `e_c`

`e_a` is calculated as the relative difference between terms: `e_a` = (`A_curr` - `A_prev`)/(`A_curr`)

Halts if max_terms is exceeded (default value 1E9)

Returns a tuple `(result, terms)` of the result and the number of terms in the series taken to get there.
    """
    curr = next(iterable)
    # Test whether relative fractional error is acceptable
    pred = lambda A_prev, A_curr: abs((A_curr - A_prev)/A_curr) < abs(e_c)
    for terms in range(1, max_terms):
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return prev, terms
        # check if sequence is inside relative error
        if pred(prev, curr):
            break
    return curr, terms

def converge_abs_error(iterable, e_c, max_terms=1_000_000_000):
    """
Given an iterable that converges on a number, computes successive terms until the absolute difference between successive terms is less than some number `e_c`. 

Halts if max_terms is exceeded (default value 1E9)

Returns a tuple `(result, terms)` of the result and the number of terms in the series taken to get there.
    """
    curr = next(iterable)
    pred = lambda A_prev, A_curr: abs(A_curr - A_prev) < abs(e_c)
    for terms in range(1, max_terms):
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return curr, terms
        if pred(prev, curr):
            break
    return curr, terms

def abs_errors_seq(iterable):
    """
Given an iterable, returns a sequence of absolute errors (the difference between successive terms of the sequence)
    """
    curr = next(iterable)
    while True:
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return curr - prev
        yield curr - prev

def rel_errors_seq(iterable):
    """
Given an iterable, returns a sequence of relative errors
    """
    curr = next(iterable)
    error = lambda prev, curr: abs((curr - prev)/curr)
    while True:
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return error(prev, curr)
        yield error(prev, curr)


def converge_terms(iterable, n):
    """
    Given an iterable, returns the value after `n` iterations.
    """
    curr = next(iterable)
    for terms in range(1, n):
        try:
            curr = next(iterable)
        except StopIteration:
            break
    return (curr, terms)

# Math Utilities

def sign(x):
    """
    Returns the sign of a number x

    Raises TypeError on failure
    """
    try:
        if x == 0:
            # Note: sign(-0) = 0
            return 0
        if x > 0:
            return 1
        if x < 0:
            return -1
    except TypeError:
        raise TypeError(f"Attempted to calculate sign of {x}")
