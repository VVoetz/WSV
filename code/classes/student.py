class Student():

    def __init__(self, studentnumber: str, name: str, courses: list[str]) -> None:
        """
        Constructor of class
        """
        self.courses = [courses]
        self.studentnumber = studentnumber
        self.name = name

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
