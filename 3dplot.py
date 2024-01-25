from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from code.visualisation import plots


from code.classes import data_loader

from code.algorithms import testalgo, random_algo, greedy_algo, tabu_algo, annealing

from code.visualisation import print_schedule, make_google_calendar, plots

from code.experiments import grid_search_tabu

import copy
import sys
import time
import csv




def malus_score_3d_plot( temp=0, number_of_iterations=0, number_of_simulations=0, tabu_length=0, neighbour_ammount=0):
        malus_room_capacity = list()
        malus_fifth_slot = list()
        malus_double_acts = list()
        malus_single_gaps = list()
        malus_double_gaps = list()
        malus_triple_gaps = list()
        maluslist = list()
        # iterating over all simulations
        for i in range(number_of_simulations):
            simulation_parameter = True

            while simulation_parameter:
                data = copy.deepcopy(base)

                # runs chosen algorithm
                if sys.argv[1] == 'tabu':
                    test = tabu_algo.Tabu_search(data, iterations=10, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount )
                    grid_search_tabu.run_grid_search()
                elif sys.argv[1] == 'anneal':
                    test = annealing.Tabu_search(data, temp=temp, iterations=number_of_iterations)

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

                    # #make_google_calendar.make_google_calendar_csv(data)
                    # make_google_calendar.make_student_calendar(data)






if __name__ == "__main__":
    
    # start = time.time()

    # base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    # number_of_simulations = 15

    if sys.argv[1]=='tabu':
        tabu_length = range(200,205)

        neighbour_ammount = range(10, 15)

        X = []
        Y = []
        Z = []
        for l in tabu_length:
            for n in neighbour_ammount:
                X.append(int(l))
                Y.append(int(n))
                Z.append(malus_score_3d_plot(tabu_length=tabu_length, neighbour_ammount=neighbour_ammount, number_of_simulations=number_of_simulations))

        fields = ['tabu length', 'neighbours', 'malus_avg']
        rows = []
        for i in range(len(X)):
            row = [X[i], Y[i], Z[i]]
            rows.append(row)
        with open(f'data/{sys.argv[1]}_algo_3d_data.csv', mode='w') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(fields)
            write.writerows(rows)

        plt.figure()
        # Creating figure
        fig = plt.figure(figsize =(16, 9))  
        ax = plt.axes(projection ='3d')

        # Creating color map
        my_cmap = plt.get_cmap('hot')

        # Creating plot
        trisurf = ax.plot_trisurf(X, Y, Z,
                                cmap = 'plasma',
                                linewidth = 0.2, 
                                antialiased = True,
                                edgecolor = 'grey')  
        fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)

        
        ax.set_title(f'3d plot voor {sys.argv[1]} algoritme met {number_of_simulations} simulaties')
        ax.set_xlabel('Tabu lengte')
        ax.set_ylabel('Neighbours')
        ax.set_zlabel('Maluspunten')

        # saving figure
        plt.savefig('3dplot.png')




    if sys.argv[1]=='anneal':

        # temp = np.arange(0.1, 8, 0.2)
        # number_of_iterations = []
        # for i in range(10,40):
        #     number_of_iterations.append(int(i))

        # X = []
        # Y = []
    
        # Z =[]
        # for i in temp:
        #     for j in number_of_iterations:
        #         X.append(i)
        #         Y.append(j)
        #         Z.append(malus_score_3d_plot(temp=i, number_of_iterations=j, number_of_simulations=number_of_simulations))
        # print([X, Y, Z])

        # fields = ['temperature', 'iterations', 'malus_avg']
        # rows = []
        # for i in range(len(X)):
        #     row = [X[i], Y[i], Z[i]]
        #     rows.append(row)
        # with open(f'data/{sys.argv[1]}_algo_3d_data.csv', mode='w') as csvfile:
        #     write = csv.writer(csvfile)
        #     write.writerow(fields)
        #     write.writerows(rows)


        data = plots.open_malus_csv('output.csv', method=3)
        X = data[0]
        Y = data[1]
        Z = data[2]

        plt.figure()
        # Creating figure
        fig = plt.figure(figsize =(16, 9))  
        ax = plt.axes(projection ='3d')

        # Creating color map
        my_cmap = plt.get_cmap('hot')

        # Creating plot
        trisurf = ax.plot_trisurf(X, Y, Z,
                                cmap = 'plasma',
                                linewidth = 0.2, 
                                antialiased = True,
                                edgecolor = 'grey')  
        fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)

        
        ax.set_title(f'3d plot voor {sys.argv[1]} algoritme met {len(X)} simulaties')
        ax.set_xlabel('Gevoeligheid voor Temperatuur van Studenten')
        ax.set_ylabel('Gevoeligheid voor Temperatuur van Activiteiten')
        ax.set_zlabel('Maluspunten')

        # saving figure
        plt.savefig(f'3dplot_{sys.argv[1]}_normal.png')



        plt.figure()
        # Creating figure
        fig = plt.figure(figsize =(16, 9))  
        ax = plt.axes(projection ='3d')
        ax.view_init(elev=90, azim=90, roll=0)

        # Creating color map
        my_cmap = plt.get_cmap('hot')

        # Creating plot
        trisurf = ax.plot_trisurf(X, Y, Z,
                                cmap = 'plasma',
                                linewidth = 0.2, 
                                antialiased = True,
                                edgecolor = 'grey')  
        fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)

        
        ax.set_title(f'3d plot voor {sys.argv[1]} algoritme met {len(X)} simulaties')
        ax.set_xlabel('Gevoeligheid voor Temperatuur van Studenten')
        ax.set_ylabel('Gevoeligheid voor Temperatuur van Activiteiten')
        ax.set_zlabel('Maluspunten')

        # saving figure
        plt.savefig(f'3dplot_{sys.argv[1]}_heat.png')



        plt.figure()
        # Creating figure
        fig = plt.figure(figsize =(16, 9))  
        ax = plt.axes(projection ='3d')
        ax.view_init(elev=0, azim=0, roll=0)

        # Creating color map
        my_cmap = plt.get_cmap('hot')

        # Creating plot
        trisurf = ax.plot_trisurf(X, Y, Z,
                                cmap = 'plasma',
                                linewidth = 0.2, 
                                antialiased = True,
                                edgecolor = 'grey')  
        fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)

        
        ax.set_title(f'3d plot voor {sys.argv[1]} algoritme met {len(X)} simulaties')
        ax.set_ylabel('Gevoeligheid voor Temperatuur van Activiteiten')
        ax.set_zlabel('Maluspunten')

        # saving figure
        plt.savefig(f'3dplot_{sys.argv[1]}_YZ.png')



        plt.figure()
        # Creating figure
        fig = plt.figure(figsize =(16, 9))  
        ax = plt.axes(projection ='3d')
        ax.view_init(elev=0, azim=-90, roll=0)

        # Creating color map
        my_cmap = plt.get_cmap('hot')

        # Creating plot
        trisurf = ax.plot_trisurf(X, Y, Z,
                                cmap = 'plasma',
                                linewidth = 0.2, 
                                antialiased = True,
                                edgecolor = 'grey')  
        fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)

        
        ax.set_title(f'3d plot voor {sys.argv[1]} algoritme met {len(X)} simulaties')
        ax.set_xlabel('Gevoeligheid voor Temperatuur van Studenten')
        ax.set_zlabel('Maluspunten')

        # saving figure
        plt.savefig(f'3dplot_{sys.argv[1]}_XZ.png')




    


        

            

















    # # writing csv file with malus lists & categories
    # fields = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps', 'Total']
    # rows = []
    # for i in range(number_of_simulations):
    #     row = [malus_room_capacity[i], malus_fifth_slot[i], malus_double_acts[i], malus_single_gaps[i], malus_double_gaps[i], malus_triple_gaps[i], maluslist[i]]
    #     rows.append(row)
    # with open(f'data/{sys.argv[1]}_algo_simulation_data.csv', mode='w') as csvfile:
    #     write = csv.writer(csvfile)
    #     write.writerow(fields)
    #     write.writerows(rows)

    


    # print(f"room capacity: {room_capacity_points}   fifth: {fifth_slot_points}  courseconflict: {double_acts}   single: {singlegaps}    double: {doublegaps}")
    # print(sorted(maluslist))
    # total = 0
    # for item in maluslist:
    #     while item > 1000000:
    #         item -= 1000000
    #     total += item
    # print(f"average: {total / len(maluslist)}")
        

    # end = time.time()
    # print(f"time taken: {end - start}")

    # plots.stacked_plot(f'{sys.argv[1]}_algo_simulation_data.csv', f'{sys.argv[1]}')
    # plots.plot_hist(f'{sys.argv[1]}_algo_simulation_data.csv', f'{sys.argv[1]}')
    # plots.pie_chart(f'{sys.argv[1]}_algo_simulation_data.csv', f'{sys.argv[1]}')
    # plots.stacked_hist(f'{sys.argv[1]}_algo_simulation_data.csv', f'{sys.argv[1]}')








# ## single points
# # creating axes
# ax = plt.axes(projection='3d')
# # drawing single point
# ax.scatter(3,5,7)

# # scatter plots
# ax = plt.axes(projection='3d')
# x_data = np.random.randint(0, 100, (500,))
# y_data = np.random.randint(0, 100, (500,))
# z_data = np.random.randint(0, 100, (500,))
# ax.scatter(x_data, y_data, z_data)

# # line plots
# ax = plt.axes(projection='3d')
# x_data = np.arange(0, 50, 0.1)
# y_data = np.arange(0, 50, 0.1)
# z_data = np.sin(x_data) * np.cos(y_data)
# ax.plot(x_data, y_data, z_data)
# ax.set_title('3d plot for Algorithm')
# ax.set_xlabel('X values')
# ax.set_ylabel('Y Values')
# ax.set_zlabel('Maluspunten')

# # surface plots
# #fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# x_data = np.arange(1, 10, 1)
# y_data = np.arange(1, 10, 1)

# # duplicate values
# X, Y = np.meshgrid(x_data, y_data)
# Z = np.sin(X) * np.sin(Y)
# print(len(x_data))
# print(len(X))

# plot = ax.plot_surface(X, Y, Z, cmap='plasma')
# # viewing plot from different perspective
# # ax.view_init(azim=0, elev=90)

# # adding a color bar which maps values to colors
# fig.colorbar(plot, shrink=0.5, aspect=5)
# ax.set_title('3d plot for Algorithm')
# ax.set_xlabel('X values')
# ax.set_ylabel('Y Values')
# ax.set_zlabel('Maluspunten')

# # saving figure
# plt.savefig('3dplot.png')