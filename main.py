from code.visualisation import print_schedule, make_google_calendar, plots

from code.experiments import anneal_grid_search, grid, run_simulation

import sys
# import time

if __name__ == "__main__":

    # --------------------------------------------------
    #
    # code to run grid searches
    #
    # --------------------------------------------------
    if sys.argv[1] == "grid":

        if len(sys.argv) < 3:
            print("Invalide input, probeer opnieuw.")

        elif sys.argv[2] == "tabu":

            # Handle user input for tabu variables
            tabu_start = input("Wat is de start waarde van de tabulijst lengte? ")
            while not tabu_start.isdigit():
                tabu_start = input("Voer een getal in... ")
            
            tabu_iteration = input("Wat is de stapgrootte van de tabulijst lengte? ")
            while not tabu_iteration.isdigit():
                tabu_iteration = input("Voer hier ook een getal in... ")

            neighbour_start = input("Met hoeveel buren wil je beginnen? ")
            while not neighbour_start.isdigit():
                neighbour_start = input("Waarom snap je niet dat het een getal moet zijn? ")
            
            neighbour_iteration = input("Wat is de stapgrootte van het aantal buren? ")
            while not neighbour_iteration.isdigit():
                neighbour_iteration = input("Je hebt nu 3 keer een getal ingevoerd... één extra keer is niet zo'n grote moeite toch? ")
            
            simulations = input("Wat is het aantal simulaties dat je wilt runnen? ")
            while not simulations.isdigit():
                simulations = input("Kom op zeg... Ik beloof je dat dit de laatste keer is dat je een getal hoeft in te voeren :) ")
            
            # make lists based on input
            tabu_lengths = []
            neighbours = []

            for i in range(abs(int(simulations))):
                tabu_lengths.append(abs(int(tabu_start)) + i * abs(int(tabu_iteration)))
                neighbours.append(abs(int(neighbour_start)) + i * abs(int(neighbour_iteration)))

            # run tabu grid search
            grid.run_grid_search("tabu", number_of_simulations = abs(int(simulations)),\
                tabu_length_list = tabu_lengths, neighbour_ammount_list = neighbours)

        elif sys.argv[2] == "anneal":

            # anneal variables
            input_test = True
            while input_test:
                input_axes = input("Hoeveel verschillende X en Y waardes wil je testen voor de gevoeligheid "
                                    "van het algoritme op de temperatuur (minimaal 2)? ")
                if input_axes.isdigit():
                    if int(input_axes) > 1:
                        input_test = False
                if input_test:
                    print("Invalide input, probeer opnieuw.")

            input_test = True
            while input_test:
                simulation_input = input('Hoeveel simulaties wil je doen per combinatie? ')
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

    # --------------------------------------------------
    #
    # code to run simulations of chosen algorithm
    #
    # --------------------------------------------------
    if sys.argv[1] == "algorithm":
        
        length = ""

        # handle user input
        if len(sys.argv) == 2:
            print("Invalide input, probeer opnieuw.")
            exit()
        elif sys.argv[2] == "anneal":
            input_test = True
            while input_test == True:
                input_duration = input("Hoe lang wil je de simulatie runnen? kort: (<1 min), medium: (~6 min), lang: (~60-80min)? ")
                if input_duration == "Lang" or input_duration == "lang":
                    length = 'long'
                    input_test = False
                elif input_duration == "Medium" or input_duration == "medium":
                    length = 'medium'
                    input_test = False
                elif input_duration == "Kort" or input_duration == "kort":
                    length = 'short'
                    input_test = False
                else:
                    print("Deze input wordt niet herkend, probeer opnieuw")

        # ammount of simulations user input
        input_test = True
        while input_test:
            simulation_input = input('Hoeveel simulaties wil je doen? ')
            if simulation_input.isdigit():
                if int(simulation_input) > 0:
                    input_test = False
            if input_test:
                print("Invalide input, probeer opnieuw.")
                
        amount_of_simulations = int(simulation_input)

        if sys.argv[2] != "anneal":
            max_time = input("Hoeveel seconden wil je het algoritme maximaal laten runnen? ")
            while not max_time.isdigit():
                max_time = input("Geef alstublieft een getal mee... ")
            
            max_time = abs(int(max_time))
        else:
            max_time = 0

        # run simulation
        if len(sys.argv) > 1:
            run_simulation.run_simulation(sys.argv[2], amount_of_simulations, False, length, max_time)
        else:
            print("Invalide input, probeer opnieuw.")
    

    # --------------------------------------------------
    #
    # code to plot with current data
    #
    # --------------------------------------------------

    if sys.argv[1] == "plot":
        if len(sys.argv) < 3:
            print("Geef een soort plot mee")
            exit()

        elif sys.argv[2] == "3d":
            
            input_test = True
            while input_test:
                simulations = input('Over hoeveel simulaties is het gemiddelde genomen? ')
                if simulations.isdigit():
                    if int(simulations) > 0:
                        input_test = False
                if input_test:
                    print("Invalide input, probeer opnieuw.")

            if sys.argv[3] == "tabu":
                plots.plot_3d("tabu_algo_3d_data.csv", simulations, "Tabu")
            if sys.argv[3] == "anneal":
                plots.plot_3d("anneal_algo_3d_data.csv", simulations, "Anneal")
        
        elif sys.argv[2] == "iteration":

            input_test = True
            while input_test:
                simulation_ammount = input('Hoevel iteratie simulaties zijn er gedaan? ')
                if simulation_ammount.isdigit():
                    if int(simulation_ammount) > 0:
                        input_test = False
                if input_test:
                    print("Invalide input, probeer opnieuw.")
            
            plots.iterative_plot(int(simulation_ammount))
        
        elif sys.argv[2] == "histogram":
            
            available_algorithms = ["tabu", "anneal", "hillclimber", "random", "greedy"]
            algorithms_to_plot = []
            algorithm = ""

            # ask for algorithms to plot
            while algorithm != "x":
                algorithm = input("Welk algoritme wil je plotten? (type x indien je klaar bent) ")
                if algorithm not in available_algorithms and algorithm != "x":
                    print("beschikbare algoritmen zijn: tabu, anneal, hillclimber, random and greedy")
                else:
                    if algorithm != "x":
                        algorithms_to_plot.append(algorithm)
            
            if len(algorithms_to_plot) < 1:
                print("Geef ten minste 1 algoritme mee")
                exit()
            
            filenames = []
            
            for algorithm in algorithms_to_plot:
                filenames.append(f"{algorithm}_algo_simulation_data.csv")
            
            plots.multi_hist(filenames, algorithms_to_plot)
        
        elif sys.argv[2] == "stacked":
            
            # handle user input
            available_algorithms = ["tabu", "anneal", "random", "greedy", "test", "hillclimber"]
            algorithm = input("Welk algoritme wil je plotten? ")
            while algorithm not in available_algorithms:
                algorithm = input("Beschikbare algoritmen zijn: tabu, anneal, random, greedy, test en hillclimber (greedy en test geven onbruikbare resultaten)")
            
            plots.stacked_plot(f"{algorithm}_algo_simulation_data.csv", algorithm)
            
        else:
            print("valide plots zijn: 3d, iteration, histogram en stacked (case sensitive :o)")
                
                
                
