import os
import sys
from io import BytesIO
from zipfile import BadZipFile, ZipFile

print("Welcome to BetterMiner Cli! Let's get you started shall we!\n\n")

try:
    import colorama
    from colorama import Fore
    colorama.init()
    import requests
except:
    if input("Would you like to automagically install the required modules? (y/n)\n >> ") == "y":
        os.system('pip install colorama requests zipfile')
        os.system('pip install requests')
        os.system('pip install zipfile')
        import colorama
        from colorama import Fore
        colorama.init()
        from zipfile import BadZipFile, ZipFile
    else:
        print("Modules must be installed for BetterMiner to work.")
        input("\n\nPress Enter to Exit the program...")
        sys.exit()

print(f"{Fore.LIGHTBLACK_EX}Setting up config...")
open('./Tools/info.json', 'w').write('{}')
print(f"{Fore.GREEN}Config Set")
print(f"{Fore.LIGHTBLACK_EX}Downloading T-Rex...")

response = requests.get('https://github.com/trexminer/T-Rex/releases/download/0.24.7/t-rex-0.24.7-win.zip')
if response.ok:
    try:
        z = ZipFile(BytesIO(response.content))
        z.extractall("./Tools/Miners")
    except BadZipFile as f:
        print("An Error has Occured: {}".format(f))
        input("\n\nPress Enter to Exit the program...")
        sys.exit()
    
    print(f"{Fore.GREEN}Download Complete")
else:
    print("Connection Failed")
    input("\n\nPress Enter to Exit the program...")
    sys.exit()

print(f"{Fore.LIGHTBLACK_EX}Downloading PhoenixMiner...")

response = requests.get('https://github.com/ethermine/PhoenixMiner/releases/download/5.9d/PhoenixMiner_5.9d_Windows.zip', allow_redirects=True)
if response.ok:
    try:
        z = ZipFile(BytesIO(response.content))
        z.extractall("./Tools/Miners")
    except BadZipFile as f:
        print("An Error has Occured: {}".format(f))
        input("\n\nPress Enter to Exit the program...")
        sys.exit()
    
    print(f"{Fore.GREEN}Download Complete")
else:
    print("Connection Failed")
    input("\n\nPress Enter to Exit the program...")
    sys.exit()

print(f"{Fore.LIGHTBLACK_EX}Downloading XMRIG...")

response = requests.get('https://github.com/xmrig/xmrig/releases/download/v6.16.1/xmrig-6.16.1-gcc-win64.zip')
if response.ok:
    try:
        z = ZipFile(BytesIO(response.content))
        z.extractall("./Tools/Miners")
    except BadZipFile as f:
        print("An Error has Occured: {}".format(f))
        input("\n\nPress Enter to Exit the program...")
        sys.exit()
    
    print(f"{Fore.GREEN}Download Complete")
else:
    print("Connection Failed")
    input("\n\nPress Enter to Exit the program...")
    sys.exit()


print(f"{Fore.WHITE}****************\n{Fore.GREEN}Setup Complete")
input("\n\nPress Enter to Start Mining...")
os.system('python ./Start.py')