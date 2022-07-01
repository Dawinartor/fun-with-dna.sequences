from colorama import init
from colorama import Fore
# Windows platforms needs init()
init()


test = [Fore.RED + 'A', Fore.RED + 'A', Fore.BLUE + 'A', Fore.RED + 'A']

for element in test:
    print(element)
