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
