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
        # self.load_activities()
    

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
                self.Courses[f"{line[0]}"] = course.Course(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
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
        """
        Reads the given file and adds the students as a student class to a dictionary

        pre:    filename is a file formatted as a student
        """
        with open(filename) as f:

            # skip header
            next(f)

            # loop to read file by line
            while True:
                line = f.readline()
                line = line.strip()
                line = line.split(",")
                if line[0] == "":
                    break

                # make student object and add it to the student dictionary
                self.Students[f"{line[2]}"] = student.Student(line[2], f"{line[0]}"+f"{line[1]}")

                # loop over the courses of the student
                for i in range(3,8):
                    if line[i]!="":
                        self.Courses[line[i]].register(self.Students[f"{line[2]}"])
                    else:
                        break

    def load_activities(self):
        """
        Adding activities based on number of courses and number of registered students
        """
        for course in self.Courses.values():
            course.activities_loader()
            for activity in course.activities:
                self.Activities.append(activity)
    
    def swap_activities(self, activity1, activity2) -> None:
        """
        Function swaps two activity roomslots in the activity and room classes

        pre:    activity1 and activity2 are activity objects
        post:   the roomslots of both activities are swapped
        """

        # swap timeslots
        activity1.timeslot, activity2.timeslot = activity2.timeslot, activity1.timeslot

        # swap rooms
        activity1.room, activity2.room = activity2.room, activity1.room

        # swap the activities in the room objects
        self.Rooms[str(activity1.room)].activity_dict[activity1.timeslot], self.Rooms[str(activity2.room)].activity_dict[activity2.timeslot] = \
            self.Rooms[str(activity2.room)].activity_dict[activity2.timeslot], self.Rooms[str(activity1.room)].activity_dict[activity1.timeslot]

        pass
