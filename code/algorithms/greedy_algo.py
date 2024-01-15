from code.classes import room, course, student
from code.classes import activity
import math

class Greedyalgo(object):

    def __init__(self, data):
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
    

    def run(self) -> None:
        
        total_activities = list()

        # Adds all necessary activities per course
        for course in self.Courses:
            lectures = int(self.Courses[course].num_hc)
            expected = int(self.Courses[course].expected)
            for i in range(lectures):
                id = "h" + str(i + 1)
                test_act = activity.Activity(course, id, expected)
                total_activities.append(test_act)
                self.Courses[course].activity(test_act)
            
            seminars = self.Courses[course].num_wc
            if self.Courses[course].max_wc != "":
                max = int(self.Courses[course].max_wc)
                test = math.ceil(int(self.Courses[course].expected) / max)
                seminars = int(seminars) * int(test)
            for j in range(int(seminars)):
                id = "w" + str(j + 1)
                test_act = activity.Activity(course, id, max)
                total_activities.append(test_act)
                self.Courses[course].activity(test_act)
            

            practica = self.Courses[course].num_pr
            if self.Courses[course].max_pr != "":
                max = int(self.Courses[course].max_pr)
                test = math.ceil(int(self.Courses[course].expected) / max)
                practica = int(practica) * int(test)
            for k in range(int(practica)):
                id = "p" + str(k + 1)
                test_act = activity.Activity(course, id, max)
                total_activities.append(test_act)
                self.Courses[course].activity(test_act) 


        rooms = list()
        for room in self.Rooms:
            rooms.append(self.Rooms[room])
        assign_all(total_activities, rooms)
        assign_students(self.Courses)

def assign_all(activities, rooms: list) -> None:
    for activity in sorted(activities, key=lambda room: room.capacity):
        fill_smallest_room(activity, rooms)

def fill_smallest_room(activity, rooms: list) -> None:
    for room in sorted(rooms, key=lambda room: room.capacity):
        if activity.capacity>room.capacity:
            break
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
        if len(slots) > 0:
            chosen_slot = slots[0]
            room.add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(room)
            return 1

def assign_students(courses):
    for course in courses:
        for item in courses[course].activities:
            if str(item.id)[0] == 'h':
                for student in courses[course].students:
                    student.add_activity(item)
                    item.add_student(student)
            if str(item.id[0]) == 'w':
                for student in courses[course].students:
                    student.add_activity(item)
                    item.add_student(student)
            if str(item.id[0]) == 'p':
                for student in courses[course].students:
                    student.add_activity(item)
                    item.add_student(student)






