from code.classes import data_loader
from code.experiments import anneal_grid_search
from code.algorithms import greedy_algo, testalgo, random_algo, hillclimber, annealing, tabu_algo
import copy
import csv

def run_simulation(algorithm_name: str, number_of_simulations: int, print_schedule = False, algo_duration ="") -> None:
    """
    Function runs algorithm a given ammount of times, prints relevent data to the terminal
    and saves relevant data in csv files in the data folder

    pre:    algorithm name is a valid algorithm
    """

    # initialize different types of malus points
    malus_room_capacity = list()
    malus_fifth_slot = list()
    malus_double_acts = list()
    malus_single_gaps = list()
    malus_double_gaps = list()
    malus_triple_gaps = list()
    maluslist = list()

    # load in data object
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    # run simulation given ammount of times
    for i in range(number_of_simulations):
        
        data = copy.deepcopy(base)

        # runs chosen algorithm
        if algorithm_name == 'greedy':
            test = greedy_algo.Greedyalgo(data)

        elif algorithm_name == 'test':
            test = testalgo.Testalgo(data)

        elif algorithm_name == 'random':
            test = random_algo.RandomAlgo(data)

        elif algorithm_name == 'tabu':
            test = greedy_algo.Greedyalgo(data)
            test = tabu_algo.Tabu_search(data, iterations=1000, neighbour_ammount=5, tabu_length=5000, create_solution=False, stop_time=15)

        elif algorithm_name == 'anneal':
            
            
            test = greedy_algo.Greedyalgo(data)
            if algo_duration == "":
                test = annealing.Annealing(data)
            else:
                test = annealing.Annealing(data, duration=algo_duration)

        # MAYBE THIS SHOULD BE REMOVED
        elif algorithm_name == 'anneal_grid':
            anneal_grid_search.run_grid_search(int(algorithm_name), int(sys.argv[3]))
            exit()

        elif algorithm_name == "hillclimber":
            test = hillclimber.Hillclimber(data, iterations=100000, no_change_stop=1000)

        else:
            print("Invalid algorithm...")
            exit()

        # print schedule in terminal
        if print_schedule == True:
            for room in test.Rooms:
               print_schedule.visualize_room_schedule(test.Rooms[room])    
        
        # count up diffent types of malus points
        room_capacity_points = 0
        fifth_slot_points = 0
        double_acts = 0
        singlegaps = 0
        doublegaps = 0
        triplegaps = 0

        # calculate course malus points
        for course in test.Courses:
            for activity in test.Courses[course].activities:
                room_capacity, fifth_slot = activity.get_detailed_malus()
                room_capacity_points += room_capacity
                fifth_slot_points += fifth_slot

        # calculate student malus points
        for item in test.Students:
            double_act_points, single_points, double_points, triple_points = test.Students[item].get_detailed_malus()
            double_acts += double_act_points
            singlegaps += single_points
            doublegaps += double_points
            triplegaps += triple_points
        
        # calculate total malus points
        malus = room_capacity_points + fifth_slot_points + double_acts + singlegaps + doublegaps + triplegaps
        
        # saving malus scores total & categories in lists
        malus_room_capacity.append(room_capacity_points)
        malus_fifth_slot.append(fifth_slot_points)
        malus_double_acts.append(double_acts)
        malus_single_gaps.append(singlegaps)
        malus_double_gaps.append(doublegaps)
        malus_triple_gaps.append(triplegaps)
        maluslist.append(malus)

        # print total malus points of this run
        print(f"{i}: {malus}")

    # writing csv file with malus lists
    fields = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps', 'Total']
    rows = []
    for i in range(number_of_simulations):
        row = [malus_room_capacity[i], malus_fifth_slot[i], malus_double_acts[i], malus_single_gaps[i], malus_double_gaps[i], malus_triple_gaps[i], maluslist[i]]
        rows.append(row)
    with open(f'data/{algorithm_name}_algo_simulation_data.csv', mode='w', newline="") as csvfile:
        write = csv.writer(csvfile)
        write.writerow(fields)
        write.writerows(rows)

    # print different types of malus points
    # print(f"room capacity: {room_capacity_points}   fifth: {fifth_slot_points}  \
    #     courseconflict: {double_acts}   single: {singlegaps}    double: {doublegaps}")
    
    total = 0
    for item in maluslist:
        while item > 1000000:
            item -= 1000000
        total += item
    # print(f"average: {total / len(maluslist)}")