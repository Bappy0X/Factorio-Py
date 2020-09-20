from colorama import init as coloramaInit, Fore, Style
coloramaInit(autoreset=True)

from player import Player

me = Player()
me.fromDB(input(f"{Fore.YELLOW}What is your username?{Style.RESET_ALL} "))

print(me)
print(me.save())