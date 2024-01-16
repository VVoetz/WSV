from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo
from code.visualisation import print_schedule, make_google_calendar
import copy
import sys



if __name__ == "__main__":
    
    maluslist = list()
    for i in range(10000):
        # paramater to make sure simulations only give valid schedules
        sim = True
        while sim:
        
            data = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

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
                if not malus_add >= 1000000:
                    malus += malus_add
                    sim = False
                # breaks out for loop when a student gets too much maluspoints
                else:
                    break

            # script only resumed when all students have a valid schedule       
            if not sim:
                maluslist.append(malus)
                print(f"simulation {i} completed")

    print(maluslist)
        
