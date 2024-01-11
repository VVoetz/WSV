import pandas as pd

# self.courses dictionary key = coursename value = object
# self.rooms dictionary key = roomname value = object
# self.students dictionary key = studentnumber value = object
# self.activities empty dictionary


# Subject is course name
# Description is room

def make_google_calendar_csv(data):
    """
    This function takes data and outputs a .csv file formatted in a way
    that is compatible to be imported in a google calendar

    pre:    data is a datastructure loaded by the class Dataloader
    post:   outputs a formatted .csv file
    """

    df = pd.DataFrame({"Subject": [], "Start Date": [], "Start Time": [], "End Time": [], "Description": []})

    print(data.activities)

print(df)