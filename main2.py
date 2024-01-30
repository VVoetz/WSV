from code.visualisation import print_schedule, make_google_calendar, plots

from code.experiments import grid_search_tabu, anneal_grid_search, grid, iterations, run_simulation

import sys
# import time

if __name__ == "__main__":

    # --------------------------------------------------
    # code to run grid searches
    # --------------------------------------------------
    if sys.argv[1] == "grid":

        if len(sys.argv) < 3:
            print("Usage: grid \"algorithm to grid search\"")

        elif sys.argv[2] == "tabu":

            # tabu variables
            tabu_lengths = [100, 200, 300, 400, 500]
            neighbours = [20, 25, 30, 35, 40]
            simulations = 5

            # run tabu grid search
            grid.run_grid_search("tabu", number_of_simulations = simulations,\
                tabu_length_list = tabu_lengths, neighbour_ammount_list = neighbours)
            
            if len(sys.argv) >= 4:
                if sys.argv[3] == "plot":
                    plots.plot_3d("tabu_algo_3d_data.csv", simulations, "Tabu")

        elif sys.argv[2] == "anneal":

            # anneal variables
            input_test = True
            while input_test:
                input_axes = input("Hoeveel verschillende waardes wil je testen voor de gevoeligheid "
                                    "van het algoritme op de temperatuur (minimaal 2)?")
                if input_axes.isdigit():
                    if int(input_axes) > 1:
                        input_test = False
                if input_test:
                    print("Invalide input, probeer opnieuw.")

            input_test = True
            while input_test:
                simulation_input = input('Hoeveel simulaties wil je doen per combinatie?')
                if simulation_input.isdigit():
                    if int(simulation_input) > 0:
                        input_test = False
                if input_test:
                    print("Invalide input, probeer opnieuw.")
                    
            simulations = int(simulation_input)
            student_acceptance = []
            activity_acceptance = []
            for i in range(1, int(input_axes) + 1):
                student_acceptance.append(i)
                activity_acceptance.append(i)
            
            input_test = True
            while input_test == True:
                input_duration = input("Hoe lang wil je de simulatie runnen? kort: (<1 min), medium: (~6 min), lang: (~60-80min)? ")
                if input_duration == "Lang" or input_duration == "lang":
                    length = 'long'
                    input_test = False
                elif input_duration == "Medium" or input_duration == "Medium":
                    length = 'medium'
                    input_test = False
                elif input_duration == "Kort" or input_duration == "kort":
                    length = 'short'
                    input_test = False
                else:
                    print("Deze input wordt niet herkend, probeer opnieuw")

            # run anneal grid search

            grid.run_grid_search("anneal", number_of_simulations = simulations,\
                 acceptance_rate_student = student_acceptance, acceptance_rate_activity = activity_acceptance, algo_duration=length)
                
            if len(sys.argv) >= 4:
                if sys.argv[3] == "plot":
                    plots.plot_3d("anneal_algo_3d_data.csv", simulations, "Anneal")
    
    # --------------------------------------------------
    # code to write simulations to iteration plot files
    # --------------------------------------------------
    if sys.argv[1] == "iteration":
        
        if len(sys.argv) >= 3:
            simulation_ammount = 2
            iterations.write_iterations_to_csv(sys.argv[2], simulation_ammount)
        else:
            print("Usage: iteration \"algorithm to run\"")

    # --------------------------------------------------
    # code to run simulations of chosen algorithm
    # --------------------------------------------------
    if sys.argv[1] == "algorithm":
        
        input_test = True
        while input_test == True:
            input_duration = input("Hoe lang wil je de simulatie runnen? kort: (<1 min), medium: (~6 min), lang: (~60-80min)? ")
            if input_duration == "Lang" or input_duration == "lang":
                length = 'long'
                input_test = False
            elif input_duration == "Medium" or input_duration == "Medium":
                length = 'medium'
                input_test = False
            elif input_duration == "Kort" or input_duration == "kort":
                length = 'short'
                input_test = False
            else:
                print("Deze input wordt niet herkend, probeer opnieuw")

        # ammount of simulations
        input_test = True
        while input_test:
            simulation_input = input('Hoeveel simulaties wil je doen?')
            if simulation_input.isdigit():
                if int(simulation_input) > 0:
                    input_test = False
            if input_test:
                print("Invalide input, probeer opnieuw.")
                
        amount_of_simulations = int(simulation_input)

        if len(sys.argv) > 1:
            run_simulation.run_simulation(sys.argv[2], amount_of_simulations, False, length)
        else:
            print("Usage: algorithm \"algorithm to run\"")


