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
    
    def register(self, student):
        self.students.append(student)
    
    def activity(self, activiteit):
        self.activities.append(activiteit)