from colorama import Fore
import os

def coinTranslate(coinSelect):
    if coinSelect == "1":
        return "CAKE"
            
    elif coinSelect == "2":
        return "SHIB"

    elif coinSelect == "3":
        return "SOL"

    elif coinSelect == "4":
        return "ADA"

    elif coinSelect == "5":
        return "ATOM"

    elif coinSelect == "6":
        return "BCH"

    elif coinSelect == "7":
        return "BTG"

    elif coinSelect == "8":
        return "DOGE"

    elif coinSelect == "9":
        return "DASH"

    elif coinSelect == "10":
        return "SUSHI"

    elif coinSelect == "11":
        return "ZIL"

    elif coinSelect == "12":
        return "XMR"

    elif coinSelect == "13":
        return "XRP"
        
    elif coinSelect == "14":
        return "LTC"
        
    elif coinSelect == "15":
        return "GAS"
        
    elif coinSelect == "16":
        return "USDT"

    elif coinSelect == "17":
        return "NANO"
    
    elif coinSelect == "18":
        return "ELON"
    
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

#addWalletRigID(input(f"{Fore.CYAN}What coin would you like to set up?{Fore.WHITE}\n1 - Monero (XMR)\n2 - Ergo (ERG)\n3 - Flux (FLUX)\n4 - Bitcoin Gold (BTG)\n5 - Cortex (CTXC)\n6 - Firo (FIRO)\n7 - Beam (BEAM)\n8 - GRIN (GRIN)\n9 - Callisto (CLO)\n10 - Aeternity (AE)\n11 - Metaverse (ETP)\n12 - MimbleWimbleCoin (MWC)\n{Fore.CYAN}Select > {Fore.WHITE}"))

def coinTranslate2Miners(coinSelect):
    if coinSelect == "1":
        return "XMR"
            
    elif coinSelect == "2":
        return "ERG"

    elif coinSelect == "3":
        return "FLUX"

    elif coinSelect == "4":
        return "BTG"

    elif coinSelect == "5":
        return "CTXC"

    elif coinSelect == "6":
        return "FIRO"

    elif coinSelect == "7":
        return "BEAM"

    elif coinSelect == "8":
        return "GRIN"

    elif coinSelect == "9":
        return "CLO"

    elif coinSelect == "10":
        return "AE"
        
    elif coinSelect == "11":
        return "ETP"
        
    elif coinSelect == "12":
        return "MWC"
    
    else:
        print(Fore.LIGHTRED_EX + "Invalid Option" + Fore.LIGHTBLACK_EX)
        input("\n\nPress Enter to Continue...")
        os.system('python ./Start.py')

def PrintASCII():
    print(Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner1.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli1.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner2.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli2.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner3.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli3.txt').read() + "\n" + Fore.LIGHTYELLOW_EX + open('./Tools/Text/BetterMiner4.txt').read() + Fore.LIGHTCYAN_EX + open('./Tools/Text/Cli4.txt').read() + "\n\n")