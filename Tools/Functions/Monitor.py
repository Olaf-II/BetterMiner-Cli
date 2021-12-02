import os
import json
import webbrowser
from colorama import Fore, Back
import sys
sys.path.append("./Tools")
from CommonFunctions import coinTranslate, PrintASCII

PrintASCII()

coinSelect = input(f"{Fore.CYAN}Select the coin to check/cashout:\n{Fore.WHITE}1 - PancakeSwap (CAKE)\n2 - SHIBA INU (SHIB)\n3 - Solana (SOL)\n4 - Cardano (ADA)\n5 - Cosmos (ATOM)\n6 - Bitcoin Cash (BCH)\n7 - Bitcoin Gold (BTG)\n8 - Dogecoin (DOGE)\n9 - Dash (DASH)\n10 - Sushi (SUSHI)\n11 - Zilliqa (ZIL)\n12 - Monero (XMR)\n13 - Ripple (XRP)\n14 - Litecoin (LTC)\n15 - Gas (GAS)\n16 - TetherUS (USDT)\n17 - NANO (NANO)\n{Fore.CYAN}Select > {Fore.WHITE}")

coin = coinTranslate(coinSelect)

try:
    info = json.loads(open('./Tools/info.json', 'r').read())
    addr = info[coin + '_wallet']
    webbrowser.open_new_tab(f'unmineable.com/coins/{coin}/address/{addr}')
    os.system('python ./Start.py')
except:
    print(f"{Fore.RED}Wallet for this coin has not been set")
    input(f"{Fore.LIGHTBLACK_EX}\n\nPress Enter to Continue...")
    os.system('python ./Start.py')