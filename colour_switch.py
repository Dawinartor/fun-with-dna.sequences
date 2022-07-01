from colorama import Fore, init
init() # Necessary for Windows OS

def A():
    return Fore.RED + "A"

def C():
    return Fore.YELLOW + "C"

def G():
    return Fore.GREEN + "G" 

def T():
    return Fore.BLUE + "T"


switcher = {
        "A": A,
        "C": C,
        "G": G,
        "T": T
    }


def letters_to_colours(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()