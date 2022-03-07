from collections import Counter, defaultdict


DATA = [1,1,3,5,3,1,1,4,1,1,5,2,4,3,1,1,3,1,1,5,5,1,3,2,5,4,1,1,5,1,4,2,1,4,2,1,4,4,1,5,1,4,4,1,1,5,1,5,1,5,1,1,1,5,1,2,5,1,1,3,2,2,2,1,4,1,1,2,4,1,3,1,2,1,3,5,2,3,5,1,1,4,3,3,5,1,5,3,1,2,3,4,1,1,5,4,1,3,4,4,1,2,4,4,1,1,3,5,3,1,2,2,5,1,4,1,3,3,3,3,1,1,2,1,5,3,4,5,1,5,2,5,3,2,1,4,2,1,1,1,4,1,2,1,2,2,4,5,5,5,4,1,4,1,4,2,3,2,3,1,1,2,3,1,1,1,5,2,2,5,3,1,4,1,2,1,1,5,3,1,4,5,1,4,2,1,1,5,1,5,4,1,5,5,2,3,1,3,5,1,1,1,1,3,1,1,4,1,5,2,1,1,3,5,1,1,4,2,1,2,5,2,5,1,1,1,2,3,5,5,1,4,3,2,2,3,2,1,1,4,1,3,5,2,3,1,1,5,1,3,5,1,1,5,5,3,1,3,3,1,2,3,1,5,1,3,2,1,3,1,1,2,3,5,3,5,5,4,3,1,5,1,1,2,3,2,2,1,1,2,1,4,1,2,3,3,3,1,3,5]


def run(initial_population, days):
    population = initial_population
    for _ in range(days):
        new_fishes = []
        for i, fish in enumerate(population):
            population[i] -= 1
            if fish == 0:
                population[i] = 6
                new_fishes.append(8)
        population.extend(new_fishes)
    return population


def run_opt(initial_population, days):
    population = Counter(initial_population)
    population = defaultdict(int, population)
    for _ in range(days):
        zeros = population.get(0, 0)
        population = {k-1: v for k, v in population.items() if k-1 >= 0}
        population[8] = zeros + population.get(8, 0)
        population[6] = zeros + population.get(6, 0)
    return population


def main():
    res = run_opt(DATA, 256)
    print(sum(res.values()))


if __name__ == '__main__':
    main()
