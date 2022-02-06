import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from numpy import random

# define initial population and coolperation
def Init_pop_one():
    POP_ONE = []
    # define chromosome -- random.shuffle(ChromosomeX)[K]
    for i in range(POP_SIZE):
        POP_ONE.append(random.sample(ChromosomeX, K))
    return POP_ONE

def Init_pop_two():
    POP_TWO = []
    # define chromosome -- random.shuffle(ChromosomeX)[K]
    for i in range(POP_SIZE):
        POP_TWO.append(random.sample(ChromosomeX, K))
    return POP_TWO

# define fitness function
def get_fitness(x):
    sqrt = np.sqrt(K)
    Eta = []
    Upsilon = []
    Sigma = []
    Mu = []
    maximum = max(x)
    standard = x.std()
    average = x.mean()
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
def pop_one_crossover(pop_one_next):
    new_pop_one = []
    for father in pop_one_next:
        mother = pop_one_next[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        new_pop_one.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        new_pop_one.append(same_pop.append(rest_pop[len(rest_pop) / 2:]))
        pop_one_next.remove(father)
        pop_one_next.remove(mother)
        return new_pop_one

def pop_two_crossover(pop_two_next):
    new_pop_two = []
    for father in pop_two_next:
        mother = pop_two_next[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        new_pop_two.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        new_pop_two.append(same_pop.append(rest_pop[len(rest_pop) / 2:]))
        pop_two_next.remove(father)
        pop_two_next.remove(mother)
        return new_pop_two

# define cooperation crossover operator
def cooperation_crossover_one(cp_next, pop_two_new, pop_one_new):
    for father in cp_next:
        mother = cp_next[np.random.randint(POP_SIZE)]
        same_pop = [x for x in father if x in mother]
        rest_pop = [y for y in (father + mother) if y not in same_pop]
        pop_one_new.append(same_pop.append(rest_pop[0: len(rest_pop) / 2]))
        pop_two_new.append(same_pop.append(rest_pop[len(rest_pop) / 2:]))
        cp_next.remove(father)
        cp_next.remove(mother)
    return pop_one_new, pop_two_new

# define a roulette selector
def pop_one_selection_elitism(POP_ONE):
    pop_parents_one = sorted(POP_ONE, key=lambda x: get_fitness(x), revers=True)

    return pop_parents_one[0: int(POP_SIZE * 0.5)]

def pop_two_selection_elitism(POP_TWO):
    pop_parents_two = sorted(POP_TWO, key=lambda x: get_fitness(x), revers=True)
    return pop_parents_two[0: int(POP_SIZE * 0.5)]

def cooperation_selection(cp_init):
    cp_parents = sorted(cp_init, key=lambda x: get_fitness(x), revers=True)
    return cp_parents[0: int(POP_SIZE * 0.5)]

def pop_one_mutation(pop_new_one):
    fit = []
    compare = []
    for i in pop_new_one:
        if random.random() < Pm:
            H = [x for x in random.randint(0, MAXG_G) if x not in pop_new_one[i]]
            H = H[: 4]
            H_set = random.sample(pop_new_one[i], np.sqrt(len(H)))
            new_one = pop_new_one[i.remove(random.sample(pop_new_one[i], 1))]
            for r in H_set:
                compare.append(new_one.append(r))
                for k in compare:
                    fit.append(get_fitness(k))
                return new_one
            if fit[0] > fit[1]:
                pop_new_one[i] = compare[0]
            else:
                pop_new_one[i] = pop_new_one[i]
    return pop_new_one

def pop_two_mutation(pop_new_one):
    fit = []
    compare = []
    for i in pop_new_one:
        if random.random() < Pm:
            H = [x for x in random.randint(0, MAXG_G) if x not in pop_new_one[i]]
            H = H[: 4]
            H_set = random.sample(pop_new_one[i], np.sqrt(len(H)))
            new_one = pop_new_one[i.remove(random.sample(pop_new_one[i], 1))]
            for r in H_set:
                compare.append(new_one.append(r))
                for k in compare:
                    fit.append(get_fitness(k))
                return new_one
            if fit[0] > fit[1]:
                pop_new_one[i] = compare[0]
            else:
                pop_new_one[i] = pop_new_one[i]
    return pop_new_one

def CGA_MWS():
    pop_one_init = Init_pop_one()
    pop_two_init = Init_pop_two()
    cp_init = pop_one_init | pop_two_init
    gen = 0
    t = 0
    for g in MAXG_G:
        while gen < g and t < MAXT:
            # step 4 :selection and crossover in pop
            pop_one_next = pop_one_selection_elitism(pop_one_init)
            pop_two_next = pop_two_selection_elitism(pop_two_init)
            pop_one_new = pop_one_crossover(pop_one_next)
            pop_two_new = pop_two_crossover(pop_two_next)
            # step 5 :selection and crossover in cooperation
            cp_next = cooperation_selection(cp_init)
            cooperation_crossover_one(cp_next)
            # step 6 :mutation
            pop_one_mutation(pop_one_new)
            pop_two_mutation(pop_two_new)
            # step 7 :sort the pop
            pop_one_new = sorted(pop_one_new, key=lambda x: get_fitness(x), reverse=True)[: POP_SIZE]
            pop_two_new = sorted(pop_two_new, key=lambda x: get_fitness(x), reverse=True)[: POP_SIZE]
            # step 8 :sort the union set
            cp_next = sorted(cp_next | pop_one_new | pop_two_new, key=lambda x: get_fitness(x), reverse=True)[
                      : 2 * POP_SIZE]

            union_pop = pop_one_new | pop_two_new
            union_pop = sorted(union_pop, key=lambda x: get_fitness(x), reverse=True)
            if get_fitness(pop_one_new[0]) > get_fitness(pop_two_new[-1]):
                pop_two_new[-1] = pop_one_new[0]
            elif get_fitness(pop_two_new[0]) > get_fitness(pop_one_new[-1]):
                pop_one_new[-1] = pop_two_new[0]
            elif get_fitness(union_pop[0]) > get_fitness(best):
                best = union_pop[0]
                t = -1
        t += 1
        gen += 1

if __name__ == "__main__":
    K = int(input())
    # set the parameters
    MAXG_G = [1000, 5000, 10000]
    MAXT = 10
    POP_SIZE = MAXG_G / 4
    Pm = 0.3
    ChromosomeX = [c for c in range(MAXG_G)]
    CGA_MWS()
