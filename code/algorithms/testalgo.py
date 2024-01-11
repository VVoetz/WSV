from code.classes import room, course, student
from code.classes import activity
import math

class Testalgo():
    def __init__(self, data) -> None:
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
                self.courses[course].activity(test_act)
            
            seminars = self.courses[course].num_wc
            print(self.courses[course].num_wc)
            if self.courses[course].max_wc != "":
                max = int(self.courses[course].max_wc)
                test = math.ceil(int(self.courses[course].expected) / max)
                seminars = int(seminars) * int(test)
            for j in range(int(seminars)):
                    id = "w" + str(j + 1)
                    test_act = activity.Activity(course, id, max)
                    total_activities.append(test_act)
                    self.courses[course].activity(test_act)
            

            practica = self.courses[course].num_pr
            if self.courses[course].max_pr != "":
                max = int(self.courses[course].max_pr)
                test = math.ceil(int(self.courses[course].expected) / max)
                practica = int(practica) * int(test)
            for k in range(int(practica)):
                id = "p" + str(k + 1)
                test_act = activity.Activity(course, id, max)
                total_activities.append(test_act)
                self.courses[course].activity(test_act)
            
        
        assign_all(total_activities, self.rooms)
        assign_students(self.courses)

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
            
    