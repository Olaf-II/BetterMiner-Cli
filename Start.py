import os
import json
import sys
import webbrowser
from Tools.CommonFunctions import PrintASCII

try:
    from colorama import Fore, Back, init
except:
    if input("Would you like to automatically install required modules and required miners? (y/n\n") == "y":
        os.system('python ./Setup.py')

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
init()

def getOption():
    PrintASCII()
    return input(f"{Fore.CYAN}What would you like to do?\n\n{Fore.LIGHTWHITE_EX}1 - Start Mining\n2 - Add Wallet\n3 - Support Server\n4 - Cashout/Monitor\n5 - Close\n\n{Fore.CYAN}Enter the corresponding number > {Fore.LIGHTWHITE_EX}")

option = getOption()

if option == "1":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    os.system('python ./Tools/Functions/Mine.py')
elif option == "2":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    os.system('python ./Tools/Functions/AddWallet.py')
elif option == "3":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    webbrowser.open_new_tab('https://discord.gg/NcdwKWrA5C')
    os.system('python ./Start.py')
elif option == "4":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    os.system('python ./Tools/Functions/Monitor.py')
elif option == "5":
    sys.exit()
else:
    print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
    input("\n\nPress Enter to Continue...")
    os.system('python ./Start.py')