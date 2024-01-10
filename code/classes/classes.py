class Vak(object):

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
    
    def register(student):
        self.students.append(student)
    
    def activity(activiteit):
        self.activities.append(activiteit)


class Zaal(object):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.tijdsloten = []

    def activity(activiteit):
        self.tijdsloten.append(activiteit)


class Activiteit(object):

    def __init__(self,name):


class Student(object):
    
    def __init__(self, surname, name, number, course1, course2, course3, course4, course5)
        self.surname = surname
        self.name = name
        self.number = number
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4
        self.course5 = course5


        