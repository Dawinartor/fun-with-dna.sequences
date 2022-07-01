from multiprocessing.dummy import Array
from tokenize import String


class DNA():
    def __init__(self, sequence): # add helix directions with fifth & third
        self.sequence = String(sequence)
        
class 