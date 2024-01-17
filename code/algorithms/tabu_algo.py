from code.classes import room, course, student
from code.classes import activity
import math, random

class Tabu_search():
    def __init__(self, data) -> None:
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
    
        # TODO
        self.create_initial_solution()

        # run()
    
    def create_initial_solution(self) -> None:
        """
        Function creates a valid initial solution to our problem
        """

        self.plan_random_schedule()
        self.register_courses()
    
    def plan_random_schedule(self) -> None:
        """
        Assigns random timeslots to all activities
        """

        # loop over all activities
        for activity in self.Activities:

            assigned = False
            
            # loop until activity is assigned
            while not assigned:
                room = random.choice(list(self.Rooms.values()))
                assigned = self.plan_random_timeslot(room, activity)


    def plan_random_timeslot(self, room, activity) -> bool:
        """
        Function that plans the given activity in a random open timeslot

        pre:    room and activity are adequate objects
        post:   returns false if activity is not assigned
                returns true if activity is assigned
        """

        available = room.return_availability()
        if len(available) == 0:
            return False

        else:
            timeslot = random.choice(available)
            room.add_activity(activity, timeslot)

            activity.set_timeslot(timeslot)
            activity.set_room(room)
            return True

    def register_courses(self) -> None:
        """
        Register all students to all the lectures
        """

        # loop over all courses and all activities
        for course in self.Courses.values():
            for activity in course.activities:

                if activity.id[0] == "h":
                    self.register_lectures(course, activity)
                else:
                    self.register_seminars()

    def register_lectures(self, course, activity) -> None:
        """
        Register all the students for an activity
        """

        # loop over all students of this lecture
        for student in course.students:
            activity.add_student(student)
            student.add_activity(activity)

    def register_seminars(self) -> None:
        pass

    def run(self) -> None:
        pass