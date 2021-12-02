import json
import os
from colorama import Fore, Back, init
import sys
sys.path.append("./Tools")
from CommonFunctions import coinTranslate, PrintASCII
init()

def addInfo(newWallet, newWorker, COIN):
    with open('./Tools/info.json', 'r') as f:
        info = json.loads(f.read())
    info[f"{COIN}_wallet"] = newWallet
    info[f"{COIN}_worker"] = newWorker
    open('./Tools/info.json', 'w').write(json.dumps(info))
    os.system('python ./Start.py')

def addWalletRigID(coin):
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    PrintASCII()
    newWallet = input(f"{Fore.CYAN}Enter your wallet for the selected coin: {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    PrintASCII()
    newWorker = input(f"{Fore.CYAN}Enter your Rig ID (optional): {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    if newWorker == "":
        newWorker = "BetterMiner"


    addInfo(newWallet, newWorker, coinTranslate(coin))



PrintASCII()

addWalletRigID(input(f"{Fore.CYAN}What coin would you like to set up?{Fore.WHITE}\n1 - PancakeSwap (CAKE)\n2 - SHIBA INU (SHIB)\n3 - Solana (SOL)\n4 - Cardano (ADA)\n5 - Cosmos (ATOM)\n6 - Bitcoin Cash (BCH)\n7 - Bitcoin Gold (BTG)\n8 - Dogecoin (DOGE)\n9 - Dash (DASH)\n10 - Sushi (SUSHI)\n11 - Zilliqa (ZIL)\n12 - Monero (XMR)\n13 - Ripple (XRP)\n14 - Litecoin (LTC)\n15 - Gas (GAS)\n16 - TetherUS (USDT)\n17 - NANO (NANO) {Fore.CYAN}\n{Fore.CYAN}Select > {Fore.WHITE}"))