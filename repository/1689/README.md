# Genetic Algorithm for Traveling Salesman Problem - 1689

**Language**: `Python`

**Lines of code**: `110`

## Description

This program implements a genetic algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits a set of cities exactly once and returns to the starting city. The genetic algorithm evolves a population of candidate solutions using principles inspired by natural selection, such as crossover and mutation, to iteratively improve the solutions.

## Code

``` Python
# Genetic Algorithm for Traveling Salesman Problem

import random
import math

# Constants
POPULATION_SIZE = 100
ELITE_SIZE = 10
MUTATION_RATE = 0.01
NUM_GENERATIONS = 1000

# City class
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        return math.sqrt(x_distance**2 + y_distance**2)

# Helper functions
def generate_random_route(city_list):
    return random.sample(city_list, len(city_list))

def calculate_fitness(route):
    total_distance = 0
    for i in range(len(route)):
        from_city = route[i]
        to_city = route[(i + 1) % len(route)]
        total_distance += from_city.distance_to(to_city)
    return 1 / total_distance

def crossover(parent1, parent2):
    start_index = random.randint(0, len(parent1))
    end_index = random.randint(start_index + 1, len(parent1))
    child = parent1[start_index:end_index]

    for city in parent2:
        if city not in child:
            child.append(city)

    return child

def mutate(route):
    for i in range(len(route)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(route))
            route[i], route[j] = route[j], route[i]
    return route

# Genetic Algorithm
def genetic_algorithm(city_list):
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(generate_random_route(city_list))

    for generation in range(NUM_GENERATIONS):
        population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)
        elite = population[:ELITE_SIZE]

        for _ in range(POPULATION_SIZE - ELITE_SIZE):
            parent1 = random.choice(elite)
            parent2 = random.choice(elite)
            child = crossover(parent1, parent2)
            child = mutate(child)
            population.append(child)

        population = population[:POPULATION_SIZE]

    best_route = population[0]
    return best_route

# Example usage
def main():
    # Create a list of cities
    cities = [
        City(60, 200),
        City(180, 200),
        City(80, 180),
        City(140, 180),
        City(20, 160),
        City(100, 160),
        City(200, 160),
        City(140, 140),
        City(40, 120),
        City(100, 120),
        City(180, 100),
        City(60, 80),
        City(120, 80),
        City(180, 60),
        City(20, 40),
        City(100, 40),
        City(200, 40),
        City(20, 20),
        City(60, 20),
        City(160, 20)
    ]

    # Solve TSP using genetic algorithm
    best_route = genetic_algorithm(cities)

    # Print the best route
    print("Best Route:")
    for city in best_route:
        print(city.x, city.y)

if __name__ == "__main__":
    main()

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```