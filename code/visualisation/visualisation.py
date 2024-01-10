# WORK IN PROGRESS
def visualize_room_schedule():
    room = Room("C0.05", 150)
    activity1 = Activity("calculus 2", "h1")

    room.add_activity(activity1.get_course(), "wo1")

    for key in room.activity_dict:
        print(key, room.activity_dict[key])



if __name__ == "__main__":
    visualize_room_schedule()