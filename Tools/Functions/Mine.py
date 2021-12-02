import json
import os
import colorama
import sys
sys.path.append("./Tools")
from CommonFunctions import coinTranslate, PrintASCII

from colorama import Fore, Back
colorama.init()

def getWallet():
    info = json.loads(open('./Tools/info.json', 'r').read())
    wallet = info[f'{coin}' + '_wallet']
    worker = info[f'{coin}' + '_worker']
    return wallet, worker

def trexMine(coin):
    try:
        wallet, worker = getWallet()
        os.system(fr"Tools\Miners\t-rex.exe -a ethash -o ethash.unmineable.com:3333 -u {coin}:{wallet}.{worker}#uj44-0zsh -p x")
        os.system("pause")
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')
def phoenixMine(coin):
    try:
        wallet, worker = getWallet()
        os.system(fr"Tools\Miners\PhoenixMiner_5.9d_Windows\PhoenixMiner.exe -pool ethash.unmineable.com:3333 -wal {coin}:{wallet}.{worker}#uj44-0zsh -pass x")
        os.system("pause")
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')
def xmrigMine(coin):
    try:
        wallet, worker = getWallet()
        os.system(fr"Tools\Miners\xmrig-6.16.1\xmrig.exe -o rx.unmineable.com:3333 -a rx -k -u {coin}:{wallet}.{worker}#uj44-0zsh -p x pause")
        os.system("pause")
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
info = json.loads(open('./Tools/info.json').read())

PrintASCII()

poolSelect = input(f"{Fore.CYAN}Would you like to CPU or GPU mine?\n{Fore.WHITE}1 - GPU\n2 - CPU\n{Fore.CYAN}Select > {Fore.WHITE}")

if poolSelect == "1":
    PrintASCII()
    minerSelect = input(f"{Fore.CYAN}Select Your Miner:\n{Fore.WHITE}1 - T-Rex (Nvidia)\n2 - PhoenixMiner (Nvidia & AMD)\n3 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if minerSelect == "1":
        minerSelect = "trex"

    elif minerSelect == "2":
        minerSelect = "phoenixminer"
    
    elif minerSelect == "3":
        os.system('python ./Start.py')
    
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
elif poolSelect == "2":
    PrintASCII()
    minerSelect = input(f"{Fore.CYAN}Select Your Miner:\n{Fore.WHITE}1 - XMRIG\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")

    if minerSelect == "1":
        minerSelect = "xmrig"
    
    elif minerSelect == "2":
        os.system('python ./Start.py')

    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Start.py')
    
else:
    print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
    input("\n\nPress Enter to Continue...")
    os.system('python ./Start.py')

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
PrintASCII()
coinSelect = input(f"{Fore.CYAN}Select the coin to mine:\n{Fore.WHITE}1 - PancakeSwap (CAKE)\n2 - SHIBA INU (SHIB)\n3 - Solana (SOL)\n4 - Cardano (ADA)\n5 - Cosmos (ATOM)\n6 - Bitcoin Cash (BCH)\n7 - Bitcoin Gold (BTG)\n8 - Dogecoin (DOGE)\n9 - Dash (DASH)\n10 - Sushi (SUSHI)\n11 - Zilliqa (ZIL)\n12 - Monero (XMR)\n13 - Ripple (XRP)\n14 - Litecoin (LTC)\n15 - Gas (GAS)\n16 - TetherUS (USDT)\n17 - NANO (NANO)\n{Fore.CYAN}Select > {Fore.WHITE}")

coin = coinTranslate(coinSelect)

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if minerSelect == "trex":
    trexMine(coin)
elif minerSelect == "phoenixminer":
    phoenixMine(coin)
elif minerSelect == "xmrig":
    xmrigMine(coin)