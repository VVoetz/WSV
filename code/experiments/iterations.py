from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from code.visualisation import plots
from code.classes import data_loader
from code.algorithms import tabu_algo, annealing, hillclimber
import copy
import csv

def write_iterations_to_csv(algorithm_name: str, number_of_simulations: int) -> None:
    """
    Function runs a few simulations of the give algorithm name
    and writes them to a formatted csv file
    """

    number_of_simulations = number_of_simulations
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    # run simulations
    for i in range(number_of_simulations):        

        data = copy.deepcopy(base)

        # runs chosen algorithm
        if algorithm_name == 'tabu':
            test = tabu_algo.Tabu_search(data)

        elif algorithm_name == 'anneal':
            test = annealing.Annealing(data)

        elif algorithm_name == 'hillclimber':
            test = hillclimber.Hillclimber(data)

        else:
            print("invalid algorithm")
            exit()

        maluslist = test.malus_per_iteration
        time_list = test.time_per_iteration

        # write results to a csv file
        fields = ['malusscore', 'time']
        rows = []
        for j in range(0, len(maluslist) - 1):
            rows.append([maluslist[j], time_list[j]])
        with open(f'data/iterations/{algorithm_name}/iteration_scores_{algorithm_name}_simulation_{i+1}.csv', mode='w', newline="") as file:
            write = csv.writer(file)
            write.writerow(fields)
            write.writerows(rows)

        print(f'simulation {i} done and data written to csv')

