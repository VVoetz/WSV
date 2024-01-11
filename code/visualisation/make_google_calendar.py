import pandas as pd

def make_google_calendar_csv(data) -> None:
    """
    This function takes data and outputs a .csv file formatted in a way
    that is compatible to be imported in a google calendar

    pre:    data is a datastructure loaded by the class Dataloader
    post:   outputs a formatted .csv file
    """

    subjects: list[str] = []
    start_dates: list[str] = []
    start_times: list[str] = []
    end_times: list[str] = []
    descriptions: list[str] = []

    for room in data.rooms.values():
        for timeslot, activity in room.activity_dict.items():

            # split day from time
            day = timeslot[0:2]
            time = timeslot[2]

            # call formatting functions
            date = format_day(day, 15, "01")
            start_time, end_time = format_time(time)

            # append existing values to according lists
            if activity != None:
                subjects.append(str(activity))
                start_dates.append(date)
                start_times.append(start_time)
                end_times.append(end_time)
                descriptions.append(str(room))
    
    # create dataframe
    df = pd.DataFrame({"Subject": subjects, "Start Date": start_dates, "Start Time": start_times, 
                        "End Time": end_times, "Description": descriptions})

    # this line only works from main.py working directory
    df.to_csv("code/visualisation/calendar_csv/calendar.csv")

def format_day(day: str, start_day: int, start_month: str) -> str:
    """
    Function takes in a day and formats it to the given date

    pre:    day is mo,tu,wo,th or fr
    post:   outputs date string
    """
    day_to_index = {"mo": 0, "tu": 1, "wo": 2, "th": 3, "fr": 4}
    date = str(start_day + day_to_index[day]) + "-" + start_month + "-2024"
    return date

def format_time(time: str) -> str:
    """
    Function take in a timeslot and formats it to the according AM and PM time

    pre:    time is an int between 1 and 4
    post:   outputs start and end time strings
    """


    time_dict = {"1": ("9:00 AM", "11:00 AM"), "2": ("11:00 AM", "1:00 PM"), "3": ("1:00 PM", "3:00 PM"), 
    "4": ("3:00 PM", "5:00 PM")}

    return time_dict[time]

def make_student_calendar(data) -> None:
    
    subjects = []
    start_dates = []
    start_times = []
    end_times = []
    descriptions = []

    for student in data.Students:
        for activity in data.Students[student].activities:
            # split day from time
            timeslot = activity.get_timeslot()
            room = str(activity.room)
            day = timeslot[0:2]
            time = timeslot[2]

            # call formatting functions
            date = format_day(day, 22, "01")
            start_time, end_time = format_time(time)

            # append existing values to according lists
            if activity != None:
                subjects.append(str(activity))
                start_dates.append(date)
                start_times.append(start_time)
                end_times.append(end_time)
                descriptions.append(str(room))
        
        break
    
    # create dataframe
    df = pd.DataFrame({"Subject": subjects, "Start Date": start_dates, "Start Time": start_times, 
                        "End Time": end_times, "Description": descriptions})

    # this line only works from main.py working directory
    df.to_csv("code/visualisation/calendar_csv/test.csv")
