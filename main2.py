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
                    plots.plot_3d("tabu_algo_3d_data.csv", simulations, "tabu")

        elif sys.argv[2] == "anneal":

            # anneal variables
            student_acceptance = [1, 2]
            activity_acceptance = [1, 2]
            simulations = 1

            # run anneal grid search

            grid.run_grid_search("anneal", number_of_simulations = simulations,\
                 acceptance_rate_student = student_acceptance, acceptance_rate_activity = activity_acceptance)
                
            if len(sys.argv) >= 3:
                if sys.argv[3] == "plot":
                    plots.plot_3d("anneal_algo_3d_data.csv", simulations, "anneal")
    
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

        # ammount of simulations
        ammount_of_simulations = 5

        if len(sys.argv) > 1:
            run_simulation.run_simulation(sys.argv[2], ammount_of_simulations)
        else:
            print("Usage: algorithm \"algorithm to run\"")


