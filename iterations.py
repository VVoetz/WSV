from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from code.visualisation import plots
from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo, tabu_algo, annealing
from code.visualisation import print_schedule, make_google_calendar, plots
from code.experiments import grid_search_tabu
import copy
import sys
import time
import csv

# tabu parameters
tabu_length = 200
neighbour_ammount = 5

# anneal parameters
input1 = 0
input2 = 0

number_of_simulations


for i in range(number_of_simulations):        

    data = copy.deepcopy(base)

    # runs chosen algorithm
    if sys.argv[1] == 'tabu':
        test = tabu_algo.Tabu_search(data, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount )
    elif sys.argv[1] == 'anneal':
        test = annealing.Tabu_search(data, input1=input1, input2=input2)
    maluslist = test.malus_per_iteration
    fields = ['malusscore']
    rows = []
    for j in maluslist:
        else:
            rows.append([j])
    with open(f'data/iterations/{sys.argv[1]}/iteration_scores_{sys.argv[1]}_simulation_{i+1}', mode='w', newline="") as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)





