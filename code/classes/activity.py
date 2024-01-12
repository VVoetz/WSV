class Activity:
    def __init__(self, course: str, id: str, capacity: int) -> None:
        """
        Class constructer
        """
        self.course = course
        self.id = id
        self.capacity = capacity
        self.timeslot = ""
        self.room = None
        self.students = list()
    
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
        return self.course + self.id
    
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
        Sets class room to the give room

        pre: new_room is a string
        post: room is a changed string
        """
        self.room = new_room
        pass

    def add_student(self, student) -> None:
        """
        Adds student to list
        """
        self.students.append(student)

    def student_list(self):
        """
        returns students in student list
        """
        return self.students
    
    def get_malus(self) -> int:
        """
        Returns ammount of minus point that this activity causes

        pre:    activity has a room
        post:   returns minus point that the specic activity room combination causes
        """

        # return 0 if room is not assigned
        if self.room == None:
            return 0
        
        room_capacity = self.room.capacity
        students = len(self.students)
        malus_points = room_capacity - students 

        if malus_points > 0:
            return 0
        else:
            return malus_points
