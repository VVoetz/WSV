from code.classes import room, course, student
from code.classes import activity
from code.visualisation import print_schedule
import math, random, copy

class Tabu_search():
    def __init__(self, data) -> None:
        """
        Tabu search algorithm constructor
        """
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
        self.best_data = copy.deepcopy(data)

        self.Course_list = list(self.Courses.values())
    
        self.create_initial_solution()

        self.run(1000)
    
    def create_initial_solution(self) -> None:
        """
        Function creates a "valid" initial solution to our problem
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

        # loop over all courses and all students
        for course in self.Courses.values():
            for student in course.students:

                self.register_student(course, student)
            
    def register_student(self, course, student) -> None:
        """
        Function randomly registers students into needed activities

        pre:    course and student are adequate classes
        post:   students have a valid schedule (not taking 3 in between hours into account)
        """
        
        # makes student assignment random
        random.shuffle(course.activities)

        registered_activities = set()

        for activity in course.activities:

            # register lectures
            if activity.id[0] == "h":
                activity.add_student(student)
                student.add_activity(activity)
            
            # register seminars
            else:
                seminar_id = activity.id[0:2]

                if seminar_id not in registered_activities and len(activity.students) < activity.capacity:
                    registered_activities.add(seminar_id)
                    activity.add_student(student)
                    student.add_activity(activity)

    def run(self, iterations: int) -> None:
        """
        Function runs tabu algorithm for set ammmount of iterations
        """

        tabu_list = []
        tabu_length = 500
        simulation_best = 2000

        # change 2 random activities and 2 random students for iteration ammount of times
        for iteration in range(0, iterations):

            neighbour_ammount = 100
            neighbours = self.get_neighbours(neighbour_ammount)
            
            best_neighbour = None
            best_neighbour_value = 1000000000

            # loop over found neighbours and their values
            for neighbour, value in neighbours.items():

                tabu = False

                if len(neighbour) == 2:
                    tabu = self.is_activity_swap_tabu(neighbour, tabu_list)
                elif len(neighbour) == 3:
                    tabu = self.is_activity_move_tabu(neighbour, tabu_list)
                elif len(neighbour) == 4:
                    tabu = self.is_student_swap_tabu(neighbour, tabu_list)

                if not tabu:
                    
                    # if neighbour is better than best neighbour set best neighbour
                    if value < best_neighbour_value:

                        best_neighbour = neighbour
                        best_neighbour_value = value
                else:
                    print("Tabu")
            
            if best_neighbour == None:
                best_neighbour = []

            # if activities have been swapped, swap best activities
            elif len(best_neighbour) == 2:
                activity1, activity2 = best_neighbour
                self.swap_activities(activity1, activity2)
                tabu_list.append(best_neighbour)
            
            # if activities have been moved, move best activity
            elif len(best_neighbour) == 3:
                activity1, old_roomslot, new_roomslot = best_neighbour
                new_room, new_timeslot = new_roomslot
                self.move_activity(activity1, new_room, new_timeslot)
                tabu_list.append(best_neighbour)

            # if students have been swapped, swap best students
            elif len(best_neighbour) == 4:
                student1, student2, activity1, activity2 = best_neighbour
                self.swap_students(student1, student2, activity1, activity2)
                tabu_list.append(best_neighbour)
            
            if len(tabu_list) > tabu_length:
                tabu_list.pop()

            if best_neighbour_value < simulation_best:
                simulation_best = best_neighbour_value

            print(f"iteration: {iteration}  tabu len: {len(tabu_list)}  current value: {best_neighbour_value}   sim best: {simulation_best}")

    def swap_activities(self, activity1, activity2) -> None:

        """
        Function swaps two activity roomslots in the activity and room classes

        pre:    activity1 and activity2 are activity objects
        post:   the roomslots of both activities are swapped
        """

        # swap timeslots
        activity1.timeslot, activity2.timeslot = activity2.timeslot, activity1.timeslot

        # swap rooms
        activity1.room, activity2.room = activity2.room, activity1.room

        # swap the activities in the room objects
        self.Rooms[str(activity1.room)].activity_dict[activity1.timeslot], self.Rooms[str(activity2.room)].activity_dict[activity2.timeslot] = \
            self.Rooms[str(activity2.room)].activity_dict[activity2.timeslot], self.Rooms[str(activity1.room)].activity_dict[activity1.timeslot]

        pass

    def calculate_malus(self) -> int:
        """
        Function calculates total malus point of current solution

        post:   returns malus points as an int
        """

        malus = 0

        for student in self.Students.values():
            malus += student.get_malus()
        
        for activity in self.Activities:
            malus += activity.get_malus()
        
        return malus
    
    def random_swap_activity(self) -> tuple:
        """
        Randomly swaps 2 activities
        Keeps good changes and reverts bad changes
        """

        # swap activities
        activity1 = random.choice(self.Activities)
        activity2 = random.choice(self.Activities)

        self.swap_activities(activity1, activity2)

        return activity1, activity2
    
    def swap_student_in_course(self) -> tuple:
        """
        Randomly swaps 2 students in a course

        post:   returns change in malus points as int
        """
        course = random.choice(self.Course_list)

        activity_id = self.swappable_workgroup(course)

        if activity_id != "":
            return self.swap_student_activity(course, activity_id)
        else:
            return None, None, None, None
    
    def swappable_workgroup(self, course) -> str:
        """
        Function determines if a course has enough workgroups for students to swap
        """

        id_set = set()

        # loop over all activities in a course
        for activity in course.activities:

            activity_id = activity.id

            # if activity has seperate work groups return true
            if activity_id in id_set:
                return activity_id

            id_set.add(activity_id)
        
        # return false if no seperate work groups have been found
        return ""
        
    def swap_student_activity(self, course, activity_id) -> tuple:
        """
        Function swaps 2 random students from workgroup of the given activity_id

        pre:    course is a course object
        post:   returns change in malus points as int
        """

        swappable_activities = list()

        # loop over all activities of a course
        for activity in course.activities:
            if activity.id == activity_id:
                swappable_activities.append(activity)

        # choose random activities
        activity1 = random.choice(swappable_activities)
        activity2 = random.choice(swappable_activities)

        # repeat while the 2 random activities are the same
        while activity1 == activity2:
            activity2 = random.choice(swappable_activities)

        # choose 2 random students and calculate their malus points
        student1 = random.choice(activity1.students)
        student2 = random.choice(activity2.students)

        # swap students
        self.swap_students(student1, student2, activity1, activity2)

        return student1, student2, activity1, activity2
    
    def swap_students(self, student1, student2, activity1, activity2) -> None:
        """
        Function swappes student 1 to activity 2
        and swappes student 2 to activity 1

        pre:    students have to be registered in according activities
        post:   students will have swapped activities
        """

        student1.remove_activity(activity1)
        activity1.remove_student(student1)

        student2.remove_activity(activity2)
        activity2.remove_student(student2)

        student1.add_activity(activity2)
        activity1.add_student(student2)

        student2.add_activity(activity1)
        activity2.add_student(student1)

    def get_neighbours(self, neighbour_count: int) -> dict:
        """
        Function changes the schedule and calculates the change in malus points
        then function reverts the change and saves the change and its score in a dict

        post:   returns a dict with changes and their according scores
        """
        neighbour_dict = dict()

        for neighbour in range(0, neighbour_count):
            
            weight = random.random()

            # swap random activity
            if weight < 0.2:
                
                # swap 2 random activities, calculate score and revert change
                activity1, activity2 = self.random_swap_activity()
                score = self.calculate_malus()
                self.swap_activities(activity1, activity2)

                neighbour_dict[(activity1, activity2)] = score

            # swap random student
            elif weight < 0.7:

                # swap 2 random students, calculate score and revert change
                student1, student2, activity1, activity2 = self.swap_student_in_course()
                if student1 != None:
                    score = self.calculate_malus()
                    self.swap_students(student1, student2, activity2, activity1)

                    neighbour_dict[(student1, student2, activity1, activity2)] = score
            
            # move random activity
            elif weight < 1:
                
                # move 1 random activity, calculate score and revert change
                activity1, old_roomslot, new_roomslot = self.random_move_activity()
                score = self.calculate_malus()
                old_room, old_timeslot = old_roomslot
                self.move_activity(activity1, old_room, old_timeslot)

                neighbour_dict[(activity1, old_roomslot, new_roomslot)] = score
            
            else:

                # swap student with empty
                pass
            

        return neighbour_dict

    def is_activity_swap_tabu(self, neighbour: tuple, tabu_list: list[tuple]) -> bool:
        """
        Function checks if activity combination is in the tabu list and returns corresponding bool
        """
        activity1, activity2 = neighbour
        neighbour_combo1 = (activity1, activity2)
        neighobur_combo2 = (activity2, activity1)

        if neighbour_combo1 in tabu_list or neighobur_combo2 in tabu_list:
            return True
        else:
            return False
    
    def is_student_swap_tabu(self, neighbour: tuple, tabu_list: list[tuple]) -> bool:
    
        """
        Function checks if student and activity combination 
        is in the tabu list and returns corresponding bool
        """
        student1, student2, activity1, activity2 = neighbour

        # configure different combinations
        student_activity_combo1 = (student1, student2, activity1, activity2)
        student_activity_combo2 = (student1, student2, activity2, activity1)
        student_activity_combo3 = (student2, student1, activity1, activity2)
        student_activity_combo4 = (student2, student1, activity2, activity1)

        combo_list = [student_activity_combo1, student_activity_combo2, student_activity_combo3, student_activity_combo4]

        # loop over all combo's and return true if combo is in tabu list
        for combo in combo_list:
            if combo in tabu_list:
                return True
        
        return False

    def is_activity_move_tabu(self, neighbour: tuple, tabu_list: list[tuple]) -> bool:
        """
        Function checks if move is in the tabu list
        and returns corresponding bool
        """
        activity1, old_roomslot, new_roomslot = neighbour

        if (activity1, new_roomslot, old_roomslot) in tabu_list:
            return True
        else:
            return False

    def random_move_activity(self) -> tuple:
        """
        Randomly swaps 2 activities
        Keeps good changes and reverts bad changes
        """

        # get random activity and save its roomslot
        activity1 = random.choice(self.Activities)
        old_roomslot = (activity1.room, activity1.timeslot)

        # loop until empty roomslot has been found

        found_timeslot = False

        while found_timeslot == False:
            
            # find random room and random available timeslot
            new_room = random.choice(list(self.Rooms.values()))
            available = new_room.return_availability()

            if len(available) > 0:
                new_timeslot = random.choice(available)
                found_timeslot = True
        
        self.move_activity(activity1, new_room, new_timeslot)

        new_roomslot = (new_room, new_timeslot)

        return activity1, old_roomslot, new_roomslot
    
    def move_activity(self, activity1, new_room, new_timeslot) -> None:

        """
        Changes timeslot and room of given activity
        Also change the needed room classes
        """

        # remove activity from old room
        activity1.room.remove_activity(activity1)

        # change activity values
        activity1.room = new_room
        activity1.timeslot = new_timeslot

        # add activity to new room
        new_room.add_activity(activity1, new_timeslot)

        pass