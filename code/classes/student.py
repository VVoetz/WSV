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
    
    def get_malus(self) -> int:
        """
        Calculates and returns malus points of student
        """
        activity_dict = {}
        maluspunt = 0
        for day in ["mo", "tu", "wo", "th", "fr"]:
            activity_dict[day] = list()
        for item in self.activities:
            day = item.timeslot[0] + item.timeslot[1]
            activity_dict[day].append(int(item.timeslot[2]))
        for day in ["mo", "tu", "wo", "th", "fr"]:
            if len(activity_dict[day]) < 2:
                pass
            else:
                copy = sorted(list(set(activity_dict[day])))
                tussenuur = 0
                for i in range(len(copy) - 1):
                    tussenuur += (copy[i + 1] - copy[i] - 1) 
                    maluspunt += tussenuur
                    if tussenuur == 2:
                        maluspunt += 1
                    elif tussenuur == 3:
                        raise ValueError
                for i in range(1, 6):
                    counter = 0
                    for j in activity_dict[day]:
                        if j == i:
                            counter += 1
                    if counter > 1:
                        maluspunt += counter
        return maluspunt