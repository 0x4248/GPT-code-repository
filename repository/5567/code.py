import random

class Individual:
    def __init__(self, cities, genes=None):
        self.cities = cities
        if genes is None:
            self.genes = random.sample(cities, len(cities))
        else:
            self.genes = genes
        self.fitness = None

    def evaluate_fitness(self):
        total_distance = 0
        for i in range(len(self.genes)):
            from_city = self.genes[i]
            to_city = self.genes[(i+1)%len(self.genes)]
            total_distance += self.cities[from_city][to_city]
        self.fitness = 1/total_distance if total_distance > 0 else float('inf')

    def mutate(self, mutation_rate):
        if random.random() < mutation_rate:
            i = random.randint(0, len(self.genes)-1)
            j = random.randint(0, len(self.genes)-1)
            self.genes[i], self.genes[j] = self.genes[j], self.genes[i]

class Population:
    def __init__(self, cities, size, crossover_rate, mutation_rate):
        self.cities = cities
        self.size = size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.individuals = [Individual(cities) for _ in range(size)]

    def evolve(self):
        self.evaluate_fitness()
        new_individuals = [self.select() for _ in range(self.size)]
        self.individuals = new_individuals

    def evaluate_fitness(self):
        for individual in self.individuals:
            individual.evaluate_fitness()
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)

    def select(self):
        parents = random.sample(self.individuals[:int(self.size/2)], 2)
        child = self.crossover(parents[0], parents[1])
        child.mutate(self.mutation_rate)
        return child

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            i = random.randint(0, len(self.cities)-1)
            j = random.randint(0, len(self.cities)-1)
            if i > j:
                i, j = j, i
            genes1 = parent1.genes[i:j]
            genes2 = [gene for gene in parent2.genes if gene not in genes1]
            genes = genes2[:i] + genes1 + genes2[i:]
            return Individual(self.cities, genes)
        else:
            return random.choice([parent1, parent2])

def read_cities(filename):
    cities = []
    with open(filename) as f:
        for line in f:
            parts = line.split()
            x, y = float(parts[1]), float(parts[2])
            cities.append((x, y))
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
