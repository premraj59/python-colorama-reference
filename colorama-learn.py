import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("\nFore.RED : " + Fore.RED + "This Will Print Red Text\n")
print("This will be Red if autoreset is not True in init()\n")
print("\\033[39m or Fore.RESET :" + "\033[39m" + "This will Make Text Normal. Not Required if autoreset=True in init()\n")

print("Here is a list of Colours Supported By Colorama:\n")

"""Giving a Background of Black to all Except Black and Reset since Terminal Color can Differ"""

print("Fore.BLACK " + Back.WHITE + Fore.BLACK + "BLACK")
print("Fore.RED " + Back.BLACK + Fore.RED + "RED")
print("Fore.GREEN " + Back.BLACK + Fore.GREEN + "GREEN")
print("Fore.YELLOW " + Back.BLACK + Fore.YELLOW + "YELLOW")
print("Fore.BLUE " + Back.BLACK + Fore.BLUE + "BLUE")
print("Fore.MAGENTA " + Back.BLACK + Fore.MAGENTA + "MAGENTA")
print("Fore.CYAN " + Back.BLACK + Fore.CYAN + "CYAN")
print("Fore.WHITE " + Back.BLACK + Fore.WHITE + "WHITE")
print("Fore.RESET " + Fore.RESET + "RESET\n")

