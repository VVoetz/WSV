from code.algorithms import tabu_algo
from code.classes import data_loader
import copy

def run_grid_search():
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

    for i in range(10):
        data = copy.deepcopy(base)
        simulation = tabu_algo.Tabu_search(data, iterations=10, tabu_length=100, neighbour_ammount=20)
