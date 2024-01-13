from code.classes import room, course, student
from code.classes import activity
import math

class Greedy_algo(object):

    def __init__(self, data):
        self.courses = data.Courses
        self.rooms = data.Rooms
        self.students = data.Students
        self.activities = data.Activities
    

    def run(self) -> None:
        
        total_activities = list()

        # Adds all necessary activities per course
        for course in self.courses:
            lectures = int(self.courses[course].num_hc)
            expected = int(self.courses[course].expected)
            for i in range(lectures):
                id = "h" + str(i + 1)
                test_act = activity.Activity(course, id, expected)
                total_activities.append(test_act)
            
            seminars = self.courses[course].num_wc
            if self.courses[course].max_wc != "":
                max = int(self.courses[course].max_wc)
                test = math.ceil(int(self.courses[course].expected) / max)
                seminars = int(seminars) * int(test)
                for j in range(int(seminars)):
                    id = "w" + str(j + 1)
                    test_act = activity.Activity(course, id, max)
                    total_activities.append(test_act)
            else:
                expected = int(self.courses[course].expected)
                id = "w" + str(1)
                test_act = activity.Activity(course, id, expected)
                total_activities.append(test_act)

            practica = self.courses[course].num_pr
            if self.courses[course].max_pr != "":
                max = int(self.courses[course].max_pr)
                test = math.ceil(int(self.courses[course].expected) / max)
                practica = int(practica) * int(test)
                for k in range(int(practica)):
                    id = "p" + str(k + 1)
                    test_act = activity.Activity(course, id, max)
                    total_activities.append(test_act)
            else:
                expected = int(self.courses[course].expected)
                id = "p" + str(1) 
                test_act = activity.Activity(course, id, expected)
                total_activities.append(test_act)    
            
        assign_all(total_activities, self.rooms)

def assign_all(activities, rooms) -> None:
    for activity in sorted(activities, key=lambda x: x.capacity):
        fill_smallest_room(rooms, activity)

def fill_smallest_room(rooms, activity) -> None:
    for room in sorted(rooms, key=lambda room: room.capacity):
        if activity.capacity>room.capacity:
            break
        slots = rooms[room].return_availability()
        if len(slots) > 0:
            chosen_slot = slots[0]
            rooms[room].add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(rooms[room])
            return 0
    #  if no room available that fits capacity, take largest available room to minimise 'maluspunten'   
    for room in sorted(rooms, key=lambda room: room.capacity, reverse=True):
        slots = rooms[room].return_availability()
        if len(slots) > 0:
            chosen_slot = slots[0]
            rooms[room].add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(rooms[room])
            return 1







