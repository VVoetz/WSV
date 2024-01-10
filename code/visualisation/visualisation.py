import math

def visualize_room_schedule(room) -> None:
    """
    Function pretty prints the schedule of a room

    pre:    room is a Room object
    post:   pretty prints the given room its schedule
    """
    
    # initialize matrix format
    day_to_index = {"mo": 0, "tu": 1, "wo": 2, "th": 3, "fr": 4}
    schedule_matrix = create_empty_schedule(4, 5)

    # split day from time and update the schedule matrix for each timeslot
    for key in room.activity_dict:
        day = key[0:2]
        timeslot = int(key[2])

        # update the schedule matrix
        if room.activity_dict[key] != None:
            schedule_matrix[timeslot][day_to_index[day]] = room.activity_dict[key]
    
    width = 20
    print_schedule_matrix(schedule_matrix, width)

def create_empty_schedule(x: int, y: int) -> list[list[str]]:
    """
    function creates x by y matrix initialized with an "x" on each position

    post:   returns a x by y matrix
    """

    schedule_matrix = [["monday", "tuesday", "wednesday", "thursday", "friday"]]
    for i in range(0, x):

        schedule_matrix.append([])

        for j in range(0, y):

            schedule_matrix[i + 1].append("x")
    
    return schedule_matrix

def print_schedule_matrix(matrix: list[list[str]], width: int) -> None:
    """
    Function pretty prints the formatted 4x5 matrix

    pre:    matrix is a 4x5 matrix
    post:   prints the matrix
    """

    for i in range(0, 5):
        for j in range(0, 5):
            course_name = matrix[i][j]
            empty_characters = width - len(course_name)

            print(" " * math.floor(empty_characters / 2), end="")
            print(course_name, end="")
            print(" " * math.ceil(empty_characters / 2), end="")
        
        print("")

