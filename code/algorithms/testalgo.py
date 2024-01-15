from code.classes import room, course, student
from code.classes import activity
import math

class Testalgo():
    def __init__(self, data) -> None:
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
        
        self.run()
    
    def run(self) -> None:
        
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