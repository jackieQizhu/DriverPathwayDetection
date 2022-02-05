import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from numpy import random


# define initial population and coolperation
def Init_pop_and_cool():
    POP_ONE = []
    POP_TWO = []
    # define chromosome -- random.shuffle(ChromosomeX)[K]
    for i in range(POP_SIZE):
        POP_ONE.append(random.shuffle(ChromosomeX)[K])
        POP_TWO.append(random.shuffle(ChromosomeX)[K])
    COOL = POP_ONE | POP_TWO
    return POP_ONE, POP_TWO, COOL

# define fitness function
def get_fitness(k):
    sqrt = np.sqrt(K)
    Eta = []
    Upsilon = []
    Sigma = []
    Mu = []
    maximum = max(k)
    standard = k.std()
    average = k.mean()
    Eta.append(maximum)
    Sigma.append(standard)
    Mu.append(average)
    for i in range(len(Eta)):
        if Eta[i] < 0.5:
            value = Sigma[i] / (2 * sqrt * Mu[i])
            Upsilon.append(value)
        else:
            value = Sigma[i] / Mu[i]
            Upsilon.append(value)
    Coverage = sum(Eta)
    Mutual_exclusivity = sum(Upsilon)
    Weight = Coverage + Mutual_exclusivity
    return Weight

# calculate the fitness of every individual in population
def pop_fitness_one(POP_ONE):
    return [get_fitness(k) for k in POP_ONE]
def pop_fitness_two(POP_TWO):
    return [get_fitness(k) for k in POP_TWO]


# define population crossover operator
def pop_crossover(POP_ONE, POP_TWO):
    new_pop_one = []
    new_pop_two = []
    for father in POP_ONE:
        mother = POP_ONE[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        new_pop_one.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        new_pop_one.append(same_pop.append(rest_pop[len(rest_pop) / 2: ]))
        POP_ONE.remove(father)
        POP_ONE.remove(mother)
    for father in POP_TWO:
        mother = POP_TWO[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        new_pop_two.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        new_pop_two.append(same_pop.append(rest_pop[len(rest_pop) / 2:]))
        POP_TWO.remove(father)
        POP_TWO.remove(mother)
        return new_pop_one, new_pop_two

# define cooperation crossover operator
def cool_crossover(COOL):
    new_cool_pop_one = []
    new_cool_pop_two = []
    for father in COOL:
        mother = COOL[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        new_cool_pop_one.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        new_cool_pop_two.append(same_pop.append(rest_pop[len(rest_pop) / 2:]))
        COOL.remove(father)
        COOL.remove(mother)
    return new_cool_pop_one, new_cool_pop_two


# define a roulette selector
def pop_selection_elitism(POP_ONE, POP_TWO):
    pop_parents_one = sorted(POP_ONE, key = lambda x: get_fitness(x), revers = True)
    pop_parents_two = sorted(POP_TWO, key = lambda x: get_fitness(x), revers = True)
    return pop_parents_one[0: int(POP_SIZE * 0.5)], pop_parents_two[0: int(POP_SIZE * 0.5)]

# a problem in here,I can't understand this step completely
def cooperation_selection(POP_ONE, POP_TWO):
    cool_parents_one = sorted(POP_ONE, key=lambda x: get_fitness(x), revers=True)
    cool_parents_two = sorted(POP_TWO, key=lambda x: get_fitness(x), revers=True)
    return cool_parents_one[0: int(POP_SIZE * 0.5)], cool_parents_two[0: int(POP_SIZE * 0.5)]
def mutation(POP_ONE, POP_TWO):
    fit = []
    compare =[]
    for i in POP_ONE:
        if random.random() < Pm:
            H = [x for x in random.randint(0, MAXG_G) if x not in POP_ONE[i]]
            H = H[: 4]
            H_set = random.sample(POP_ONE[i], np.sqrt(len(H)))
            new_one = POP_ONE[i.remove(random.sample(POP_ONE[i], 1))]
            for r in H_set:
                compare.append(new_one.append(r))
                for k in compare:
                    fit.append(get_fitness(k))
                return new_one
            if fit[0] > fit[1]:
                POP_ONE[i] = compare[0]
            else:
                POP_ONE[i] = POP_ONE[i]


if __name__ == "__main__":
    K = int(input())
    # set the parameters
    MAXG_G = [1000, 5000, 10000]
    MAXT = 10
    POP_SIZE = MAXG_G / 4
    Pm = 0.3
    ChromosomeX = np.arange(MAXT)

    # init pop1 pop2 and coolperation
    Init_pop_and_cool()

    for g in MAXG_G:
        # set the generations
        for gen,t in range(g):
            if gen < MAXG_G[g] and t < MAXT:
                pop_crossover()

