import matplotlib.pyplot as plt
import seaborn as sns
import csv
import numpy as np
import pandas
import matplotlib as mpl


def open_malus_csv(filename: str, method=1, algo=''):
    """
    Writes csv files for malus points data
    """
    if method==1:
        malus_room_capacity = list()
        malus_fifth_slot = list()
        malus_double_acts = list()
        malus_single_gaps = list()
        malus_double_gaps = list()
        maluslist = list()
        with open(f'data/simulations/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                malus_room_capacity.append(float(line[0]))
                malus_fifth_slot.append(float(line[1]))
                malus_double_acts.append(float(line[2]))
                malus_single_gaps.append(float(line[3]))
                malus_double_gaps.append(float(line[4]))
                maluslist.append(float(line[6]))
        return [malus_room_capacity, malus_fifth_slot, malus_double_acts, malus_single_gaps, malus_double_gaps, maluslist]

    elif method==2:
        x_data = list()
        y_data = list()
        maluslist = list()
        with open(f'data/simulations/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                x_data.append(float(line[0]))
                y_data.append(float(line[1]))
                maluslist.append(float(line[2]))
        return [x_data, y_data, maluslist]
    elif method==3:
        x_data = []
        y_data = []
        z_data = []
        with open(f'data/grid/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                x_data.append(int(line[0]))
                y_data.append(int(line[1]))
                z_data.append(float(line[2]))
        return [x_data, y_data, z_data]
    elif method==4:
        x_data = []
        y_data = []
        with open(f'data/iterations/{algo}/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                y_data.append(float(line[0]))
                x_data.append(float(line[1]))
        return x_data, y_data

    else:
        print('Not a valid method')
        return 0
    

def multi_hist(filenames, labels):
    data = {}
    test = 0
    for i in range(len(filenames)):
        data_ = open_malus_csv(filenames[i])
        data[f'{labels[i]} N={len(data_[0])}']=data_[5]
        if len(data_[0]) < 2:
            print(f"{labels[i]} heeft niet genoeg data voor een histogram. Er moeten minstens 2 runs per algoritme zijn")
            test += 1
    if test > 0:
        exit()
    data = pandas.DataFrame(data)
    plt.figure(figsize =(16, 9)) 
    sns.set(rc={'figure.figsize':(10,8.27)})
    ax = sns.displot(data, kind='kde', fill='True').set(title="Distributies Maluspunten Algoritmes")
    ax.set(xlabel='MalusPunten')
    plt.savefig('code/visualisation/multi_hist.png')




def stacked_plot(filename: str, algo: str):
    """
    Function plots stacked percentage of maluspoints per category
    """

    # loading data
    data = open_malus_csv(filename)
    y1 = data[0]
    y2 = data[1]
    y3 = data[2]
    y4 = data[3]
    y5 = data[4]
    y6 = data[5]

    # # saving fractional data
    # for i in range(len(data[0])):
    #     y1.append(data[0][i]/data[6][i])
    #     y2.append(data[1][i]/data[6][i])
    #     y3.append(data[2][i]/data[6][i])
    #     y4.append(data[3][i]/data[6][i])
    #     y5.append(data[4][i]/data[6][i])

    simulations = range(1, (len(y1)+1))

    #sorting data
    y1_new = []
    y2_new = []
    y3_new = []
    y4_new = []
    y5_new = []

    indexes = sorted(range(len(y6)), key=lambda k: y6[k])
    for i in range(len(y6)):
        index = indexes[i]
        y1_new.append(y1[index])
        y2_new.append(y2[index])
        y3_new.append(y3[index])
        y4_new.append(y4[index])
        y5_new.append(y5[index])
        

    # colors
    the_colors = sns.cubehelix_palette(5, start=0.5, rot=-.75)

    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps']

    # using new clear figure
    plt.figure()
    fig, ax = plt.subplots()


    # basic stacked area chart
    plt.stackplot(simulations, y1_new, y2_new, y3_new, y4_new, y5_new, labels=categories, colors=the_colors)

    # define axes limits
    plt.xlim([1, len(y1)])

    # shrink axis's height by 20 %
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # put a to the right of current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # define axes labels and title
    plt.title(f'Distribution of maluspoints of {algo} Algorithm')
    plt.ylabel('Maluspoints per categorie')
    plt.xlabel('Simulaties')

    # plot text & line on top of figure
    # plt.axvline(x=, linestyle='dotted', color='black')
    # plt.text(x-coordinate, y-coordinate, 'text')

    # reverse legend color
    plt.savefig(f'code/visualisation/stacked_plots/stacked_plot_{algo}_algo.png')

def plot_hist(filename: str, algo: str):
    """
    Function plots histogram
    """
    
    # loading data
    data = open_malus_csv(filename)

    # only secting total for histogram
    print(data)
    data = data[5]

    # using new clear figure
    plt.figure()
    fig = sns.histplot(data, kde=True)
    fig.set(xlabel='Maluspunten', ylabel='Frequentie')
    #plt.title(f'Histogram of Maluspoints for the {algo} Algorithm')

    plt.savefig(f"code/visualisation/hist_plot_{algo}_algo.png")

    # plt.hist(x, bins=50, color="pink", ec="red")
    # plt.xlabel("Maluspunten")
    # plt.ylabel("Frequentie")
    # plt.savefig("code/visualisation/malus_point_plot.png")

def pie_chart(filename: str, algo: str):
    """
    Prints circle diagram with average percentage of maluspoints per categorie
    """
    # loading data
    data = open_malus_csv(filename)
    Percentages = {}
    for i in range(5):
        Percentages[f'y{i+1}'] = []
 

    # saving fractional data
    for i in range(len(data[0])):
        for j in range(5):
            Percentages[f'y{j+1}'].append(data[j][i]/data[6][i])    
        
    average = []
    for i in range(5):
        average.append(sum(Percentages[f'y{i+1}'])/len(Percentages[f'y{i+1}']))

    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps']


    # colors
    the_colors = sns.cubehelix_palette(5, start=0.5, rot=-.75)


    # using new clear figure
    plt.figure()
    plt.pie(average, colors=the_colors, labels=categories, autopct='%1.1f%%')
    plt.title(f'Average Percentages per Category Maluspoints for the {algo} Algorithm')
    plt.savefig(f"code/visualisation/piechart_{algo}_algo.png")

def stacked_hist(filename: str, algo: str):

    data = open_malus_csv(filename)
    y1= data[0]
    y2= data[1]
    y3= data[2]
    y4= data[3]
    y5= data[4]
    data = [y1, y2, y3, y4, y5]



    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps']

    # using new clear figure
    plt.figure()
    fig, ax = plt.subplots()
    the_colors = sns.cubehelix_palette(5, start=0.5, rot=-.75)
    plt.hist(data, histtype='barstacked', color=the_colors, label=categories, bins =100)

    # shrink axis's height by 20 %
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # put a to the right of current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # define axes labels and title
    plt.title(f'Percentages Maluspoints per Category for the {algo} Algorithm')
    plt.ylabel('Frequentie')
    plt.xlabel('Maluspunten')

    plt.savefig(f"code/visualisation/stacked_hist_{algo}_algo")

def iterative_plot(sim: int):

    max_iterations = 0
    plt.style.use('dark_background')
    plt.figure()
    fig, ax = plt.subplots()

    for i in range(sim):
        data = open_malus_csv(f'iteration_scores_tabu_simulation_{i+1}.csv', algo='tabu', method=4)
        line1, = ax.plot(data[0], data[1], linewidth=0.5, color='green', label='Tabu', alpha=0.5)
        data = open_malus_csv(f'iteration_scores_anneal_simulation_{i+1}.csv', algo='anneal', method=4)
        line2, = ax.plot(data[0], data[1], linewidth=0.5, color='red', label='Anneal', alpha=0.5)
        data = open_malus_csv(f'iteration_scores_hillclimber_simulation_{i+1}.csv', algo='hillclimber', method=4)
        line3, = ax.plot(data[0], data[1], linewidth=0.5, color='blue', label="Hillclimber", alpha=0.5)
        
    plt.ylim(0, 1500)
    plt.xlabel('Tijd in seconden')
    plt.ylabel('Malusscore')
    plt.title('Convergentie Maluspunten')
    ax.legend(handles=[line1, line2, line3])
    plt.savefig('code/visualisation/plot_pictures/iterative_plot.png')






def plot_3d(filename: str, number_of_simulations, algo):

    # loading data
    data = open_malus_csv(filename, method=3)
    X = data[0]
    Y = data[1]
    Z = data[2]

    x_label = {}
    x_label['Tabu'] = 'Tabu Length'
    x_label['Anneal'] = 'Gevoeligheid voor Temperatuur van Studenten'

    y_label = {}
    y_label['Tabu'] = 'Neighbours'
    y_label['Anneal'] = 'Gevoeligheid voor Temperatuur van Activiteiten'


    plt.style.use('dark_background')
    # COLOR = 'white'
    # mpl.rcParams['text.color'] = COLOR
    # mpl.rcParams['axes.labelcolor'] = COLOR
    # mpl.rcParams['xtick.color'] = COLOR
    # mpl.rcParams['ytick.color'] = COLOR
    # mpl.rcParams.update({'text.color' : "white",
    #                  'axes.labelcolor' : "white"})
    #normal 3d plots
    plt.figure()
    # Creating figure
    fig = plt.figure(figsize =(16, 9))  
    ax = plt.axes(projection ='3d')
    # Creating plot
    trisurf = ax.plot_trisurf(X, Y, Z,
                            cmap = 'plasma',
                            linewidth = 0.2, 
                            antialiased = True,
                            edgecolor = 'grey')  
    fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)
    # if algo=='anneal':
    #     ax.set_xlabel('Gevoeligheid voor Temperatuur van Studenten')
    #     ax.set_ylabel('Gevoeligheid voor Temperatuur van Activiteiten')
    #     ax.set_title(f'3d plot voor Annealing algoritme met {number_of_simulations} simulaties')
    # if algo=='tabu':
    ax.set_xlabel(f'{x_label[algo]}')
    ax.set_ylabel(f'{y_label[algo]}')
    ax.set_title(f'3d plot voor {algo} algoritme met {number_of_simulations} simulaties')
    ax.set_zlabel('Gemiddelde Maluspunten')
    # saving figure
    plt.savefig(f'code/visualisation/grid/3dplot_{algo}_normal.png')


    # heatmap
    plt.figure()
    # Creating figure
    fig = plt.figure(figsize =(16, 9))  
    ax = plt.axes(projection ='3d')
    ax.view_init(elev=90, azim=90)
    # Creating plot
    trisurf = ax.plot_trisurf(X, Y, Z,
                            cmap = 'plasma',
                            linewidth = 0.2, 
                            antialiased = True,
                            edgecolor = 'grey')  
    fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5) 
    ax.set_xlabel(f'{x_label[algo]}')
    ax.set_ylabel(f'{y_label[algo]}')
    ax.set_title(f'Maluspunten Heatmap voor {algo} algoritme met {number_of_simulations} simulaties')
    ax.set_zticklabels([])
    # saving figure
    plt.savefig(f'code/visualisation/grid/3dplot_{algo}_heat.png')

    # YZ plot
    plt.figure()
    # Creating figure
    fig = plt.figure(figsize =(16, 9))  
    ax = plt.axes(projection ='3d')
    ax.view_init(elev=0, azim=0)
    # Creating plot
    trisurf = ax.plot_trisurf(X, Y, Z,
                            cmap = 'plasma',
                            linewidth = 0.2, 
                            antialiased = True,
                            edgecolor = 'grey')  
    fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)
    ax.set_ylabel(f'{y_label[algo]}')
    ax.set_title(f'3d plot voor {algo} algoritme met {number_of_simulations} simulaties')
    ax.set_zlabel('Gemiddelde Maluspunten')
    ax.set_xticklabels([])
    # saving figure
    plt.savefig(f'code/visualisation/grid/3dplot_{algo}_YZ.png')

    # XZ plot
    plt.figure()
    # Creating figure
    fig = plt.figure(figsize =(16, 9))  
    ax = plt.axes(projection ='3d')
    ax.view_init(elev=0, azim=-90)
    # Creating plot
    trisurf = ax.plot_trisurf(X, Y, Z,
                            cmap = 'plasma',
                            linewidth = 0.2, 
                            antialiased = True,
                            edgecolor = 'grey')  
    fig.colorbar(trisurf, ax = ax, shrink = 0.5, aspect = 5)
    ax.set_xlabel(f'{x_label[algo]}')
    ax.set_title(f'3d  voor {algo} algoritme met {number_of_simulations} simulaties')
    ax.set_zlabel('Gemiddelde Maluspunten')
    ax.set_yticklabels([])
    # saving figure
    plt.savefig(f'code/visualisation/grid/3dplot_{algo}_XZ.png')



    


# def three_dimensional_plot(filename: str):
#     # loading correct data
#     data = open_malus_csv(filename, method=2)
#     x = data[0]
#     y = data[1]
#     z = d
    
#     # creating axes
#     fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

#     plot = ax.plot_surface(x, y, z, cmap='plasma')


#     # adding a color bar which maps values to colors
#     ax.set_title('3d plot for Algorithm')
#     ax.set_xlabel('X values')
#     ax.set_ylabel('Y Values')
#     ax.set_zlabel('Maluspunten')

#     # saving figure
#     plt.savefig('3dplot.png')




