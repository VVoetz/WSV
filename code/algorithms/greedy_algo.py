from code.classes import room, course, student
from code.classes import activity
import math, random

class Greedyalgo(object):

    def __init__(self, data) -> None:
        """
        Greedy algorithm constructor
        """
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities

        rooms = list()
        for room in self.Rooms:
            rooms.append(self.Rooms[room])
        
        # disables 5th timeslot to avoid maluspoints and triplegaps
        self.Rooms["C0.110"].slots = 5

        assign_all(self.Activities, rooms)
        assign_students(self.Courses)

        # re-enabling the 5th timeslot for future algorithms
        self.Rooms["C0.110"].slots = 6

def assign_all(activities, rooms: list) -> None:
    """
    Find for each activity the smallest room that it fits in and
    plan the activity for the first available timeslot
    """
    for activity in sorted(activities, key=lambda activity: activity.capacity):

        fill_smallest_room(activity, rooms)

def fill_smallest_room(activity, rooms: list) -> None:
    """
    Find for an activity the smallest room that it fits in and
    plan the activity for the first available timeslot
    """
    # finds smallest available room that suits the number of students that will be in the activity
    for room in sorted(rooms, key=lambda room: room.capacity):
        if activity.capacity <= room.capacity:
            slots = room.return_availability()
            if len(slots) > 0:
                chosen_slot = slots[0]
                room.add_activity(activity, chosen_slot)
                activity.set_timeslot(chosen_slot)
                activity.set_room(room)
                return

    #  if no room available that fits capacity, take largest available room to minimise 'maluspunten'   
    for room in sorted(rooms, key=lambda room: room.capacity, reverse=True):
        slots = room.return_availability()
        if len(slots) > 0:
            chosen_slot = slots[0]
            room.add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(room)
            return

def assign_students(courses) -> None:
    """
    Assigns students based to the activities that give them the lowest amount of maluspoints.
    Students sorted by the amount of courses they are taking.
    """
    
    for course in courses:
        seminarlist = list() 
        practicalist = list()
        seminarset = set()
        practicaset = set()
        
        
        for item in courses[course].activities:
            # assigning all students to the lectures 
            if str(item.id)[0] == 'h':
                for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                    student.add_activity(item)
                    item.add_student(student)

            # counting the number of seminars and practica
            elif str(item.id[0]) == 'w':
                seminarlist.append(item)
                seminarset.add(int(item.id[1]))  
            elif str(item.id[0]) == 'p':
                practicalist.append(item)
                practicaset.add(int(item.id[1]))

        # assigning students to the seminar that gives them the lowest amount of malus points
        for i in range(len(seminarset)):
            for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                best = 999999999
                chosen_seminar = None
                for activity in seminarlist:
                    if student.test_malus(activity) + activity.test_malus(student) < best and activity.capacity > len(activity.students):
                        best = student.test_malus(activity) + activity.test_malus(student)
                        chosen_seminar = activity     
                student.add_activity(chosen_seminar)
                chosen_seminar.add_student(student)

        # assigning students to the practica that gives them the lowest amount of malus points
        for i in range(len(practicaset)):
            for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                best = 999999999
                chosen_practica = None
                for activity in practicalist:
                    if student.test_malus(activity) + activity.test_malus(student) < best and activity.capacity > len(activity.students):
                        best = student.test_malus(activity) + activity.test_malus(student)
                        chosen_practica = activity
                student.add_activity(chosen_practica)
                chosen_practica.add_student(student)
