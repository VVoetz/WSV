from code.classes import course, room, student

class Data_loader(object):

    def __init__(self, courses: str, rooms: str, students: str) -> None:
        """
        Dictionaries to load in data objects
        """
        self.Courses = {}
        self.Rooms = {}
        self.Students = {}
        self.Activities = []

        
        # call functions to load data
        self.load_courses(f"data/{courses}")
        self.load_rooms(f"data/{rooms}")
        self.load_students(f"data/{students}")
    

    def load_courses(self, filename: str) -> None:
        """
        Reads the given file and adds the courses as course objects into a dictionary

        pre:    filename is a file formatted as a course
        """
        
        with open(filename) as f:
            next(f) 

            # loop to read whole file by lane
            while True: 
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break

                # make course object and add it to the course dictionary
                new_course = course.Course(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                self.Courses[f"{line[0]}"] = new_course
                # add course activities to data activities
                for activity in new_course.activities:
                    self.Activities.append(activity)

        pass
    
    def load_rooms(self, filename):
        """
        Reads the given file and adds the rooms as a Room object to a dictionary

        pre:    filename is a file formatted as a room
        """

        with open(filename) as f:

            # skips header
            next(f)

            # loop to read whole file by line
            while True:
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break

                # make room object and add it to the Room dictionary
                self.Rooms[f"{line[0]}"] = room.Room(line[0], line[1])

        pass

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
                        self.Courses[line[i]].register(self.Students[f"{line[2]}"])
                    else:
                        break











