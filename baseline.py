from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo
from code.visualisation import print_schedule, make_google_calendar, malus_hist
import copy
import sys
import csv

if __name__ == "__main__":
    
    maluslist = list()
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    for i in range(10000):
        # paramater to make sure simulations only give valid schedules
        sim = True
        while sim:

            data = copy.deepcopy(base)
            test = random_algo.RandomAlgo(data)
            
            # calculating malus points for activities
            malus = 0
            for course in data.Courses:
                for activity in data.Courses[course].activities:
                    malus += activity.get_malus()
            
            # calculating malus points for the students
            for item in test.Students:
                malus_add = test.Students[item].get_malus()
                if malus_add >= 1000000:
                    sim = True
                    break
                # breaks out for loop when a student gets too much maluspoints
                else:
                    sim = False
                    malus += malus_add

            # script only resumed when all students have a valid schedule       
            if not sim:
                maluslist.append([malus])
                print(f"simulation {i} completed")
    #malus_hist.plot_hist(maluslist)
    fields = ['maluspunten']

    with open('data/baseline_data.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(maluslist)
    
    malus_hist.plot_hist('data/baseline_data')
