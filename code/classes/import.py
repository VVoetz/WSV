from classes import Zaal, Vak, Student, Activiteit

with open("vakken.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")
        f"{line[0]}" = Vak(line[0], line[1], line[2], line[3], line[4], line[5], line[6])

with open("zalen.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")
        f"{line[0]}" = Zaal(line[0], line[1])

with open("studenten_en_vakken.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")





