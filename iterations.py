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

number_of_simulations = 2

base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")



for i in range(number_of_simulations):        

    data = copy.deepcopy(base)

    # runs chosen algorithm
    if sys.argv[1] == 'tabu':
        test = tabu_algo.Tabu_search(data)
    elif sys.argv[1] == 'anneal':
        test = annealing.Tabu_search(data)
    maluslist = test.malus_per_iteration
    fields = ['malusscore']
    rows = []
    for j in maluslist:
        rows.append([j])
    with open(f'data/iterations/{sys.argv[1]}/iteration_scores_{sys.argv[1]}_simulation_{i+1}', mode='w', newline="") as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)

    print(f'simulation {i} done and data written to csv')





