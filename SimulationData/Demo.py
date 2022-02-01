import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from numpy import random

# set the parameters
MAXG_G = [1000, 5000, 10000]
MAXT =10
POP_SIZE = MAXG_G/4
Mutation_Rate = 0.3
ChromosomeX = np.arange(MAXG_G)
POP_ONE = []
POP_TWO = []
COOLPERATION = []


# define fitness function
def Fit(x):
    return W(M[i])

def pop_and_coolperation(pop): # define the initial value
    # POP_ONE = pop[0:POP_SIZE/2, 0:K]
    # POP_TWO = pop[POP_SIZE/2:POP_SIZE, K:]
    POP_ONE[0] = pop[random.randint(POP_SIZE)]
    POP_TWO[0] = pop[random.randint(POP_SIZE)]
    COOLPERATION[0] = (POP_ONE[0] | POP_TWO[0])

def selection(POP_ONE, POP_TWO):
    new_pop = []
    for father in POP_ONE:
        child = father
        mother = POP_TWO[np.random.randint(POP_SIZE)]
        for i in father:
            for j in mother:
                if i == j:
                    selector = father.remove(i) | mother.remove(j)

        child[cross_points:] = mother[cross_points:]  # 孩子得到位于交叉点后的母亲的基因
        mutation(child)  # 每个后代有一定的机率发生变异
        new_pop.append(child)

    return new_pop
def get_fitness(pop):

    w
if __name__ == "__main__":
    K = int(input())
    # Generate Initial_chromosome
    Init_chromosome = random.shuffle(ChromosomeX)[K]
    pop = [[Init_chromosome] for i in POP_SIZE]
    pop_and_coolperation(pop)
    # pop = random.randint(0, MAXG_G, size = (POP_SIZE, K))
    for g in MAXG_G:
        # set the object as a iterator
        G = list(range(g))
        for time in G:
            gen = 0
            t = 0
            if gen < MAXG_G[g] and t < MAXT:
                # begin to iterate
                # step four : selection operation tp pop
                SAME = [x for x in POP_ONE[gen] if x in POP_TWO[gen]]
                REST = [y for y in (POP_ONE[gen] + POP_TWO[gen]) if y not in SAME]
                REST = random.stuffle(REST)
                Rest_pre = REST[0: len(REST)/2]
                Rest_back = REST[len(REST)/2:]
                POP_ONE[gen + 1] = SAME.extend(Rest_pre)
                POP_TWO[gen + 1] = SAME.extend(Rest_back)