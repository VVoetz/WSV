from code.classes import room, course, student
from code.classes import activity
import math, random

class Testalgo():
    def __init__(self, data) -> None:
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities

        for i in range(1, 17):
            test_act = activity.Activity('test', 'h' + str(i), 100)
            self.Activities.append(test_act)
        print(len(self.Activities))
        random.shuffle(self.Activities)
        assign_all(self.Activities, self.Rooms)
        assign_students(self.Courses)

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
            
    