---
title: Thinking about Numerical Error
author: Jasper
date: Tue Sep 19
---

# Significant Figures

Measurements are limited in *precision* and *accuracy*. An inaccurate measurement is one that does not correspond well to the "true" value of the number being measured. An imprecise measurement has greater variance. Clearly, precision is easier to describe and guarantee; accuracy is a much shiftier concept.

**True error** is the difference between the true value (call it $phi$) and an approximation:

$$
E_t = \mathrm{true value} - \mathrm{approximation} = \phi - A
$$

The **true fractional relative error** accounts for the magnitudes in the quantities; giving the error as a fraction of the true value.

$$
E_f = \frac{E_t}{\phi}
$$

where the subscript _f_ stands for 'fractional' error.

Such errors can *only* be computed when a true, accurate answer is known. This is often used for the verification of approximate numerical methods, but obviously cannot be used for a field model intended to give an idea of an (otherwise unknown) true answer!

For an iterative algorithm, the approximation error represents the fractional change in approximations between iterations.

$$
e_a = \frac{A_k - A_{k - 1}}{A_k}
$$

Normally, each iteration, the algorithm will come closer to the true answer. You choose a cutoff $e_c$, and say that if the fractional change between iterations is less than that cutoff, the algorithm has converged acceptably.

:::{.aside}

It's worth noting that the cutoff makes your accuracy sensitive to how slowly an algorithm converges on the correct answer. An algorithm that converges more slowly will halt at a value further from the true answer. This is one reason it's good to find quickly convergent algorithms.

:::

The following demonstration shows how more terms in the Maclaurin expansion of $e^1$ must be taken to reach a closer radius of convergence:

![](python/Error_maclaurin_expansion_e.png)
