from code.algorithms import annealing
from code.classes import data_loader
import copy
import csv

def run_grid_search(iterations, input):
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    averages = [input]
    resultlist = list()
    with open('code/experiments/anneal_results/output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(1, 11):
            average = 0
            results = list()
            for j in range(1, iterations + 1):
                data = copy.deepcopy(base)
                annealing.Tabu_search(data, input, i)
                malus = calculate_malus(data)
                average += (malus / iterations)
                result = [input, i, malus]
                results.append(result)
                writer.writerow(result)
                
            averages.append(str(average))
    
    with open('code/experiments/anneal_results/averages.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(averages)
        # for average in averages:
        #     test = [str(input), str(i), str(average)]
        #     averages.append(test)
        #     writer.writerow(test)
            
        
        
    print(f"{(averages)}")    

def calculate_malus(data):
    total = 0
    for course in data.Courses:
        for activity in data.Courses[course].activities:
            total += activity.get_malus()
    for student in data.Students:
        total += data.Students[student].get_malus()
    return total