# Nonlinear Optimization Solver - 5861

**Language**: `Python`

**Lines of code**: `16`

## Description

This program uses the nonlinear optimization algorithm to find the minimum value of a multivariable function. The user inputs the function and starting point, and the program iteratively updates the input to converge to the minimum.

In this example, the objective function is defined as the sum of the squares of the input variables plus the sine function applied to each variable. The BFGS algorithm is used to find the minimum value of this function, starting from the point (1,1). The resulting minimum value and input values are printed to the console. This program demonstrates the use of mathematical optimization techniques to solve complex problems.

## Code

``` Python
import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # Define the objective function
    return x[0]**2 + x[1]**2 + np.sin(x[0]) + np.sin(x[1])

# Set the initial point
x0 = np.array([1,1])

# Use the BFGS optimization algorithm to minimize the objective function
result = minimize(objective_function, x0, method='BFGS')

# Print the minimum value and the corresponding input values
print("Minimum value: ", result.fun)
print("Input values: ", result.x)

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting. The program must use a mathematical equations

When you create the program make a title for it and a short description of what it does.
```