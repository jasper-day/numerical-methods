"Various implementations of Newton's method"

# desired system to solve: g(u) = 0
# iterative method: start with guess u_0
# at each step improve u_curr to u_next
# compute jacobian matrix J_ij = partial g_i / partial u_j
# this provides linear approximation
# g(u) ~ g(u_k) + J(u_k) (u - u_k)
# see spivak calculus on manifolds
# to get g(u) = 0, use linear approximation and solve
# g(u_k) + J(u_k) (u - u_k) = 0
# u = J_k^inv(g_k - J_k(u_k))

import numpy as np

def solve(a, b):
    "Solve ax=b for scalar or matrix a and b"
    if type(a) == np.ndarray and a.ndim == 2:
        return np.linalg.solve(a,b)
    else:
        return b/a


def golden_ratio_seq(f, x_l, x_u):
    """Simple bracketing search, no derivatives required
    Find an maximum of f(x) between endpoints x_l and x_u
    Returns an iterable sequence of (x_approx, y_approx, error)
    """
    # set up the loop
    phi = np.sqrt(5)/2 - 1/2 # golden ratio
    x_1 = x_l + phi * (x_u - x_l) # phi is greater than 1/2, so this is closer to the upper point x_u
    x_2 = x_u - phi * (x_u - x_l) # closer to x_l
    y_1 = f(x_1)
    y_2 = f(x_2)
    def error(x_l, x_u, x_opt):
        return (1 - phi)*abs((x_u-x_l)/x_opt)
    while True:
        # each iteration of the loop calculates one new bracketing point
        if y_1 > y_2:
            yield x_1, y_1, error(x_l, x_u, x_1)
            # discard points to the left of x2
            x_l = x_2
            x_2 = x_1
            y_2 = y_1
            # calculate new point
            x_1 = x_l + phi * (x_u - x_l)
            y_1 = f(x_1)
        else: # y2 > y1, choose y2 as the approximation to maximum
            yield x_2, y_2, error(x_l, x_u, x_1)
            # discard points to the right of x1
            x_u = x_1
            x_1 = x_2
            y_1 = y_2
            # calculate new point
            x_2 = x_u - phi * (x_u - x_l)
            y_2 = f(x_2)


def 





            



        
        






