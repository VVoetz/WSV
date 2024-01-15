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
        self.registrations = 0

    def activities_loader(self):
        """
        Loading activities
        """
        # load activities
        lectures = int(self.num_hc)
        self.registrations = len(self.students)
        if lectures > 0:
            for i in range(lectures):
                id = "h" + str(i + 1)
                test_act = Activity(self.name, id, self.registrations)
                self.activities.append(test_act)
        
        seminars = int(self.num_wc)
        if int(self.num_wc) > 0:
            if self.max_wc != "":
                max = int(self.max_wc)
                groups = math.ceil(self.registrations / max)
                #seminars = int(seminars) * int(test)
            else:
                max = self.registrations
            for j in range(seminars):
                for k in range(groups):
                    id = "w" + str(j+1)
                    test_act = Activity(self.name, id, max, k)
                    self.activities.append(test_act)

        practica = int(self.num_pr)
        if int(self.num_pr) > 0:
            if self.max_pr != "":
                max = int(self.max_pr)
                groups = math.ceil(self.registrations / max)
                #practica = int(practica) * int(test)
            else:
                max = self.registrations
            for k in range(practica):
                for i in range(groups):
                    id = "p" + str(k + 1)
                    test_act = Activity(self.name, id, max, i)
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