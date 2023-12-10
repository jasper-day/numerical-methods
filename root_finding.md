---
title: Root Finding
author: Jasper Day
date: Wed Sep 20
---

Root finding (of continuous, but potentially non-linear functions) is a pretty fundamental numeric method, and demonstrates a lot of important properties of numeric algorithms, particularly convergence speed.

# Bisection Method

Simple: Start with two points on a C1 continuous function. One is positive, one is negative. Since the function is continuous, it must pass through zero somewhere between those points.

Next, compute the value of the function at the point halfway between the starting points. Now you have three known points in the functions. Select the midpoint and whichever starting point has the opposite sign to the function, and repeat the process.

See [[python/root_finding_bisection]] for example code.

The bisection method is quick and dirty and often pretty good, but it can be improved.

# False Position Method

Here, we actually use the function values at the endpoints, and instead of simply taking the midpoint of the function every time, we model the function as a straight line between the endpoints. Since the function values at the endpoints are of opposite signs, that straight line will pass through zero at some point.

For points x1 and x2 with values y1 and y2, the straight line through them is given by 

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)
$$

which passes through $y=0$ at 

$$
x = x_1 - y_1\frac{x2 - x1}{y_2 - y_1}
$$

Substitute this guess for the midpoint, and the series should converge faster.
