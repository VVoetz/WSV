import matplotlib.pyplot as plt
import seaborn as sns
import csv
import numpy as np


def open_malus_csv(filename: str, method=1):
    """
    Writes csv files for malus points data
    """
    if method==1:
        malus_room_capacity = list()
        malus_fifth_slot = list()
        malus_double_acts = list()
        malus_single_gaps = list()
        malus_double_gaps = list()
        malus_triple_gaps = list()
        maluslist = list()
        with open(f'data/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                malus_room_capacity.append(float(line[0]))
                malus_fifth_slot.append(float(line[1]))
                malus_double_acts.append(float(line[2]))
                malus_single_gaps.append(float(line[3]))
                malus_double_gaps.append(float(line[4]))
                malus_triple_gaps.append(float(line[5]))
                maluslist.append(float(line[6]))
        return [malus_room_capacity, malus_fifth_slot, malus_double_acts, malus_single_gaps, malus_double_gaps, malus_triple_gaps, maluslist]

    elif method==2:
        x_data = list()
        y_data = list()
        maluslist = list()
        with open(f'data/{filename}', mode='r') as file:
            next(file)
            csvFile = csv.reader(file)
            for line in csvFile:
                x_data.append(float(line[0]))
                y_data.append(float(line[1]))
                maluslist.append(float(line[2]))
        return [x_data, y_data, maluslist]
    else:
        print('Not a valid method')
        return 0
    
            


def stacked_plot(filename: str, algo: str):
    """
    Function plots stacked percentage of maluspoints per category
    """

    # loading data
    data = open_malus_csv(filename)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []

    # saving fractional data
    for i in range(len(data[0])):
        y1.append(data[0][i]/data[6][i])
        y2.append(data[1][i]/data[6][i])
        y3.append(data[2][i]/data[6][i])
        y4.append(data[3][i]/data[6][i])
        y5.append(data[4][i]/data[6][i])
        y6.append(data[5][i]/data[6][i])
    simulations = range(1, (len(y1)+1))

    # colors
    the_colors = sns.cubehelix_palette(6, start=0.5, rot=-.75)

    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps']

    # using new clear figure
    plt.figure()
    fig, ax = plt.subplots()


    # basic stacked area chart
    plt.stackplot(simulations, y1, y2, y3, y4, y5, y6, labels=categories, colors=the_colors)

    # define axes limits
    plt.xlim([1, len(y1)])
    plt.ylim([0, 1])

    # shrink axis's height by 20 %
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # put a to the right of current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # define axes labels and title
    plt.title(f'Percentages Maluspoints per Category for the {algo} Algorithm')
    plt.ylabel('Percentage maluspunten per categorie %')
    plt.xlabel('Simulaties')

    # plot text & line on top of figure
    # plt.axvline(x=, linestyle='dotted', color='black')
    # plt.text(x-coordinate, y-coordinate, 'text')

    # reverse legend color
    plt.savefig('code/visualisation/stacked_plot.png')

def plot_hist(filename: str, algo: str):
    """
    Function plots histogram
    """
    
    # loading data
    data = open_malus_csv(filename)

    # only secting total for histogram
    data = data[6]

    # using new clear figure
    plt.figure()
    fig = sns.histplot(data, kde=True)
    fig.set(xlabel='Maluspunten', ylabel='Frequentie')
    #plt.title(f'Histogram of Maluspoints for the {algo} Algorithm')

    plt.savefig("code/visualisation/malus_point_plot.png")

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
    for i in range(6):
        Percentages[f'y{i+1}'] = []
 

    # saving fractional data
    for i in range(len(data[0])):
        for j in range(6):
            Percentages[f'y{j+1}'].append(data[j][i]/data[6][i])    
        
    average = []
    for i in range(6):
        average.append(sum(Percentages[f'y{i+1}'])/len(Percentages[f'y{i+1}']))

    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps']


    # colors
    the_colors = sns.cubehelix_palette(6, start=0.5, rot=-.75)


    # using new clear figure
    plt.figure()
    plt.pie(average, colors=the_colors, labels=categories, autopct='%1.1f%%')
    plt.title(f'Average Percentages per Category Maluspoints for the {algo} Algorithm')
    plt.savefig("code/visualisation/piechart.png")

def stacked_hist(filename: str, algo: str):

    data = open_malus_csv(filename)
    y1= data[0]
    y2= data[1]
    y3= data[2]
    y4= data[3]
    y5= data[4]
    y6= data[5]
    data = [y1, y2, y3, y4, y5, y6]



    # categories
    categories = ['Room Capacity', 'Fifth Slot Usage','Double Acts', 'Single Gaps', 'Double Gaps', 'Triple Gaps']

    # using new clear figure
    plt.figure()
    fig, ax = plt.subplots()
    the_colors = sns.cubehelix_palette(6, start=0.5, rot=-.75)
    plt.hist(data, histtype='barstacked', color=the_colors, bins=3, label=categories)

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


def three_dimensional_plot(filename: str):
    # loading correct data
    data = open_malus_csv(filename, method=2)
    x_data = data[0]
    y_data = data[1]
    z_data = data[2]
    # duplicate values
    X, Y = np.meshgrid(x_data, y_data)
    # correct Z value
    Z = np.sin(X) * np.sin(Y)

    # surface plots
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    # using new clear figure
    plt.figure()
    plot = ax.plot_surface(X, Y, Z, cmap='plasma')
    # viewing plot from different perspective
    # ax.view_init(azim=0, elev=90)

    # adding a color bar which maps values to colors
    fig.colorbar(plot, shrink=0.5, aspect=5)
    ax.set_title('3d plot for Algorithm')
    ax.set_xlabel('X values')
    ax.set_ylabel('Y Values')
    ax.set_zlabel('Maluspunten')

    # saving figure
    plt.savefig('3dplot.png')




