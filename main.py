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

    for i in range(1):
        
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
            triplegaps += triple_points
        
        malus = room_capacity_points + fifth_slot_points + double_acts + singlegaps + doublegaps + triplegaps
        
        print(f"{i}: {malus}")

        maluslist.append(malus)
        
        #make_google_calendar.make_google_calendar_csv(data)
        make_google_calendar.make_student_calendar(data)

    print(f"room capacity: {room_capacity_points}   fifth: {fifth_slot_points}  courseconflict: {double_acts}   single: {singlegaps}    double: {doublegaps}")
    print(sorted(maluslist))
    total = 0
    for item in maluslist:
        while item > 1000000:
            item -= 1000000
        total += item
    print(f"average: {total / len(maluslist)}")
        

    end = time.time()
    print(f"time taken: {end - start}")
