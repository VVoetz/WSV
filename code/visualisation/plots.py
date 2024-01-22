import matplotlib.pyplot as plt
import seaborn as sns
import csv


def open_malus_csv(filename: str):
    """
    Writes csv files for malus points data
    """
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
            malus_room_capacity.append(line[0])
            malus_fifth_slot.append(line[1])
            malus_double_acts.append(line[2])
            malus_single_gaps.append(line[3])
            malus_double_gaps.append(line[4])
            malus_triple_gaps.append(line[5])
            maluslist.append(line[6])
    
    return [malus_room_capacity, malus_fifth_slot, malus_double_acts, malus_single_gaps, malus_double_gaps, malus_triple_gaps, maluslist]
            


def stacked_plot(categories: list, data):
    """
    Function plots stacked percentage of maluspoints per category
    """
    the_colors = sns.cubehelix_palette(4, start=0.5, rot=-.75)

    y1 = data[0]
    y2 = data[1]
    y3 = data[2]
    y4 = data[3]
    y5 = data[4]
    y6 = data[5]

    simulations = range(1, (len(y1)+1))


    # basic stacked area chart
    plt.stackplot(simulations, y1, y2, y3, y4, y5, y6, labels=categories, colors=the_colors)

    # define axes limits
    plt.xlim([1, len(y1)])
    plt.ylim([0, 1])

    # define axes labels
    plt.ylabel('Percentage maluspunten per categorie %')
    plt.xlabel('Simulaties')

    # plot text & line on top of figure
    # plt.axvline(x=, linestyle='dotted', color='black')
    # plt.text(x-coordinate, y-coordinate, 'text')

    # reverse legend color
    current_handles, current_labels = plt.gca().get_legend_handles_labels()
    plt.legend(list(reversed(current_handles)), list(reversed(current_labels)),  fontsize=9)
    plt.savefig('stacked_plot.png')

def plot_hist(filename: str):
    """
    Function plots histogram
    """
    data = []
    with open(f'{filename}.csv', mode='r') as file:
        next(file)
        csvFile = csv.reader(file)
        for lines in csvFile:
            data.append(int(lines[0]))

    fig = sns.histplot(data, kde=True)
    fig.set(xlabel='Maluspunten', ylabel='Frequentie')
    plt.savefig("code/visualisation/malus_point_plot.png")

    # plt.hist(x, bins=50, color="pink", ec="red")
    # plt.xlabel("Maluspunten")
    # plt.ylabel("Frequentie")
    # plt.savefig("code/visualisation/malus_point_plot.png")

def pie_chart(filename):
    """
    Prints circle diagram with average percentage of maluspoints per categorie
    """
    categories = {}
    for i in range(1,5):
        categories[f'category{i}']=[]

    with open(f'data/{filename}', mode='r') as file:
        next(file)
        csvFile = csv.reader(file)
        for line in csvFile:
            for i in range(1,5):
                categories[f'category{i}'].append(line[i-1])
    
    percentages = []

    for i in range(1,5):
        percentages.append(sum(categories[f'category{i}']))

    plt.pie(percentages)
    plt.savefig("code/visualisation/piechart.png")
