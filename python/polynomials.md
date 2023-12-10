---
title: Numerical Methods for Polynomials
author: Jasper Day
---

Numpy's `roots` command states that it finds the eigenvalues of the "companion matrix" of the polynomial. What does this mean?

# Companion Matrix

The companion matrix of a polynomial

$$
P(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + ... + a_n x^n
$$

is that matrix $A$ *such that the characteristic polynomial* $\|A - \lambda I\|$ *is the polynomial which we wished to solve*. In other words, the eigenvalues of the matrix A are the roots of our polynomial.

In general, computers are good at finding the eigenvalues of matrices, much better than finding the roots of continuous problems.


