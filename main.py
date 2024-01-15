from code.classes import data_loader
from code.algorithms import testalgo, random_algo, greedy_algo
from code.visualisation import print_schedule, make_google_calendar
import copy



if __name__ == "__main__":
    
    maluslist = list()
    for i in range(1):
        
        data = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")

        test = testalgo.Testalgo(data)
        test.run()

        # print(test.Courses["Calculus 2"].activities[0])
        # data.swap_activities(test.Courses["Calculus 2"].activities[0], test.Courses["Calculus 2"].activities[1])
        # print(test.Courses["Calculus 2"].activities[0])

        # print schedule in terminal
        for room in test.Rooms:
           print_schedule.visualize_room_schedule(test.Rooms[room])    
        
        # print the malus points of a course's activities
        malus = 0
        for course in data.Courses:
            for activity in data.Courses[course].activities:
                malus += activity.get_malus()

        #for activity in data.Courses["Calculus 2"].activities:
        #    print(activity.get_malus())
        
        for item in test.Students:
            malus += test.Students[item].get_malus()
        # print(f"{i}: {malus}") 
        maluslist.append(malus)
        #make_google_calendar.make_google_calendar_csv(data)
        #make_google_calendar.make_student_calendar(data)
    # print(sorted(maluslist))