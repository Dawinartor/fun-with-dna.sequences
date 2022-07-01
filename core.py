from tokenize import String
import colour_switch


class DNA():
    def __init__(self, sequence): # add helix directions with fifth & third
        self.sequence = str(sequence).upper()
        
    def print(self):
        # iterate through sequenz
        for letter in self.sequence:
            # for each character check which colour to add
            print(colour_switch.letters_to_colours(letter), end='')
