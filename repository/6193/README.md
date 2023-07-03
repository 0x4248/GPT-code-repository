# Differential Equations Simulator - 6193

**Language**: `JavaScript`

**Lines of code**: `55`

## Description

This program is a simulator for systems of first-order ordinary differential equations (ODEs). The user can input the ODEs and initial conditions, and the program will use the fourth-order Runge-Kutta method to solve the equations numerically and display the solutions on a graph.

In this example, the program defines a system of first-order ODEs as a function of time and state. The fourth-order Runge-Kutta method is used to solve the ODEs numerically for a specified time range and time step. The solutions are then plotted on a graph using the Chart.js library. The user can input their own system of ODEs and initial conditions to simulate. This program demonstrates the use of complex mathematical techniques to simulate and visualize systems of ODEs.

## Code

``` JavaScript
function simulateODEs(equations, initialValues, tMin, tMax, tStep) {
  // Define the system of ODEs as a function of time and state
  const system = (t, y) => equations.map(equation => equation(t, y));

  // Initialize the state vector
  let y = initialValues;

  // Initialize the time vector
  const times = [];
  for (let t = tMin; t <= tMax; t += tStep) {
    times.push(t);
  }

  // Use the fourth-order Runge-Kutta method to solve the ODEs numerically
  const solutions = [y];
  for (let i = 0; i < times.length - 1; i++) {
    const t = times[i];
    const h = tStep;

    const k1 = system(t, y);
    const k2 = system(t + h/2, y.map((yi, j) => yi + h/2 * k1[j]));
    const k3 = system(t + h/2, y.map((yi, j) => yi + h/2 * k2[j]));
    const k4 = system(t + h, y.map((yi, j) => yi + h * k3[j]));

    y = y.map((yi, j) => yi + h/6 * (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]));
    solutions.push(y);
  }

  // Plot the solutions on a graph using the Chart.js library
  const chartData = {
    labels: times,
    datasets: equations.map((equation, i) => ({
      label: `y${i+1}(t)`,
      data: solutions.map(y => y[i]),
      borderColor: `rgb(${i*100}, ${255-i*100}, 0)`,
      fill: false,
    })),
  };
  const chartConfig = {
    type: 'line',
    data: chartData,
  };
  new Chart(document.getElementById('chart'), chartConfig);
}

// Example usage: simulate the system of ODEs dy1/dt = y2, dy2/dt = -y1, with initial values y1(0) = 1, y2(0) = 0
const equations = [
  (t, [y1, y2]) => y2,
  (t, [y1, y2]) => -y1,
];
const initialValues = [1, 0];
const tMin = 0;
const tMax = 10;
const tStep = 0.1;
simulateODEs(equations, initialValues, tMin, tMax, tStep);

```

## Prompt

```
Make me a program in JavaScript that is more than 20 lines of code long and is complex and interesting. The program must include very complex mathematics. 

When you create the program make a title for it and a short description of what it does.
```