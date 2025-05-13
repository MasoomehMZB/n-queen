import random

# Counts number of queen conflicts
def fitness(positions):
    size = len(positions)
    attacks = 0
    for i in range(size):
        for j in range(i + 1, size):
            if positions[i] == positions[j] or abs(positions[i] - positions[j]) == abs(i - j):
                attacks += 1
    return -attacks

# Picks a random row and randomly changes its column.
def mutate(positions):
    new_pos = positions[:]
    i = random.randint(0, len(new_pos) - 1)
    new_pos[i] = random.randint(0, len(new_pos) - 1)
    return new_pos

# Takes the first part from one parent, rest from another.
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def solve_genetic(size, population_size=100, generations=1000):
    population = [random.sample(range(size), size) for _ in range(population_size)]
    generation_best = []

    for gen in range(generations):
        population.sort(key=fitness, reverse=True)
        best = population[0]
        if fitness(best) == 0:
            return best, generation_best

        next_gen = population[:10]
        generation_best.append(best)
        while len(next_gen) < population_size:
            p1, p2 = random.choices(population[:50], k=2)
            child = crossover(p1, p2)
            if random.random() < 0.1:
                child = mutate(child)
            next_gen.append(child)
        population = next_gen

    return population[0], generation_best
