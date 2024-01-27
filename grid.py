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

def specified_simulations(tabu_length=0, neighbour_ammount=0, input1=0, input2=0, number_of_simulations=0):

    print(f"sim tabu: {tabu_length}     neighbours: {neighbour_ammount}")

    # average malus list for all combinations
    maluslist = list()

    # iterating over all simulations
    for i in range(number_of_simulations):        

        simulation_parameter = True
        malus_room_capacity = list()
        malus_fifth_slot = list()
        malus_double_acts = list()
        malus_single_gaps = list()
        malus_double_gaps = list()
        malus_triple_gaps = list()


        while simulation_parameter:
            data = copy.deepcopy(base)

            # runs chosen algorithm
            if sys.argv[1] == 'tabu':
                test = tabu_algo.Tabu_search(data, iterations=5000, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount )
            elif sys.argv[1] == 'anneal':
                test = annealing.Tabu_search(data, input1=input1, input2=input2)

            # print schedule in terminal
            # for room in test.Rooms:
            #    print_schedule.visualize_room_schedule(test.Rooms[room])    
            
            # print the malus points of a course's activities

            room_capacity_points = 0
            fifth_slot_points = 0
            double_acts = 0
            singlegaps = 0
            doublegaps = 0
            triplegaps = 0

            for course in data.Courses:
                for activity in data.Courses[course].activities:
                    room_capacity, fifth_slot = activity.get_detailed_malus()
                    room_capacity_points += room_capacity
                    fifth_slot_points += fifth_slot

            for item in test.Students:
                double_act_points, single_points, double_points, triple_points = test.Students[item].get_detailed_malus()
                double_acts += double_act_points
                singlegaps += single_points
                doublegaps += double_points
                if triple_points > 100:
                    simulation_parameter = True
                    break
                else:
                    triplegaps += triple_points
                    simulation_parameter = False
            
            if not simulation_parameter:
                malus = room_capacity_points + fifth_slot_points + double_acts + singlegaps + doublegaps + triplegaps
                
                # saving malus scores total & categories in lists
                malus_room_capacity.append(room_capacity_points)
                malus_fifth_slot.append(fifth_slot_points)
                malus_double_acts.append(double_acts)
                malus_single_gaps.append(singlegaps)
                malus_double_gaps.append(doublegaps)
                malus_triple_gaps.append(triplegaps)
                maluslist.append(malus)
        if sys.argv[1]=='anneal':
            print(f"{i}: {malus} for simulation {i} and X value {input1} and Y value {input2}")
        if sys.argv[1]=='tabu':
            print(f"{i}: {malus} for simulation {i} and X value {tabu_length} and Y value {neighbour_ammount}")
               
    if sys.argv[1]=='anneal':
        print(f'negative average for {input1} and {input2}: {sum(maluslist)/len(maluslist)*-1}')
    if sys.argv[1]=='tabu':
        print(f'negative average for {tabu_length} and {neighbour_ammount}: {sum(maluslist)/len(maluslist)*-1}')
    return sum(maluslist)/len(maluslist)*-1

if __name__ == "__main__":
    
    malus_average = list()
    X = []
    Y = []
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    number_of_simulations = 10

    # anneal veriables
    input1=np.arange(1, 3, 1)
    input2 = np.arange(1, 3, 1)

    # tabu variables
    tabu_length = []
    for i in range(100, 130, 10):
        tabu_length.append(int(i))
    neighbour_ammount = []
    for i in range(20, 30, 5):
        neighbour_ammount.append(int(i))

    if sys.argv[1]=='tabu':
        for i in tabu_length:
            for j in neighbour_ammount:
                X.append(i)
                Y.append(j)
                malus_average.append(specified_simulations(tabu_length=i, neighbour_ammount=j, number_of_simulations=number_of_simulations))
    if sys.argv[1]=='anneal':
        for i in input1:
            for j in input2:
                X.append(i)
                Y.append(j)
                malus_average.append(specified_simulations(input1=i, input2=j, number_of_simulations=number_of_simulations))
    
    
    
    if sys.argv[1]=='tabu': 
        fields = ['tabu length', 'neighbours', 'malus_avg']
    else:
        fields = ['input1', 'input2', 'malus_avg']
    rows = []
    for i in range(len(X)):
        row = [X[i], Y[i], malus_average[i]]
        rows.append(row)
    with open(f'data/grid/{sys.argv[1]}_algo_3d_data.csv', mode='w', newline="") as csvfile:
        write = csv.writer(csvfile)
        write.writerow(fields)
        write.writerows(rows)


















def calculate_malus(data):
    total = 0
    for course in data.Courses:
        for activity in data.Courses[course].activities:
            total += activity.get_malus()
    for student in data.Students:
        total += data.Students[student].get_malus()
    return total