from code.classes import room, course, student
from code.classes import activity
import math

class Testalgo():
    def __init__(self, data) -> None:
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
                groups = int(math.ceil(int(self.Courses[course].expected) / max))

            for j in range(int(seminars)):
                for k in range(groups):
                    id = "w" + str(j + 1)
                    test_act = activity.Activity(course, id, max, k)
                    total_activities.append(test_act)
                    self.Courses[course].activity(test_act)
            

            practica = self.Courses[course].num_pr
            if self.Courses[course].max_pr != "":
                max = int(self.Courses[course].max_pr)
                groups = int(math.ceil(int(self.Courses[course].expected) / max))
            for k in range(int(practica)):
                for l in range(groups):
                    id = "p" + str(k + 1)
                    test_act = activity.Activity(course, id, max, l)
                    total_activities.append(test_act)
                    self.Courses[course].activity(test_act)
            
        
        assign_all(total_activities, self.Rooms)
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
                                groups = int(math.ceil(int(courses[course].expected) / max))
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
                                groups = int(math.ceil(int(courses[course].expected) / max))
                                
                            if item.group == letters[groups - 1]:
                                student.add_activity(item)
                                item.add_student(student)