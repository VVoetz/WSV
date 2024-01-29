from code.algorithms import tabu_algo
from code.classes import data_loader
import numpy as np
import copy

def run_grid_search():

    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    neighbour_tests = [10,20,30,40,50]
    tabu_length_tests = [50,100,200,300,500,1000,2000,10000]

    
    for tabu_change in range(0,2):
        for neighbour_ammount in range(0,5):

            malus_list = []

            for simulation_ammount in range(10):
                data = copy.deepcopy(base)
                simulation = tabu_algo.Tabu_search(data, iterations=10000, tabu_length=tabu_length_tests[tabu_change], neighbour_ammount=neighbour_tests[neighbour_ammount])

                malus = 0

                for activity in simulation.Activities:
                    malus += activity.get_malus()
                
                for student in simulation.Students.values():
                    malus += student.get_malus()
                
                malus_list.append(malus)
            
            print(f"neighbour: {neighbour_tests[neighbour_ammount]}     tabu: {tabu_length_tests[tabu_change]}      average score:{np.average(malus_list)}")
    

