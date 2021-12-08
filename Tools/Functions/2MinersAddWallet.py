import json
import os
from colorama import Fore, Back, init
import sys
sys.path.append("./Tools")
from CommonFunctions import coinTranslate2Miners, PrintASCII
init()

def addInfo(newWallet, newWorker, COIN):
    with open('./Tools/2minerswallet.json', 'r') as f:
        info = json.loads(f.read())
    info[f"{COIN}_wallet"] = newWallet
    info[f"{COIN}_worker"] = newWorker
    open('./Tools/2minerswallet.json', 'w').write(json.dumps(info))
    os.system('python ./Tools/Functions/2MinersMenu.py')

def addWalletRigID(coin):
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    PrintASCII()
    newWallet = input(f"{Fore.CYAN}Enter your wallet for the selected coin: {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    PrintASCII()
    newWorker = input(f"{Fore.CYAN}Enter your Worker (optional): {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    if newWorker == "":
        newWorker = "BetterMiner"


    addInfo(newWallet, newWorker, coinTranslate2Miners(coin))

PrintASCII()

addWalletRigID(input(f"{Fore.CYAN}What coin would you like to set up?{Fore.WHITE}\n\n1 - Monero (XMR)\n2 - Ergo (ERG)\n3 - Flux (FLUX)\n4 - Bitcoin Gold (BTG)\n5 - Cortex (CTXC)\n6 - Firo (FIRO)\n7 - Beam (BEAM)\n8 - GRIN (GRIN)\n9 - Callisto (CLO)\n10 - Aeternity (AE)\n11 - Metaverse (ETP)\n12 - MimbleWimbleCoin (MWC)\n\n{Fore.CYAN}Select > {Fore.WHITE}"))