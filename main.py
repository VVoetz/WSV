from code.classes import room, course, student
from testalgo import Testalgo
from code.visualisation import visualisation



class Imports(object):

    def __init__(self, courses: str, rooms: str, students: str):
        """
        Dictionaries to load in data objects
        """
        self.Courses = {}
        self.Rooms = {}
        self.Students = {}
        self.Activities = {}

        """
        Loading the actual data
        """
        self.load_courses(f"data/{courses}")
        self.load_rooms(f"data/{rooms}")
        self.load_students(f"data/{students}")
    

    def load_courses(self, filename):
        with open(filename) as f:
            next(f) 
            while True: 
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break
                self.Courses[f"{line[0]}"] = course.Course(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    
    def load_rooms(self, filename):
        with open(filename) as f:
            next(f) 
            while True:
                #next(f) skips header
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break
                self.Rooms[f"{line[0]}"] =room.Room(line[0], line[1])

    def load_students(self, filename):
        with open(filename) as f:
            next(f)
            while True:
                #next(f) skips header
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break
                self.Students[f"{line[2]}"] = student.Student(line[2], f"{line[0]}"+f"{line[1]}")
                for i in range(3,8):
                    if line[i]!="":
                        self.Courses[line[i]].register(line[2])
                    else:
                        break



if __name__ == "__main__":

    imports = Imports("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    test = Testalgo(imports)
    test.run()
    for room in test.rooms:
        visualisation.visualize_room_schedule(test.rooms[room])
