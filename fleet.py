
from robot import Robot
class Fleet:
    def __init__(self) -> None:
        self.robots = []


    def create_fleet(self):
        self.robots.append(Robot('Mecha-Godzilla'))
        self.robots.append(Robot('Bender'))
        self.robots.append(Robot("GIR"))