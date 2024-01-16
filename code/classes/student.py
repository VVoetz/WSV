class Student():

    def __init__(self, studentnumber: str, name: str) -> None:
        """
        Constructor of class
        """
        self.courses = list()
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
    
    def test_malus(self, activity) -> int:
        self.activities.append(activity)
        malus = self.get_malus()
        self.activities.remove(activity)
        return malus

    def get_malus(self) -> int:
        """
        Calculates and returns malus points of student
        """
        activity_dict = {}
        maluspoint = 0
        days = ["mo", "tu", "wo", "th", "fr"]
        
        # add empty lists with days as keys to activity dictionary
        for day in days:
            activity_dict[day] = list()

        # loop over activities of this student then add its timeslot 
        # to the activity dictionary with the day as key
        for activity in self.activities:
            day = activity.timeslot[0:2]
            activity_dict[day].append(int(activity.timeslot[2]))
        
        # loop over all days
        for day in days:

            # don't check with 1 or 0 activities
            if len(activity_dict[day]) < 2:
                pass
            else:

                # remove multiple courses on the same timeslot
                copy = sorted(list(set(activity_dict[day])))
                class_break = 0

                # loop over all but the last timeslot as int in a day
                for time in range(len(copy) - 1):

                    # compare current to next timeslot and calculate difference
                    class_break += (copy[time + 1] - copy[time] - 1) 
                    maluspoint += class_break

                    # add extra minus point for 2 class breaks (tussenuren)
                    if class_break == 2:
                        maluspoint += 1
                    
                    # temporary solution for 3 class_breaks
                    elif class_break == 3:
                        maluspoint += 1000000
                
                # loop over all timeslots and check for duplicates
                for timeslot in range(1, 6):
                    counter = 0

                    # loop over all timeslots of this students activities
                    for activity_timeslot in activity_dict[day]:
                        if timeslot == activity_timeslot:
                            counter += 1
                    
                    # update malus
                    if counter > 1:
                        maluspoint += counter

        return maluspoint