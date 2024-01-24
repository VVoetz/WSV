from code.algorithms import tabu_algo
from code.classes import data_loader
import copy

def run_grid_search(tabu_run):
    base = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    tabu_length = int(200 * int(tabu_run))

    for neighbour_run in range(1,11):
        data = copy.deepcopy(base)
        neighbour_ammount = 10 * neighbour_run
        simulation = tabu_algo.Tabu_search(data, iterations=10000, tabu_length=tabu_length, neighbour_ammount=neighbour_ammount, filename=f"{neighbour_ammount}neighbour_{tabu_length}tabu.csv", run_id=f"{(int(tabu_run) - 1)}{(neighbour_run - 1)}")
