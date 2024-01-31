from code.classes import room, course, student
from code.classes import activity
import math, random

class RandomAlgo():
    def __init__(self, data) -> None:
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities

        for i in range(1, 17):
            test_act = activity.Activity('test', 'h' + str(i), 100)
            self.Activities.append(test_act)
        random.shuffle(self.Activities)
        assign_all(self.Activities, self.Rooms)
        assign_students(self.Courses)
    
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

def assign_all(activities, rooms) -> None:
    for activity in activities:
        fill_first_room(rooms, activity)

def fill_first_room(rooms, activity) -> None:
    for room in rooms:
        slots = rooms[room].return_availability()
        if len(slots) > 0:
            chosen_slot = slots[0]
            rooms[room].add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(rooms[room])
            break

def assign_students(courses):
    for course in courses:
        seminarlist = list() 
        practicalist = list()
        seminarset = set()
        practicaset = set()
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
        