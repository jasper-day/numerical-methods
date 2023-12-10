"""
exam: 2022
question: 2
"""

import math
from functools import partial
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
np.seterr(all='raise') # catch overflow errors

dy_dt = lambda y: 10*y**2 - y**3

def euler_step(y, dy_dt, dt):
    "ydot = dy_dt(y)"
    return y + dy_dt(y) * dt

def integrate_euler(y0, dy_dt, t, dt):
    ts = np.arange(0,t,dt)
    ys = np.zeros_like(ts)
    ys[0] = y0
    for i in range(1,len(ys)):
        ys[i] = euler_step(ys[i-1], dy_dt, dt)
    return {
        "h": dt,
        "y0": y0,
        "t": ts,
        "y": ys
    }

def a():
    y0 = 0.02
    hs = np.arange(0.0001, 0.04, 0.00001)
    res = []
    for h in hs:
        try:
            res_h = integrate_euler(y0, dy_dt, t=10, dt=h) 
        except FloatingPointError:
            # since the equation is stiff, a too-large timestep will generally overflow
            print(str(h) + " skipped due to overflow")
            continue
        res.append(res_h) 
    return res

def b():
    y0s = [0.02, 0.01, 0.005]
    h = 1e-4
    res = []
    for y0 in y0s:
        try:
            res_y = integrate_euler(y0, dy_dt, t=30, dt=h) 
        except FloatingPointError:
            # since the equation is stiff, a too-large timestep will generally overflow
            print(str(y0) + " skipped due to overflow")
            continue
        res.append(res_y)
    return res


def abs_error(res1, res2):
    y1 = res1["y"]
    y2 = res2["y"]
    if len(y1) > len(y2):
        return None
    skip = math.ceil(len(y2) / len(y1))
    r2 = y2[0:-1:skip]
    r1 = y1[0:len(r2)]
    return np.average(np.abs(r2 - r1))

if __name__ == "__main__":
    res_a = a()
    for result in res_a:
        plt.plot(result["t"], result["y"], label=result["h"])
    #plt.legend()
    plt.title("Simulation result (part A)")
    plt.xlabel("Time $t$ [s]")
    plt.ylabel("Combustion front radius $y(t)$")
    plt.savefig('ignition.png')
    plt.gca().clear()
    for i in range(1, len(res_a)):
        err = abs_error(res_a[i-1], res_a[i])
        plt.scatter(res_a[i]["h"], err, color="black")
    plt.semilogy()
    #plt.semilogx()
    plt.gca().invert_xaxis()
    plt.xlabel("Step size $h$")
    plt.ylabel("Absolute error in approximation")
    plt.title("Effect of step size on approximation error")
    plt.savefig("ignition_err.png")
    plt.gca().clear()
    res_b = b()
    for result in res_b:
        plt.plot(result["t"], result["y"], label=result["y0"])
        print("Time for combustion front at y0 = " + str(result["y0"]) + ":")
        print(result["t"][np.argwhere(np.diff(np.sign(result["y"] - 9)))])
    plt.title("Simulation result (part B)")
    plt.xlabel("Time $t$ [s]")
    plt.ylabel("Combustion front radius $y(t)$")
    plt.legend()
    plt.savefig('ignition_b.png')

