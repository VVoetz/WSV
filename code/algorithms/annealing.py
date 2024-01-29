from code.classes import room, course, student
from code.classes import activity
import math, random


class Annealing():
    def __init__(self, data, input1=7, input2=1) -> None:
        """
        Tabu search algorithm constructor
        """
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
        self.input1 = input1
        self.input2 = input2
        self.input3 = 5
        self.malus_per_iteration = list()
        self.Course_list = list(self.Courses.values())
        
        # checks if activities are already assigned by previous algorithm. if not, an initial solution is created
        if self.Activities[0].room == None:
            self.create_initial_solution()
        self.run(10000000)
        
    
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
        Function runs simulated annealing algorithm based on the amount of iterations
        the user has given.
        """

        malus = self.calculate_malus()
        no_change = 0
        self.T = 0.2

        # change 2 random activities for iteration ammount of times
        for iteration in range(0, iterations):
            
            
            self.T = 0.999999 * self.T
            change = 0
            change += self.random_swap_activity()
            change += self.swap_student_in_course()
            if random.random() < 0.1:
                change += self.tripleswap_activity()
            
            # update malus points
            
            #print(f"{self.T} {malus_after}")
            if change == 0:
                no_change += 1
                      
            else:
                no_change = 0

            if iteration % 100 == 0:
                malus = self.calculate_malus()
                self.malus_per_iteration.append(malus)

            # if iteration % 1000 == 0:
            #     print(f"{self.calculate_malus()} {no_change} {self.T}")
            
            if no_change > 20000:
                return

    def tripleswap_activity(self) -> int:
        """
        swaps three activities at the same time, checks for the difference in maluspoints and accepts changes 
        """
        activity1 = random.choice(self.Activities)
        activity2 = random.choice(self.Activities)
        activity3 = random.choice(self.Activities)
        malus_before = activity1.get_heuristics(self.Courses, self.input3) + activity2.get_heuristics(self.Courses, self.input3) + activity3.get_heuristics(self.Courses, self.input3)
        self.swap_activities(activity1, activity2)
        self.swap_activities(activity2, activity3)

        # calculate malus points
        malus_after = activity1.get_heuristics(self.Courses, self.input3) + activity2.get_heuristics(self.Courses, self.input3)+ activity3.get_heuristics(self.Courses, self.input3)
        
        # revert bad change or return good change

        malus_diff = (malus_after - malus_before)
        if malus_after <= malus_before:
            return malus_diff
        
        prob = math.exp((-malus_diff / self.T) / (2 * self.input2))
        #print(f"{prob} {self.T} {malus_diff} {malus_before}")
        yesno = random.random() - prob
        #print(yesno)
        
        if malus_after - malus_before > 10000:
            self.swap_activities(activity2, activity3)
            self.swap_activities(activity1, activity2)
            return 0    
        if yesno > 0:
            self.swap_activities(activity2, activity3)
            self.swap_activities(activity1, activity2)
            return 0
        else:
            return malus_diff
    
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
    
    def random_move_activity(self) -> int:
        """
        Randomly moves 1 activity
        Keeps good changes and reverts bad changes
        """
        activity1 = random.choice(self.Activities)
        old_roomslot = (activity1.room, activity1.timeslot)
        old_room = activity1.room
        old_timeslot = activity1.timeslot

        # loop until empty roomslot has been found

        found_timeslot = False

        while found_timeslot == False:
            
            # find random room and random available timeslot
            new_room = random.choice(list(self.Rooms.values()))
            available = new_room.return_availability()

            if len(available) > 0:
                new_timeslot = random.choice(available)
                found_timeslot = True
        malus_before = activity1.get_heuristics(self.Courses, self.input3)
        self.move_activity(activity1, new_room, new_timeslot)
        malus_after = activity1.get_heuristics(self.Courses, self.input3)
        
        malus_diff = (malus_after - malus_before)
        if malus_after <= malus_before:
            return malus_diff
        
        prob = math.exp((-malus_diff / self.T) / (20 * self.input2))
        #print(f"{prob} {self.T} {malus_diff} {malus_before}")
        yesno = random.random() - prob
        #print(yesno)
        
        if malus_after - malus_before > 10000:
            self.move_activity(activity1, old_room, old_timeslot)
            return 0    
        if yesno > 0:
            self.move_activity(activity1, old_room, old_timeslot)
            return 0
        else:
            return malus_diff

        

    def random_swap_activity(self) -> int:
        """
        Randomly swaps 2 activities
        Keeps good changes and reverts bad changes
        """
        if random.random() < (16 / 144):
            return self.random_move_activity()
        
        # swap activities
        activity1 = random.choice(self.Activities)
        activity2 = random.choice(self.Activities)
        malus_before = activity1.get_heuristics(self.Courses, self.input3) + activity2.get_heuristics(self.Courses, self.input3)
        self.swap_activities(activity1, activity2)

        # calculate malus points
        malus_after = activity1.get_heuristics(self.Courses, self.input3) + activity2.get_heuristics(self.Courses, self.input3)
        
        # revert bad change or return good change

        malus_diff = (malus_after - malus_before)
        if malus_after <= malus_before:
            return malus_diff
        
        prob = math.exp((-malus_diff / self.T) / (2 * self.input2))
        #print(f"{prob} {self.T} {malus_diff} {malus_before}")
        yesno = random.random() - prob
        #print(yesno)
        
        if malus_after - malus_before > 10000:
            self.swap_activities(activity1, activity2)
            return 0    
        if yesno > 0:
            self.swap_activities(activity1, activity2)
            return 0
        else:
            return malus_diff
    
    def swap_student_in_course(self) -> int:
        """
        Randomly swaps 2 students in a course
        Keeps good changes and reverts bad changes

        post:   returns change in malus points as int
        """
        course = random.choice(self.Course_list)

        activity_id = self.swappable_workgroup(course)

        if activity_id != "":
            malus_change = self.swap_student_activity(course, activity_id)
            return malus_change

        else:
            return 0
    
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
        
    def swap_student_activity(self, course, activity_id) -> int:
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
        
        if random.random() < (len(activity2.students) / activity2.capacity):
            student2 = random.choice(activity2.students)
            student2malus = student2.get_malus()
            activity1malus = 0
            activity2malus = 0
        else:
            student2 = None
            student2malus = 0
            activity1malus = activity1.get_malus()
            activity2malus = activity2.get_malus()
        
        student1malus = student1.get_malus()
        

        before = activity1.get_malus() + activity2.get_malus()

        # swap students and calculate scores before and after the swap
        malus_before = student1malus + student2malus + activity1malus + activity2malus
        self.swap_students(activity1, activity2, student1, student2)
        malus_after = student1.get_malus()
        if student2:
            malus_after += student2.get_malus()
        else:
            malus_after += activity1.get_malus() + activity2.get_malus()
               

        malus_diff = (malus_after - malus_before)
        
        if malus_after <= malus_before:
            return malus_after - malus_before
        
        prob = math.exp((-malus_diff / self.T) / (5 * self.input1))
        #print(f"{prob} {self.T} {malus_diff} {malus_before}")
        yesno = random.random() - prob
        
        
        if malus_after - malus_before > 10000:
            self.swap_students(activity2, activity1, student1, student2)
            return 0      
        if yesno > 0:
            self.swap_students(activity2, activity1, student1, student2)
            return 0
        else:
            return malus_after - malus_before

    
    def swap_students(self, activity1, activity2, student1, student2=None) -> None:
        """
        Function swappes student 1 to activity 2
        and swappes student 2 to activity 1

        pre:    students have to be registered in according activities
        post:   students will have swapped activities
        """

        student1.remove_activity(activity1)
        activity1.remove_student(student1)
        student1.add_activity(activity2)
        activity2.add_student(student1)

        if student2:
            student2.remove_activity(activity2)
            activity2.remove_student(student2)
            activity1.add_student(student2)
            student2.add_activity(activity1)

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

        





        

