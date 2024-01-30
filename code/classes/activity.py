class Activity:
    def __init__(self, course: str, id: str, capacity: int, group=None) -> None:
        """
        Class constructer
        """
        self.course = course
        self.id = id
        self.capacity = capacity
        self.timeslot = ""
        self.room = None
        self.students = list()
        self.group = ""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        if group != None:
            self.group = letters[group]
        
    
    def get_course(self) -> str:
        """
        Returns course name as string
        """
        return self.course

    def get_id(self) -> str:
        """
        Returns id name as string
        """
        return self.id
    
    def get_activity_name(self) -> str:
        """
        Returns the course name + activity type
        """
        return self.course + self.id
    
    def get_room(self) -> str:
        """
        Returns course name as string
        """
        return self.room
    
    def get_timeslot(self) -> str:
        """
        Returns timeslot as string
        """
        return self.timeslot
    
    def __repr__(self) -> str:
        """
        Returns the course name with activity id
        """
        return f"{self.course} {self.id}{self.group}"
    
    def set_timeslot(self, new_timeslot: str) -> None:
        """
        Sets class timeslot to the given timeslot

        pre:    new_timeslot is a string
        post:   timeslot is a changed string
        """
        self.timeslot = new_timeslot
        pass

    def set_room(self, new_room) -> None:
        """
        Sets class room to the given room

        pre:    new_room is a string
        post:   room is a changed string
        """
        self.room = new_room
        pass

    def add_student(self, student) -> None:
        """
        Adds student to list
        """
        self.students.append(student)
        if len(self.students) > self.capacity:
            return ValueError
    
    def remove_student(self, student) -> None:
        """
        Removes student from list

        pre:    student object has to be in list
        """
        self.students.remove(student)

    def student_list(self):
        """
        returns students in student list
        """
        return self.students
    
    def test_malus(self, student) -> int:
        """
        returns difference in maluspoints for activity if student is added
        """
        if len(self.students) >= self.capacity:
            return 1
        return 0

    def get_heuristics(self, courses, input=5) -> int:
        """
        calculates heuristic points and maluspoints and returns both combined
        """
        total = 0

        # checks if lectures are given in the 'desirable' timeslots 2 and 3
        # adds "fake" maluspoints if not
        if self.id[0] == "h":
            if self.timeslot[2] != 2 and self.timeslot[2] != 3:
                total += 5

        # checks if current seminar/practica is at the same time as another activity from the same course
        # adds "fake" maluspoints if finished
        if self.id[0] == "w" or self.id[0] == "p":
            total -= 5 * input
            for activity in courses[self.course].activities:
                if self.id[0] != "h" and activity.timeslot == self.timeslot:
                    total += 5 * input

        return total + self.get_total_malus()

    def get_total_malus(self) -> int:
        """
        calculates the maluspoints for each student in said activity
        returns all malus points of students + activity
        """
        total = 0
        total += self.get_malus()
        for student in self.students:
            total += student.get_malus()
        return total
    
    def get_malus(self) -> int:
        """
        Returns ammount of minus point that this activity causes

        pre:    activity has a room
        post:   returns minus point that the specic activity room combination causes
        """

        # return 0 if room or timeslot is not assigned or if there are no students in a course
        if self.room == "" or self.timeslot == "" or len(self.students) == 0:
            return 0
        
        room_capacity = self.room.capacity
        students = len(self.students)
        malus_points = students - room_capacity

        # if students fit in the room give no malus points
        if malus_points < 0:
            malus_points = 0

        # if timeslot is from 5 till 7 add 5 malus points
        if self.timeslot[2] == "5":
            malus_points += 5

        return malus_points
    
    def get_detailed_malus(self) -> tuple[int]:
        """
        Returns detailed ammount of minus point that this activity causes

        pre:    activity has a room
        post:   returns tuple of different types of minus points
        """

        # return 0 if room or timeslot is not assigned or if there are no students in a course
        if self.room == "" or self.timeslot == "" or len(self.students) == 0:
            return 0, 0
        
        room_capacity = self.room.capacity
        students = len(self.students)

        room_capacity_malus_points = students - room_capacity
        fifth_timeslot_malus_points = 0

        # if students fit in the room give no malus points
        if room_capacity_malus_points < 0:
            room_capacity_malus_points = 0

        # if timeslot is from 5 till 7 add 5 malus points
        if self.timeslot[2] == "5":
            fifth_timeslot_malus_points += 5

        return room_capacity_malus_points, fifth_timeslot_malus_points
