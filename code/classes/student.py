class Student():

    def __init__(self, studentnumber: str, name: str) -> None:
        """
        Constructor of class
        """
        self.courses = []
        self.studentnumber = studentnumber
        self.name = name
        self.activities = list()

    def get_name(self) -> str:
        """
        Returns name of this student as a string
        """
        return self.name
    
    def get_studentnumber(self) -> str:
        """
        Returns student number of this student as a string
        """
        return self.studentnumber

    def add_activity(self, activity) -> None:
        """
        Adds activity to list of activities 
        """
        self.activities.append(activity)
    
    def show_activities(self):
        """
        Returns list of activities
        """
        return self.activities