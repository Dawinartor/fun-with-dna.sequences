from tokenize import String
from colour_switch import letters_to_colours


class DNA():
    def __init__(self, sequence): # add helix directions with fifth & third
        self.sequence = str(sequence).upper()
        
    def print(self):
        # iterate through sequenz
        for letter in self.sequence:
            # for each character check which colour to add
            print(letters_to_colours(letter), end='')
