from room import Room
from course import Course
from student import Student
from activity import Activity



class Importing(object):

    def __init__(self, courses, rooms, students):

        self.Courses = {}
        self.Rooms = {}
        self.Students = {}
        self.Activities = {}

        self.load_courses(f"{courses}")
        self.load_rooms(f"{rooms}")
        self.load_students(f"{students}")
    

    def load_courses(self, filename):
        with open(filename) as f:
            while True:
                #next(f) skips header?
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                self.Courses[f"{line[0]}"] = Course(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    
    def load_rooms(self, filename):
        with open(filename) as f:
            while True:
                #next(f) skips header
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                self.Rooms[f"{line[0]}"] = Room(line[0], line[1])

    def load_students(self, filename):
        with open(filename) as f:
            while True:
                #next(f) skips header
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                self.Students[f"{line[2]}"] = Student(line[2], f"{line[0]}"+f"{line[1]}")
                for i in range(1,4):
                    if line[i]!="":
                        self.Courses[line[i]].register(line[2])












