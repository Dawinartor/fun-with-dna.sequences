from multiprocessing.dummy import Array
from tokenize import String
import colour_switch

class DNA():
    def __init__(self, sequence): # add helix directions with fifth & third
        self.sequence = str(sequence).upper()
        
    def print(self):
        colouredString = []
        # iterate through sequenz
        for letter in self.sequence:
            # for each character chech which colour to add
            colouredString.append(colour_switch.letters_to_colours(letter))
        print(colouredString)
            