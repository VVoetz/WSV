import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
import numpy as np
import csv

def plot_malus(malus_list: list[int], color="r", size=100) -> None:
    """
    Function takes in a list of malus points and plots it in a diagram

    pre:    malus list is a list of values
    """

    # create scatter plot with run on x and value on y with given color and size
    upper = max(malus_list)
    lower = min(malus_list)
    difference = upper - lower

    plt.scatter(range(0,len(malus_list)), malus_list, color=color, s=size)
    plt.xlim(0, len(malus_list) - 1)
    plt.ylim(lower - difference, upper + difference)
    plt.savefig("code/visualisation/malus_point_plot.png")


def plot_3d_hist():



    with open("code/experiments/grid_search_tabu_results/best_scores.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        empty = []
        for i in range(0,10):
            empty.append([])
            for j in range(0,10):
                empty[i].append(0)

        for row in csv_reader:

            x, y, z = row[0], row[1], row[2]

            empty[int(x)][int(y)] = int(z)
        max = 0
        for i in range(0,10):
            for j in range(0,10):
                if empty[i][j] > max:
                    max = empty[i][j]
                
        for i in range(0,10):
            for j in range(0,10):
                empty[i][j] /= max
        


        sns.heatmap(data = empty, annot=True)
            

    

    plt.show()

    

if __name__ == "__main__":
    plot_3d_hist()