from code.classes import room, course, student
from code.classes import activity
import math

class Testalgo():
    def __init__(self, data):
        self.courses = data.Courses
        self.rooms = data.Rooms
        self.students = data.Students
        self.activities = data.Activities
        
    
    def run(self):
        for course in self.courses:
            lectures = int(self.courses[course].num_hc)
            for i in range(lectures):
                id = "h" + str(i + 1)
                test_act = activity.Activity(course, id)
                room = fill_first_room(self.rooms, test_act)
            
            seminars = self.courses[course].num_wc
            if self.courses[course].max_wc != "":
                max = int(self.courses[course].max_wc)
                test = math.ceil(int(self.courses[course].expected) / max)
                seminars = int(seminars) * int(test)

            for j in range(int(seminars)):
                id = "w" + str(j + 1)
                test_act = activity.Activity(course, id)
                room = fill_first_room(self.rooms, test_act)

            practica = self.courses[course].num_pr
            if self.courses[course].max_pr != "":
                max = int(self.courses[course].max_pr)
                test = math.ceil(int(self.courses[course].expected) / max)
                practica = int(practica) * int(test)
            
            for k in range(int(practica)):
                id = "p" + str(k + 1)
                test_act = activity.Activity(course, id)
                room = fill_first_room(self.rooms, test_act)
            


def fill_first_room(rooms, activity):
    for room in rooms:
        slots = rooms[room].return_availability()
        if len(slots) > 0:
            chosen_slot = slots[0]
            rooms[room].add_activity(activity, chosen_slot)
            activity.set_timeslot(chosen_slot)
            activity.set_room(rooms[room])
            return
