from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo, tabu_algo, annealing
from code.visualisation import print_schedule, make_google_calendar
import copy
import sys
import time



if __name__ == "__main__":
    
    start = time.time()

    maluslist = list()
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    for i in range(5):
        
        data = copy.deepcopy(base)

        # runs chosen algorithm
        if sys.argv[1] == 'greedy':
            test = greedy_algo.Greedyalgo(data)
        elif sys.argv[1] == 'test':
            test = testalgo.Testalgo(data)
        elif sys.argv[1] == 'random':
            test = random_algo.Testalgo(data)
        elif sys.argv[1] == 'tabu':
            test = tabu_algo.Tabu_search(data)
        elif sys.argv[1] == 'anneal':
            test = annealing.Tabu_search(data)

        # print schedule in terminal
        # for room in test.Rooms:
        #    print_schedule.visualize_room_schedule(test.Rooms[room])    
        
        # print the malus points of a course's activities

        malus = 0
        for course in data.Courses:
            for activity in data.Courses[course].activities:
                malus += activity.get_malus()
        
        for item in test.Students:
            malus += test.Students[item].get_malus()
        print(f"{i}: {malus}")

        maluslist.append(malus)
        
        #make_google_calendar.make_google_calendar_csv(data)
        make_google_calendar.make_student_calendar(data)
    print(sorted(maluslist))

    end = time.time()
    print(f"time taken: {end - start}")
