from code.classes import room, course, student
from code.classes import activity
import math, random

class RandomAlgo():
    def __init__(self, data) -> None:
        """
        Random algorithm class constructor
        """
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities

        # create phantom courses
        for i in range(1, 17):
            test_act = activity.Activity('test', 'h' + str(i), 100)
            self.Activities.append(test_act)
        
        # assign all random students and activities
        random.shuffle(self.Activities)
        self.assign_all(self.Activities, self.Rooms)
        self.assign_students(self.Courses)
    
    def calculate_malus(self) -> int:
        """
        Function calculates total malus point of current solution

        post:   returns malus points as an int
        """

        malus = 0

        for student in self.Students.values():
            malus += student.get_malus()
        
        for activity in self.Activities:
            malus += activity.get_malus()
        
        return malus

    def assign_all(self, activities, rooms) -> None:
        """
        Assigns all students and acitivities

        pre:    activities is a list of activity classes
                rooms is a dictionary of room classes
        """
        for activity in activities:
            self.fill_first_room(rooms, activity)

    def fill_first_room(self, rooms, activity) -> None:
        """
        Fill the room that is available with an activity

        pre:    rooms is a room object dictionary
                activity is an activity class
        """
        for room in rooms:
            slots = rooms[room].return_availability()
            if len(slots) > 0:
                chosen_slot = slots[0]
                rooms[room].add_activity(activity, chosen_slot)
                activity.set_timeslot(chosen_slot)
                activity.set_room(rooms[room])
                break

    def assign_students(self, courses):
        """
        Function randomly assigns students to needed activities and
        tries to minimize 3 in between hours

        pre:    courses is a course dictionary
        """

        # loop over every course
        for course in courses:
            seminarlist = list() 
            practicalist = list()
            seminarset = set()
            practicaset = set()

            # register students for lecures and make seminar sets
            for item in courses[course].activities:
                if str(item.id)[0] == 'h':
                    for student in courses[course].students:
                        student.add_activity(item)
                        item.add_student(student)
                if str(item.id[0]) == 'w':
                    seminarlist.append(item)
                    seminarset.add(int(item.id[1]))
                    
                if str(item.id[0]) == 'p':
                    practicalist.append(item)
                    practicaset.add(int(item.id[1]))

            # randomly assign students to seminars
            for i in range(len(seminarset)):
                for student in courses[course].students:
                    random.shuffle(seminarlist)
                    i = 0
                    while True:
                        if student.test_malus(seminarlist[i]) < 100000:
                            student.add_activity(seminarlist[i])
                            break
                        i += 1
                        if i == len(seminarlist):
                            student.add_activity(seminarlist[0])
                            break
            
            # randomly assign students to practica
            for i in range(len(practicaset)):
                for student in courses[course].students:
                    random.shuffle(practicalist)
                    i = 0
                    while True:
                        if student.test_malus(practicalist[i]) < 100000:
                            student.add_activity(practicalist[i])
                            break
                        i += 1
                        if i == len(practicalist):
                            student.add_activity(practicalist[0])
                            break
        