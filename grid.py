from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo
from code.visualisation import print_schedule, make_google_calendar, malus_hist
import copy
import sys
import csv

if __name__ == "__main__":
    
    malus_average = list()
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    input1=np.arange(1, 11, 1)
    input2 = np.arange(1, 11, 1)
    tabu_length = []
    for i in range(250, 255):
        tabu_length.append(i)
    neighbour_ammount = []
    for i in range

    def specified_simulations(tabu_length=0, neighbour_ammount=0, input1=0, input2=0, number_of_simulations):
        # iterating over all simulations
        for i in range(number_of_simulations):

            simulation_parameter = True
            malus_room_capacity = list()
            malus_fifth_slot = list()
            malus_double_acts = list()
            malus_single_gaps = list()
            malus_double_gaps = list()
            malus_triple_gaps = list()
            maluslist = list()

            while simulation_parameter:
                data = copy.deepcopy(base)

                # runs chosen algorithm
                if sys.argv[1] == 'tabu':
                    test = tabu_algo.Tabu_search(data, iterations=10, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount )
                    grid_search_tabu.run_grid_search()
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

                    print(f"{i}: {malus}")
        return sum(maluslist)/len(maluslist)*-1













def calculate_malus(data):
    total = 0
    for course in data.Courses:
        for activity in data.Courses[course].activities:
            total += activity.get_malus()
    for student in data.Students:
        total += data.Students[student].get_malus()
    return total