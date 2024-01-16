from code.classes import room, course, student
from code.classes import activity
import math, random

class Greedyalgo(object):

    def __init__(self, data):
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities

        rooms = list()
        for room in self.Rooms:
            rooms.append(self.Rooms[room])
        assign_all(self.Activities, rooms)
        assign_students(self.Courses)

def assign_all(activities, rooms: list) -> None:
    for activity in sorted(activities, key=lambda room: room.capacity):
        fill_smallest_room(activity, rooms)

def fill_smallest_room(activity, rooms: list) -> None:
    for room in sorted(rooms, key=lambda room: room.capacity):
        if activity.capacity <= room.capacity:
            slots = room.return_availability()
            if len(slots) > 0:
                chosen_slot = slots[0]
                room.add_activity(activity, chosen_slot)
                activity.set_timeslot(chosen_slot)
                activity.set_room(room)
                return 0
    #  if no room available that fits capacity, take largest available room to minimise 'maluspunten'   
    for room in sorted(rooms, key=lambda room: room.capacity, reverse=True):
        slots = room.return_availability()
        print(room.capacity)
        if len(slots) > 0:
            chosen_slot = slots[0]
            room.add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(room)
            return 1

def assign_students(courses):
    for course in courses:
        seminarlist = list() 
        practicalist = list()
        seminarset = set()
        practicaset = set()
        
        for item in courses[course].activities:
            if str(item.id)[0] == 'h':
                for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                    student.add_activity(item)
                    item.add_student(student)
            if str(item.id[0]) == 'w':
                seminarlist.append(item)
                seminarset.add(int(item.id[1]))
                
            if str(item.id[0]) == 'p':
                practicalist.append(item)
                practicaset.add(int(item.id[1]))

        for i in range(len(seminarset)):
            for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                best = 999999999
                for activity in seminarlist:
                    if student.test_malus(activity) < best:
                        best = student.test_malus(activity)
                        chosen_seminar = activity
                student.add_activity(chosen_seminar)

        
        #sorted(rooms, key=lambda room: room.capacity, reverse=True)       
                    
        for i in range(len(practicaset)):
            for student in sorted(courses[course].students, key=lambda student: len(student.activities), reverse=True):
                best = 999999999
                for activity in practicalist:
                    if student.test_malus(activity) < best:
                        best = student.test_malus(activity)
                        chosen_seminar = activity
                student.add_activity(chosen_seminar)


