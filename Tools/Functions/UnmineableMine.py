import json
import os
import colorama
import sys
sys.path.append("./Tools")
from CommonFunctions import coinTranslate, PrintASCII

from colorama import Fore, Back
colorama.init()



def useCurrentInfo(prefs):
    prefMiner = prefs["miner"]
    prefPool = prefs["pool"]
    useCurrentInfoOption = input(f"{Fore.CYAN}Would you like to use your saved configuration?\n\n{Fore.WHITE}Miner - {prefMiner}\nPool - {prefPool}\n\n{Fore.CYAN}Select (y/n) > {Fore.WHITE}")
    if useCurrentInfoOption == "y":
        if prefPool == "Ethash":
            ethash = True
        else:
            ethash = False

        PrintASCII()
        coinSelect = input(f"{Fore.CYAN}Select the coin to mine:\n\n{Fore.WHITE}1 - PancakeSwap (CAKE)\n2 - SHIBA INU (SHIB)\n3 - Solana (SOL)\n4 - Cardano (ADA)\n5 - Cosmos (ATOM)\n6 - Bitcoin Cash (BCH)\n7 - Bitcoin Gold (BTG)\n8 - Dogecoin (DOGE)\n9 - Dash (DASH)\n10 - Sushi (SUSHI)\n11 - Zilliqa (ZIL)\n12 - Monero (XMR)\n13 - Ripple (XRP)\n14 - Litecoin (LTC)\n15 - Gas (GAS)\n16 - TetherUS (USDT)\n17 - NANO (NANO)\n18 - Dogelon (ELON)\n\n{Fore.CYAN}Select > {Fore.WHITE}")
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        coin = coinTranslate(coinSelect)

        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if prefMiner == "trex":
            trexMine(coin, ethash)
        elif prefMiner == "phoenixminer":
            phoenixMine(coin, ethash)
        elif prefMiner == "xmrig":
            xmrigMine(coin)
    else:
        return "exit"

def prefSave(miner, ethash):
    PrintASCII()
    if ethash:
        ethash = "Ethash"
    else:
        ethash = "Etchash"

    if miner == "trex":
        formattedMiner = "T-Rex"
    elif miner == "phoenixminer":
        formattedMiner = "PhoenixMiner"
    elif miner == "xmrig":
        formattedMiner = "XMRig"
    saveOption = input(f"{Fore.CYAN}Would you like to save these settings?\n\n{Fore.WHITE}Miner: {formattedMiner}\nPool: {ethash}\n\n{Fore.CYAN}Select (y/n) > {Fore.WHITE}")
    if saveOption == "y":
        saveInfo = {
            "miner": miner,
            "pool": ethash
        }
        open('./Tools/unmineableprefs.json', 'w').write(json.dumps(saveInfo))
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    else:
        pass

def getWallet(coin):
    info = json.loads(open('./Tools/info.json', 'r').read())
    wallet = info[f'{coin}' + '_wallet']
    worker = info[f'{coin}' + '_worker']
    return wallet, worker

def trexMine(coin, ethash):
    try:
        wallet, worker = getWallet(coin)
        try:
            if ethash:
                os.system(fr"Tools\Miners\t-rex.exe -a ethash -o ethash.unmineable.com:3333 -u {coin}:{wallet}.{worker}#uj44-0zsh -p x")
                os.system("pause")
            else:
                os.system(fr"Tools\Miners\t-rex.exe -a etchash -o etchash.unmineable.com:3333 -u {coin}:{wallet}.{worker}#uj44-0zsh -p x")
                os.system("pause")
        except:
            os.system('python ./Start.py')
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

def phoenixMine(coin, ethash):
    try:
        wallet, worker = getWallet(coin)
        try:
            if ethash:
                os.system(fr"Tools\Miners\PhoenixMiner_5.9d_Windows\PhoenixMiner.exe -logfile /Tools/PhoenixLog.txt -pool ethash.unmineable.com:3333 -wal {coin}:{wallet}.{worker}#uj44-0zsh -pass x")
                os.system("pause")
            else:
                os.system(fr"Tools\Miners\PhoenixMiner_5.9d_Windows\PhoenixMiner.exe -logfile /Tools/PhoenixLog.txt -pool etchash.unmineable.com:3333 -wal {coin}:{wallet}.{worker}#uj44-0zsh -pass x")
                os.system("pause")
        except:
            os.system('python ./Start.py')
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

def xmrigMine(coin):
    try:
        wallet, worker = getWallet(coin)
        try:
            os.system(fr"Tools\Miners\xmrig-6.16.1\xmrig.exe -o rx.unmineable.com:3333 -a rx -k -u {coin}:{wallet}.{worker}#uj44-0zsh -p x pause")
            os.system("pause")
        except:
            os.system('python ./Start.py')
    except:
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

if os.path.isfile('./Tools/Miners/t-rex.exe') and os.path.isfile('./Tools/Miners/PhoenixMiner_5.9d_Windows\PhoenixMiner.exe') and os.path.isfile('./Tools/Miners/xmrig-6.16.1/xmrig.exe'):
    pass
else:
    print(f"{Fore.RED}Run Setup.py")
    input()

prefs = json.loads(open('./Tools/unmineableprefs.json', 'r').read())
try:
    prefs["miner"]
    useCurrentInfo(prefs)
except:
    pass

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
info = json.loads(open('./Tools/info.json').read())

PrintASCII()

gpuCPU = input(f"{Fore.CYAN}Would you like to CPU or GPU mine?\n\n{Fore.WHITE}1 - GPU\n2 - CPU\n\n{Fore.CYAN}Select > {Fore.WHITE}")
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if gpuCPU == "1":
    PrintASCII()
    minerSelect = input(f"{Fore.CYAN}Select Your Miner:\n\n{Fore.WHITE}1 - T-Rex (Nvidia)\n2 - PhoenixMiner (Nvidia & AMD)\n3 - Exit\n\n{Fore.CYAN}Select > {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
    
    PrintASCII()
    algo = input(f"{Fore.CYAN}Select Your Algorithm:\n\n{Fore.WHITE}1 - Ethash (6GB+ VRAM)\n2 - Etchash (3GB+ VRAM)\n3 - Exit\n\n{Fore.CYAN}Select > {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    if algo == "3":
        os.system('python ./Start.py')

    elif algo == "1":
        ethash = True

    elif algo == "2":
        ethash = False

    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Start.py')


    os.system('cls' if os.name in ('nt', 'dos') else 'clear')




elif gpuCPU == "2":
    PrintASCII()
    minerSelect = input(f"{Fore.CYAN}Select Your Miner:\n{Fore.WHITE}1 - XMRIG\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
coinSelect = input(f"{Fore.CYAN}Select the coin to mine:\n\n{Fore.WHITE}1 - PancakeSwap (CAKE)\n2 - SHIBA INU (SHIB)\n3 - Solana (SOL)\n4 - Cardano (ADA)\n5 - Cosmos (ATOM)\n6 - Bitcoin Cash (BCH)\n7 - Bitcoin Gold (BTG)\n8 - Dogecoin (DOGE)\n9 - Dash (DASH)\n10 - Sushi (SUSHI)\n11 - Zilliqa (ZIL)\n12 - Monero (XMR)\n13 - Ripple (XRP)\n14 - Litecoin (LTC)\n15 - Gas (GAS)\n16 - TetherUS (USDT)\n17 - NANO (NANO)\n18 - Dogelon (ELON)\n\n{Fore.CYAN}Select > {Fore.WHITE}")
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

coin = coinTranslate(coinSelect)

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

prefSave(minerSelect, ethash)

os.system('cls' if os.name in ('nt', 'dos') else 'clear')

if minerSelect == "trex":
    trexMine(coin, ethash)
elif minerSelect == "phoenixminer":
    phoenixMine(coin, ethash)
elif minerSelect == "xmrig":
    xmrigMine(coin)