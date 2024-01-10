class Room():
    def __init__(self, name: str, capacity: int) -> None:
        """
        constructs Room class
        """
        self.name = name
        self.activity_dict = {}
        self.capacity = int(capacity)
        self.days = ["mo", "tu", "wo", "th", "fr"]
        for day in self.days:
            for timeslot in range(1, 5):
                self.activity_dict[day + str(timeslot)] = None
    
    def __repr__(self) -> str:
        """
        returns name of room
        """
        return self.name
    
    def show_capacity(self) -> int:
        """
        returns capacity of room
        """
        return self.capacity
    
    def add_activity(self, activity, slot: str) -> None:
        """
        adds activity to the room,
        returns False if timeslot already full
        """
        if self.check_empty(slot) == True:
            self.activity_dict[slot] = activity
        else:
            raise ValueError("Slot is already occupied, check first with check_empty(slot)")
    
    def check_empty(self, slot: str) -> bool:
        """
        checks if timeslot is empty. returns True if empty and False if not
        """
        if self.activity_dict[slot] == None:
            return True
        return False

    def remove_activity(self, activity) -> None:
        """
        removes activity from room,
        returns false if activity not in dictionary
        """
        for day in self.days:
            for timeslot in range(1, 5):
                if self.activity_dict[day + str(timeslot)] == activity:
                    self.activity_dict[day + str(timeslot)] = None
                    return
        raise ValueError("Activity not in dictionary")

    def return_availability(self) -> list():
        """
        returns list of available slots
        """
        available = list()
        for day in self.days:
            for timeslot in range(1, 5):
                if self.activity_dict[day + str(timeslot)] == None:
                    available.append(day + str(timeslot))
        return available
