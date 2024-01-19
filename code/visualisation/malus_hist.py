import csv
import matplotlib.pyplot as plt
import seaborn as sns

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
