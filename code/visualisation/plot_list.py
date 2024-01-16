import matplotlib.pyplot as plt

def plot_malus(malus_list: list[int], color="r", size=100) -> None:
    """
    Function takes in a list of malus points and plots it in a diagram

    pre:    malus list is a list of values
    """

    # create scatter plot with run on x and value on y with given color and size
    plt.scatter(range(0,len(malus_list)), malus_list, color=color, s=size)
    plt.xlim(0, len(malus_list) - 1)
    plt.savefig("code/visualisation/malus_point_plot.png")