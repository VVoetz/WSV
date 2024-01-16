from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo
from code.visualisation import print_schedule, make_google_calendar, plot_list
import copy
import sys

if __name__ == "__main__":
    
    maluslist = list()
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    for i in range(100):
        # paramater to make sure simulations only give valid schedules
        sim = True
        while sim:

            data = copy.deepcopy(base)
            # runs chosen algorithm
            if sys.argv[1] == 'greedy':
                test = greedy_algo.Greedyalgo(data)
            elif sys.argv[1] == 'test':
                test = testalgo.Testalgo(data)
            elif sys.argv[1] == 'random':
                test = random_algo.Testalgo(data)
            
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
                maluslist.append(malus)
                print(f"simulation {i} completed")

    print(maluslist)
