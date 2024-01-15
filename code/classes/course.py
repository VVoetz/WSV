from activity import Activity
import math

class Course(object):

    def __init__(self, name, num_hc, num_wc, max_wc, num_pr, max_pr, expected):
        self.name = name
        self.num_hc = num_hc
        self.num_wc = num_wc
        self.max_wc = max_wc
        self.num_pr = num_pr
        self.max_pr = max_pr
        self.expected = expected
        self.students = []
        self.activities = []

        """
        Loading activities
        """
        self.activities()
    
    def activities(self):
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

    def register(self, studentnumber):
        self.students.append(studentnumber)
    
    def activity(self, activiteit):
        self.activities.append(activiteit)