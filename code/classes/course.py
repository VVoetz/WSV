from .activity import Activity
import math

class Course(object):

    def __init__(self, name: str, num_hc: str, num_wc: str, max_wc: str, num_pr: str, max_pr: str, expected: str) -> None:
        """
        Construct course objects and load according activities
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

        # load activities
        self.activities_loader()
    
    def activities_loader(self) -> None:
        lectures = int(self.num_hc)
        expected = int(self.expected)
        for i in range(lectures):
            id = "h" + str(i + 1)
            test_act = Activity(self.name, id, expected)
            self.activities.append(test_act)
        
        seminars = self.num_wc
        if self.max_wc != "":
            max = int(self.max_wc)
            test = math.ceil(int(self.expected) / max)
            seminars = int(seminars) * int(test)
            for j in range(int(seminars)):
                id = "w" + str(j + 1)
                test_act = Activity(self.name, id, max)
                self.activities.append(test_act)
        else:
            expected = int(self.expected)
            id = "w" + str(1)
            test_act = Activity(self.name, id, expected)
            self.activities.append(test_act)

        practica = self.num_pr
        if self.max_pr != "":
            max = int(self.max_pr)
            test = math.ceil(int(self.expected) / max)
            practica = int(practica) * int(test)
            for k in range(int(practica)):
                id = "p" + str(k + 1)
                test_act = Activity(self.name, id, max)
                self.activities.append(test_act)
        else:
            expected = int(self.expected)
            id = "p" + str(1) 
            test_act = Activity(self.name, id, expected)
            self.activities.append(test_act)    

    def register(self, studentnumber: str) -> None:
        """
        Add student number to this class
        """
        self.students.append(studentnumber)
        pass
    
    def activity(self, activity) -> None:
        """
        Add activity to this class

        pre:    activity is an activity class
        """
        self.activities.append(activity)
        pass