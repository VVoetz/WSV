from code.classes import room, course, student
from code.classes import activity
import math

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
        for item in courses[course].activities:
            if str(item.id)[0] == 'h':
                for student in courses[course].students:
                    student.add_activity(item)
                    item.add_student(student)
            if str(item.id[0]) == 'w':
                for student in courses[course].students:
                    student_acts = list()
                    for activity in student.activities:
                        student_acts.append(activity.get_activity_name())
                    if item.get_activity_name() in student_acts:
                        pass
                    else:
                        if len(item.students) < item.capacity:
                            student.add_activity(item)
                            item.add_student(student)
                        else:
                            #print('test')
                            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
                            groups = 1
                            if courses[course].max_wc != "":
                                max = int(courses[course].max_wc)
                                groups = int(math.ceil(len(courses[course].students) / max))
                            if item.group == letters[groups - 1]:
                                student.add_activity(item)
                                item.add_student(student)
            if str(item.id[0]) == 'p':
                for student in courses[course].students:
                    student_acts = list()
                    for activity in student.activities:
                        student_acts.append(activity.get_activity_name())
                    if item.get_activity_name() in student_acts:
                        pass
                    else:
                        if len(item.students) < item.capacity:
                            student.add_activity(item)
                            item.add_student(student)
                        else:
                            #print('test')
                            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
                            groups = 1
                            if courses[course].max_pr != "":
                                max = int(courses[course].max_pr)
                                groups = int(math.ceil(len(courses[course].students) / max))
                                
                            if item.group == letters[groups - 1]:
                                student.add_activity(item)
                                item.add_student(student)



