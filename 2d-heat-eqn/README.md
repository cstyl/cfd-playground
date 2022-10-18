# Solving 2D Heat Equation using Finite Differences using Python

## Heat Equation 

The PDE of Heat equation is:

$\frac{\partial u}{\partial t} = \alpha \Delta u$

In 2D (Cartesian) this becomes:

$\frac{\partial u}{\partial t} - \alpha (\frac{\partial^{2} u}{\partial^{2} x} + \frac{\partial^{2} u}{\partial^{2} y}) = 0$

where $u$ is the quantity we want to know, $t$ is for temporal variable, $x$ and $y$ are for spatial variables and $\alpha$ is diffusivity constant. Our goal is to find the solution $u$ everywhere in $x$ and $y$ over time $t$.

## Discretized Equation

Finite Difference (FDM) is a numerical method for solving PDE by approximating the derivative with finite differences.

$f'(a) = \lim \limits_{h \to 0} \frac{f(a+h) - f(a)}{h} \approx \frac{f(a+h) - f(a)}{h}$

In finite-difference method, we are going to “discretize” the spatial domain and the time interval $x$, $y$, and $t$. We can write it like this:

$x_i = i \Delta x$

$y_j = j \Delta y$

$t_k = k \Delta t$

with $i$, $j$, $k$ being the steps for each difference for $x$, $y$, and $t$ respectively. The solution $u$ hence becomes: $u(x,y,t) = u_{i,j}^{k}$

The discretized heat equation with FDM becomes:

$\frac{u_{i,j}^{k+1} - u_{i,j}^{k}}{\Delta t} - \alpha (\frac{u_{i+1,j}^{k} - 2 u_{i,j}^{k} + u_{i-1,j}^{k}}{\Delta x^{2}} + \frac{u_{i,j+1}^{k} - 2 u_{i,j}^{k} + u_{i,j-1}^{k}}{\Delta y^{2}}) = 0$

With $\Delta x = \Delta y$, rearranging the above results in:

$u_{i,j}^{k+1} = \gamma (u_{i+1,j}^{k} + u_{i-1,j}^{k} + u_{i,j+1}^{k} + u_{i,j-2}^{k} - 4u_{i,j}^{k}) + u_{i,j}^{k}$

where
$\gamma = \alpha \frac{\Delta t}{\Delta x^{2}}$

## Exercise Problem

Suppose a thin square plate with the side of 50 unit length. The temperature everywhere inside the plate is originally 0 degree (at $t=0$). The top boundary has a temperature of 50 degrees and the rest are set to 0 degree. Assume for our model that $\Delta x = 1$ and $\alpha = 2.0$. Solve the problem numerically to see the temperature everywhere in the 2D space and over time.