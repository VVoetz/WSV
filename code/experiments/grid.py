from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from code.visualisation import plots


from code.classes import data_loader

from code.algorithms import testalgo, random_algo, greedy_algo, tabu_algo, annealing

from code.visualisation import print_schedule, make_google_calendar, plots

import copy
import sys
import time
import csv

def specified_simulations(base, algorithm_name: str, tabu_length=0, neighbour_ammount=0, input1=0, input2=0, number_of_simulations=0) -> float:
    """
    Function runs the given algorithm with the given settings for a number of
    simulations ammount of times and returns the negative average of all runs

    pre:    algorithm name is a valid algorithm
            base is a data loader object
    post:   returns the negative average of ran runs as a float
    """

    # average malus list for all combinations
    maluslist = list()

    # iterating over all simulations
    for i in range(number_of_simulations):

        data = copy.deepcopy(base)

        # runs chosen algorithm
        if algorithm_name == 'tabu':
            test = tabu_algo.Tabu_search(data, iterations=100000, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount, stop_time = 20)
        elif algorithm_name == 'anneal':
            test = annealing.Tabu_search(data, input1=input1, input2=input2)

        # calculate malus for courses
        malus = 0
        for course in test.Courses:
            for activity in test.Courses[course].activities:
                malus += activity.get_malus()

        # calculate malus for students
        for student in test.Students.values():
            malus += student.get_malus()
        
        maluslist.append(malus)

        # print malus score
        if algorithm_name=='anneal':
            print(f"{i}: {malus} for simulation {i} and X value {input1} and Y value {input2}")
        if algorithm_name=='tabu':
            print(f"{i}: {malus} for simulation {i} and X value {tabu_length} and Y value {neighbour_ammount}")
               
    if algorithm_name == 'anneal':
        print(f'negative average for {input1} and {input2}: {sum(maluslist)/len(maluslist)*-1}')
    if algorithm_name == 'tabu':
        print(f'negative average for {tabu_length} and {neighbour_ammount}: {sum(maluslist)/len(maluslist)*-1}')

    return sum(maluslist)/len(maluslist)*-1

def run_grid_search(algorithm_name: str, number_of_simulations = 5, tabu_length_list = [], neighbour_ammount_list = [], acceptance_rate_student = [], acceptance_rate_activity = []) -> None:
    """
    Function runs multiple simulations of given algorithm with different given settings

    pre:    given lists only contain integers with constant intervals
    post:   run algorithms and saves average data to csv
    """

    malus_average = list()
    X = []
    Y = []
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    number_of_simulations = number_of_simulations

    # anneal veriables
    input1 = acceptance_rate_student
    input2 = acceptance_rate_activity

    # tabu variables
    tabu_length = tabu_length_list
    neighbour_ammount = neighbour_ammount_list

    if algorithm_name == 'tabu':

        # loop over all variables and run simulation
        for i in tabu_length:
            for j in neighbour_ammount:
                X.append(i)
                Y.append(j)
                malus_average.append(specified_simulations(base, algorithm_name, tabu_length=i, neighbour_ammount=j, number_of_simulations=number_of_simulations))
    if algorithm_name == 'anneal':

        # loop over all variables and run simulation
        for i in input1:
            for j in input2:
                X.append(i)
                Y.append(j)
                malus_average.append(specified_simulations(base, algorithm_name, input1=i, input2=j, number_of_simulations=number_of_simulations))
    
    
    if algorithm_name == 'tabu': 
        fields = ['tabu length', 'neighbours', 'malus_avg']
    else:
        fields = ['input1', 'input2', 'malus_avg']

    rows = []

    # loop over found averages and write them to csv
    for i in range(len(X)):
        row = [X[i], Y[i], malus_average[i]]
        rows.append(row)
    with open(f'data/grid/{algorithm_name}_algo_3d_data.csv', mode='w', newline="") as csvfile:
        write = csv.writer(csvfile)
        write.writerow(fields)
        write.writerows(rows)

if __name__ == "__main__":
    
    # tabu variables
    tabu_lengths = [100, 200]
    neighbours = [10, 15]

    # anneal variables
    student_acceptance = [1, 2]
    activity_acceptance = [1, 2]

    simulations = 2

    run_grid_search(sys.argv[1], number_of_simulations = simulations, tabu_length_list = tabu_lengths,\
        neighbour_ammount_list = neighbours, acceptance_rate_student = student_acceptance, acceptance_rate_activity = activity_acceptance)
