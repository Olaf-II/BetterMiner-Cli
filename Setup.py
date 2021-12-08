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
        os.system('pip install colorama requests')
        import colorama
        from colorama import Fore
        colorama.init()
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print(Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner1.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli1.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner2.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli2.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner3.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli3.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner4.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli4.txt').read() + "\n\n")
    else:
        print("Modules must be installed for BetterMiner to work.")
        input("\n\nPress Enter to Exit the program...")
        sys.exit()

print(f"{Fore.WHITE}- Setting up config...")
open('./Tools/2minerswallet.json', 'w').write('{}')
open('./Tools/unmineablewallet.json', 'w').write('{}')
open('./Tools/unmineableprefs.json', 'w').write('{}')
print(f"- {Fore.GREEN}Config Set")

def download(link):
    response = requests.get(f'{link}')
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

print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading Trex...")
download("https://github.com/trexminer/T-Rex/releases/download/0.24.7/t-rex-0.24.7-win.zip")
print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading PhoenixMiner...")
download("https://github.com/ethermine/PhoenixMiner/releases/download/5.9d/PhoenixMiner_5.9d_Windows.zip")
print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading XMRIG...")
download("https://github.com/xmrig/xmrig/releases/download/v6.16.1/xmrig-6.16.1-gcc-win64.zip")
print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading lolMiner...")
download("https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.38/lolMiner_v1.38_Win64.zip")
print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading TeamRedMiner...")
download("https://github.com/todxx/teamredminer/releases/download/v0.8.6.3/teamredminer-v0.8.6.3-win.zip")
print(f"{Fore.WHITE}- {Fore.LIGHTBLACK_EX}Downloading GMiner...")
download("https://github.com/develsoftware/GMinerRelease/releases/download/2.73/gminer_2_73_windows64.zip")


print(f"\n\n{Fore.GREEN}Setup Complete")
input(f"{Fore.LIGHTBLACK_EX}Press Enter to Start BetterMiner Cli...")
os.system('python ./Start.py')