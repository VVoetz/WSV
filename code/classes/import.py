from classes import Room, Course, Student, Activity

Courses = {}
with open("vakken.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")
        Courses[f"{line[0]}"] = Course(line[0], line[1], line[2], line[3], line[4], line[5], line[6])

Rooms = {}
with open("zalen.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")
        Rooms[f"{line[0]}"] = Room(line[0], line[1])

Students = {}
with open("studenten_en_vakken.csv") as f:
    while True:
        #next(f) skips header
        line = f.readline()
        line = line.strip()
        line = line.split(",")
        Students[f"{line[2]}"] = Student(line[2], f"{line[0]}"+f"{line[1]}")
        Courses[f"{line[3]}"].register(line[2])





