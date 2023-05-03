from buffer import Buffer
from vector import Vector

class Logger():
    def __init__(self):
        self.pos = Buffer(10, "")
        self.vel = Buffer(10, "velocity.txt")
        self.acc = Buffer(10, "acceleration.txt")
        self.jer = Buffer(10, "jerk.txt")

    def update(self, new_entry):
        self.pos.update(new_entry)
        self.vel.update(self.pos.get_derivative())
        self.acc.update(self.vel.get_derivative())
        self.jer.update(self.acc.get_derivative())
