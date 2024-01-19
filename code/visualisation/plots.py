import matplotlib.pyplot as plt
import seaborn as sns
import csv

def stacked_plot(categories: list, y1, y2, y3, y4, sim: int):
    """
    Function plots stacked percentage of maluspoints per category
    """
    the_colors = sns.cubehelix_palette(4, start=0.5, rot=-.75)
    simulations = sim + 1
    simulations = range(1, simulations)
    # basic stacked area chart
    plt.stackplot(simulations, y1, y2, y3, y4, labels=categories, colors=the_colors)

    # define axes limits
    plt.xlim([1, sim])
    plt.ylim([0, 1])

    # define axes labels
    plt.ylabel('Percentage maluspunten per categorie %   ')
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
    x = []
    with open(f'{filename}.csv', mode='r') as file:
        next(file)
        csvFile = csv.reader(file)
        for lines in csvFile:
            x.append(int(lines[0]))

    fig = sns.histplot(x, kde=True)
    fig.set(xlabel='Maluspunten', ylabel='Frequentie')
    plt.savefig("code/visualisation/malus_point_plot.png")

    # plt.hist(x, bins=50, color="pink", ec="red")
    # plt.xlabel("Maluspunten")
    # plt.ylabel("Frequentie")
    # plt.savefig("code/visualisation/malus_point_plot.png")

def circle_diagram(filename):
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
