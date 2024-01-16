from code.classes import room, course, student
from code.classes import activity
import math, random

class Tabu_search():
    def __init__(self, data) -> None:
        self.Courses = data.Courses
        self.Rooms = data.Rooms
        self.Students = data.Students
        self.Activities = data.Activities
    
        # TODO
        self.create_initial_solution()
        # run()
    
    def create_initial_solution(self) -> None:
        print(self.Students["84449005"].courses)

    def run(self) -> None:
        pass