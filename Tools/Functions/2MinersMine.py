import os
import json
import sys
from colorama import Fore, init
import webbrowser

init()
sys.path.append("./Tools")
from CommonFunctions import PrintASCII

def getWallet(coin):
    info = json.loads(open('./Tools/2minerswallet.json', 'r').read())
    try:
        wallet = info[f'{coin}' + '_wallet']
        worker = info[f'{coin}' + '_worker']
        return wallet, worker
    except:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print(f"{Fore.RED}Wallet for this coin has not been set")
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def monitor(coin, wallet):
    coin = coin.lower()
    webbrowser.open_new(f'https://{coin}.2miners.com/account/{wallet}')

def mineXMR():
    wallet, worker = getWallet("XMR")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - XMRig\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\xmrig-6.16.1\xmrig.exe --coin=XMR -o xmr.2miners.com:2222 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("XMR", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineERG():
    wallet, worker = getWallet("ERG")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - T-Rex\n2 - lolMiner\n3 - TeamRedMiner\n4 - NBMiner\n5 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\t-rex.exe -a autolykos2 -o stratum+tcp://erg.2miners.com:8888 -u {wallet}.{worker} -w {worker} -p x")
            os.system(r"pause")
            monitor("ERG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo AUTOLYKOS2 --pool erg.2miners.com:8888 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("ERG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        try:
            os.system(fr"Tools\teamredminer-v0.8.6.3-win\teamredminer.exe -a autolykos2 -o stratum+tcp://erg.2miners.com:8888 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("ERG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "4":
        try:
            os.system(fr"Toolsnbminer.exe -a ergo -o stratum+tcp://erg.2miners.com:8888 -u {wallet}.{worker}")
            os.system(r"pause")
            monitor("ERG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "5":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineFLUX():
    wallet, worker = getWallet("FLUX")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo EQUI144_5 --pers BgoldPoW --pool btg.2miners.com:4040 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("FLUX", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')


def mineBTG():
    wallet, worker = getWallet("BTG")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - BMiner\n3 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo EQUI144_5 --pers BgoldPoW --pool btg.2miners.com:4040 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("BTG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\miner.exe --algo 144_5 --pers BgoldPoW --server btg.2miners.com --port 4040 --user {wallet}.{worker} --pass x")
            os.system(r"pause")
            monitor("BTG", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineCTXC():
    wallet, worker = getWallet("CTXC")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --coin CTXC --pool ctxc.2miners.com:2222 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("CTXC", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineFIRO():
    wallet, worker = getWallet("FIRO")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - T-Rex\n2 - TeamRedMiner\n3 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"t-rex.exe -a firopow -o stratum+tcp://firo.2miners.com:8181 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("FIRO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\teamredminer-v0.8.6.3-win\teamredminer.exe -a firopow -o stratum+tcp://firo.2miners.com:8181 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("FIRO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineBEAM():
    wallet, worker = getWallet("BEAM")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - BMiner\n3 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --coin BEAM --pool beam.2miners.com:5252 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("BEAM", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\miner.exe --algo beamhash --server beam.2miners.com --port 5252 --ssl 1 --user {wallet}.{worker} --pass x")
            os.system(r"pause")
            monitor("BEAM", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineGRIN():
    wallet, worker = getWallet("GRIN")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - BMiner\n3 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --coin GRIN-C32 --pool grin.2miners.com:3030 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("GRIN", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\miner.exe --algo grin32 --server grin.2miners.com --port 3030 --user {wallet}.{worker} --pass x")
            os.system(r"pause")
            monitor("GRIN", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineCLO():
    wallet, worker = getWallet("CLO")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - T-Rex\n2 - lolMiner\n3 - BMiner\n4 - TeamRedMiner\n5 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\t-rex.exe -a autolykos2 -o stratum+tcp://erg.2miners.com:8888 -u {wallet}.{worker} -w {worker} -p x")
            os.system(r"pause")
            monitor("CLO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo ETHASH --pool clo.2miners.com:3030 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("CLO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        try:
            os.system(fr"Tools\Miners\miner.exe --algo beamhash --server beam.2miners.com --port 5252 --ssl 1 --user {wallet}.{worker} --pass x")
            os.system(r"pause")
            monitor("CLO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "4":
        try:
            os.system(fr"Tools\teamredminer-v0.8.6.3-win\teamredminer.exe -a firopow -o stratum+tcp://firo.2miners.com:8181 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("CLO", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "5":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')


def mineAE():
    wallet, worker = getWallet("AE")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo C29AE --pool ae.2miners.com:4040 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("AE", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineETP():
    wallet, worker = getWallet("ETP")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - T-Rex\n2 - lolMiner\n3 - BMiner\n4 - TeamRedMiner\n5 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\t-rex.exe -a ethash -o stratum+tcp://etp.2miners.com:9292 -u {wallet}.{worker} -w {worker} -p x")
            os.system(r"pause")
            monitor("ETP", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo ETHASH --pool etp.2miners.com:9292 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("ETP", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        try:
            os.system(fr"Tools\Miners\miner.exe -uri ethproxy://{wallet}.{worker}@etp.2miners.com:9292")
            os.system(r"pause")
            monitor("ETP", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "4":
        try:
            os.system(fr"Tools\teamredminer-v0.8.6.3-win\teamredminer.exe -a ethash -o stratum+tcp://etp.2miners.com:9292 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("ETP", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "5":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

def mineMWC():
    wallet, worker = getWallet("MWC")
    miner = input(f"{Fore.CYAN}Which miner would you like to use?\n{Fore.WHITE}1 - lolMiner\n2 - BMiner\n3 - TeamRedMiner\n4 - Exit\n{Fore.CYAN}Select > {Fore.WHITE}")
    if miner == "1":
        try:
            os.system(fr"Tools\Miners\1.38\lolMiner.exe --algo ETHASH --pool etp.2miners.com:9292 --user {wallet}.{worker}")
            os.system(r"pause")
            monitor("MWC", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "2":
        try:
            os.system(fr"Tools\Miners\miner.exe -uri ethproxy://{wallet}.{worker}@etp.2miners.com:9292")
            os.system(r"pause")
            monitor("MWC", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "3":
        try:
            os.system(fr"Tools\teamredminer-v0.8.6.3-win\teamredminer.exe -a ethash -o stratum+tcp://etp.2miners.com:9292 -u {wallet}.{worker} -p x")
            os.system(r"pause")
            monitor("MWC", wallet)
        except:
            os.system('python ./Tools/Functions/2MinersMenu.py')
    elif miner == "4":
        os.system('python ./Tools/Functions/2MinersMenu.py')
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Tools/Functions/2MinersMenu.py')

PrintASCII()
option = input(f"{Fore.CYAN}What coin would you like to mine?{Fore.WHITE}\n\n1 - Monero (XMR)\n2 - Ergo (ERG)\n3 - Flux (FLUX)\n4 - Bitcoin Gold (BTG)\n5 - Cortex (CTXC)\n6 - Firo (FIRO)\n7 - Beam (BEAM)\n8 - GRIN (GRIN)\n9 - Callisto (CLO)\n10 - Aeternity (AE)\n11 - Metaverse (ETP)\n12 - MimbleWimbleCoin (MWC)\n13 - Exit\n\n{Fore.CYAN}Select > {Fore.WHITE}")

if option == "1":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineXMR()

elif option == "2":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineERG()

elif option == "3":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineFLUX()

elif option == "4":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineBTG()

elif option == "5":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineCTXC()

elif option == "6":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineFIRO()

elif option == "7":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineBEAM()

elif option == "8":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineGRIN()

elif option == "9":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineCLO()

elif option == "10":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineAE()

elif option == "11":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineETP()

elif option == "12":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    mineMWC()

elif option == "13":
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    os.system('python ./Tools/Functions/2MinersMenu.py')

else:
    print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
    input("\n\nPress Enter to Continue...")
    os.system('python ./Tools/Functions/2MinersMenu.py.py')