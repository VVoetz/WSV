from code.classes import data_loader

from code.algorithms import testalgo, random_algo, greedy_algo, tabu_algo, annealing

from code.visualisation import print_schedule, make_google_calendar

from code.experiments import grid_search_tabu, anneal_grid_search

import copy
import sys
import time
import csv



if __name__ == "__main__":
    
    start = time.time()

    number_of_simulations = 1

    malus_room_capacity = list()
    malus_fifth_slot = list()
    malus_double_acts = list()
    malus_single_gaps = list()
    malus_double_gaps = list()
    malus_triple_gaps = list()
    maluslist = list()


    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    for i in range(number_of_simulations):
        
        data = copy.deepcopy(base)

        # runs chosen algorithm
        if sys.argv[1] == 'greedy':
            test = greedy_algo.Greedyalgo(data)
        elif sys.argv[1] == 'test':
            test = testalgo.Testalgo(data)
        elif sys.argv[1] == 'random':
            test = random_algo.Testalgo(data)
        elif sys.argv[1] == 'tabu':
            test = greedy_algo.Greedyalgo(data)
            test = tabu_algo.Tabu_search(data, iterations=100000, neighbour_ammount=25, tabu_length=200, create_solution=False)
        elif sys.argv[1] == 'tabu_grid':
            grid_search_tabu.run_grid_search()
            test = tabu_algo.Tabu_search(data, iterations=0)
        elif sys.argv[1] == 'anneal':
            test = greedy_algo.Greedyalgo(data)
            test = annealing.Tabu_search(data)
        elif sys.argv[1] == 'anneal_grid':
            anneal_grid_search.run_grid_search(int(sys.argv[2]), int(sys.argv[3]))
            exit()
        elif sys.argv[1] == "hillclimber":
            test = hillclimber.Hillclimber(data, iterations=100000, no_change_stop=1000)

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
        
        # saving malus scores total & categories in lists
        malus_room_capacity.append(room_capacity_points)
        malus_fifth_slot.append(fifth_slot_points)
        malus_double_acts.append(double_acts)
        malus_single_gaps.append(singlegaps)
        malus_double_gaps.append(doublegaps)
        malus_triple_gaps.append(triplegaps)
        maluslist.append(malus)

        # print(f"{i}: {malus}")

        
        #make_google_calendar.make_google_calendar_csv(data)
        # make_google_calendar.make_student_calendar(data)

    # writing csv file with malus lists
    fields = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps', 'Total']
    rows = []
    for i in range(number_of_simulations):
        row = [malus_room_capacity[i], malus_fifth_slot[i], malus_double_acts[i], malus_single_gaps[i], malus_double_gaps[i], malus_triple_gaps[i], maluslist[i]]
        rows.append(row)
    with open(f'data/{sys.argv[1]}_algo_simulation_data.csv', mode='w') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(fields)
        write.writerows(rows)


    print(f"room capacity: {room_capacity_points}   fifth: {fifth_slot_points}  courseconflict: {double_acts}   single: {singlegaps}    double: {doublegaps}")
    # print(sorted(maluslist))
    total = 0
    for item in maluslist:
        while item > 1000000:
            item -= 1000000
        total += item
    # print(f"average: {total / len(maluslist)}")
        

    end = time.time()
    print(f"time taken: {end - start}")


