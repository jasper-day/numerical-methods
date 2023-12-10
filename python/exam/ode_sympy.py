from sympy import Function, dsolve, symbols, diff, exp, cos

x = Function('x')
t, m, k, b = symbols('t,m,k,b')

ode = m * x(t).diff(t,2) + b * x(t).diff(t) + k * x(t)

A0, omega, phi = symbols('A0, omega, phi')

soln = A0 * exp(-b*t/(2*m)) * cos(omega*t + phi)

ode.subs(x, soln)
