from code.classes import data_loader
from code.algorithms import testalgo
from code.visualisation import print_schedule, make_google_calendar



if __name__ == "__main__":

    data = data_loader.Data_loader("vakken.csv", "zalen.csv", "studenten_en_vakken.csv")
    test = testalgo.Testalgo(data)
    test.run()
    for room in test.Rooms:
        print_schedule.visualize_room_schedule(test.Rooms[room])    
        
    #for item in test.Students:
    #    print(f"{item}: {test.Students[item].activities}")    
    make_google_calendar.make_google_calendar_csv(data)
    make_google_calendar.make_student_calendar(data)
