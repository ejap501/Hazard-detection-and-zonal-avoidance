from math import sqrt
import os
from vector import Vector

class Buffer():
    BUFFER_SIZE = 10 # Size of the table used to store historical samples 
    buffer = [] # The table being used
    pointer = 0 # Position for next table entry
    is_filled = False # Has each table entry been used at least once
    dump = False
    fn = ""

    def __init__(self, size, filename):
        folder = "dump"
        self.BUFFER_SIZE = size
        self.buffer = [[] for i in range(size)]
        if filename != "":
            self.dump = True
            if not os.path.exists(folder): os.makedirs(folder)
            self.fn = "%s\%s" % (folder, filename)
            file = open(self.fn, 'w')
            file.close()
            
    def update(self, new_entry):

        if self.dump:
            file = open(self.fn, 'a')
            file.write(str(new_entry.magnitude()) + "\n")
            file.close()
        self.buffer[self.pointer] = new_entry
        self.pointer = (self.pointer + 1) % self.BUFFER_SIZE
        if self.pointer == 0 and self.is_filled == False:
            self.is_filled = True
        return self.buffer

    def get_size(self):
        if self.is_filled: return self.BUFFER_SIZE
        return self.pointer

    def get_buffer(self): return self.buffer

    def get_derivative(self):
        t = self.get_size()
        if t == 0: return Vector(0, 0, 0)
        n = Vector(0, 0, 0)
        for i in range(t):
            n += self.buffer[i]
        return n / t


