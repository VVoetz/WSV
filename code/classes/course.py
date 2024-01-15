class Course(object):

    def __init__(self, name: str, num_hc :str, num_wc: str, max_wc: str, num_pr: str, max_pr: str, expected: str) -> None:
        """
        Constructor for Course data-object
        """
        self.name = name
        self.num_hc = num_hc
        self.num_wc = num_wc
        self.max_wc = max_wc
        self.num_pr = num_pr
        self.max_pr = max_pr
        self.expected = expected
        self.students = []
        self.activities = []
    
    def register(self, studentnumber: str) -> None:
        """
        Adds given student number to this course

        pre:    student number is a string
        """

        self.students.append(studentnumber)
        pass
    
    def activity(self, activity) -> None:
        """
        Adds given activity to this course

        pre:    activity is an activity object
        """

        self.activities.append(activity)
        pass