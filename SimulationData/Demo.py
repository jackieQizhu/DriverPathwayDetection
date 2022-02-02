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
COOPERATION = []


# define fitness function
def Fit(x):
    return W(M[i])

def initial_pop_and_cooperation(pop): # define the initial value
    # POP_ONE = pop[0:POP_SIZE/2, 0:K]
    # POP_TWO = pop[POP_SIZE/2:POP_SIZE, K:]
    POP_ONE[0] = pop[random.randint(POP_SIZE)]
    POP_TWO[0] = pop[random.randint(POP_SIZE)]
    COOPERATION[0] = (POP_ONE[0] | POP_TWO[0])

def get_fitness(pop):

    w

def pop_selection(POP_ONE, POP_TWO):
    SAME = [x for x in POP_ONE[gen] if x in POP_TWO[gen]]
    REST = [y for y in (POP_ONE[gen] + POP_TWO[gen]) if y not in SAME]
    REST = random.stuffle(REST)
    Rest_pre = REST[0: len(REST) / 2]
    Rest_back = REST[len(REST) / 2:]
    POP_ONE[gen + 1] = SAME.extend(Rest_pre)
    POP_TWO[gen + 1] = SAME.extend(Rest_back)
    return POP_ONE[gen + 1], POP_TWO[gen + 1]

def cooperation_selection():
    SAME = [x for x in POP_ONE[gen] if x in POP_TWO[gen]]
    REST = [y for y in (POP_ONE[gen] + POP_TWO[gen]) if y not in SAME]
    REST = random.stuffle(REST)
    Rest_pre = REST[0: len(REST) / 2]
    Rest_back = REST[len(REST) / 2:]
    POP_ONE[gen + 1] = SAME.extend(Rest_pre)
    POP_TWO[gen + 1] = SAME.extend(Rest_back)
    return POP_ONE[gen + 1], POP_TWO[gen + 1]

if __name__ == "__main__":
    K = int(input())
    # Generate Initial_chromosome
    Init_chromosome = random.shuffle(ChromosomeX)[K]
    pop = [[Init_chromosome] for i in POP_SIZE]
    initial_pop_and_cooperation(pop)
    # pop = random.randint(0, MAXG_G, size = (POP_SIZE, K))
    for g in MAXG_G:
        # set the object as a iterator
        G = list(range(g))
        for time in G:
            gen = 0
            t = 0
            if gen < MAXG_G[g] and t < MAXT:
                # begin to iterate
                # step fourth : selection operation in pop
                pop_selection(POP_ONE, POP_TWO)
                # step fifth : selection operation in cooperation
                cooperation_selection()
                # step sixth :
                # step seventh :
                # step eighth :
                # step ninth :
                # step tenth :
                # step eleventh :
                # step twelfth :
                # step thirteenth :
                # step fourteenth :
                # step fifteenth :
                # step sixteenth :
                # step seventeenth :

