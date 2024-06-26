import os
import time

RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_RED = "\033[41m"
NEGRITO = '\033[1m'
CLARO = '\033[90m'

def logo_animada():
   
    logo = [
            NEGRITO, "              ", GREEN + "                       _____                   _             _ \n" +
            WHITE + "     /////|           " + GREEN + "|_   _|__ _ __ _ __ ___ (_)_ __   __ _| |\n" +
            WHITE + "    ///// |    (\       " + GREEN + "| |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |\n" +
            WHITE + "   |~~~|  |    \ \      " + GREEN + "| |  __/ |  | | | | | | | | | | (_| | |\n" +
            WHITE + "   |===|  |     \ \     " + GREEN + "|_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\n" +
            WHITE + "   |T  |  |     / '|   " + MAGENTA + "         _____     ____   ___  _     ___    _____\n" +
            WHITE + "   | D |  |     \ '/  " + MAGENTA + "         |_   _|__ |  _ \ / _ \| |   |_ _|__|_   _|\n" +
            WHITE + "   |  L| /        \      " + MAGENTA + "        | |/ _ \| | | | | | | |    | |/ __|| |  \n" +
            WHITE + "   |===|/         ==).   " + MAGENTA + "        | | (_) | |_| | |_| | |___ | |\__ \| | \n" +
            WHITE + "   '---'         (__)   " + MAGENTA + "         |_|\___/|____/ \___/|_____|___|___/|_| 1.1.1\n" + RESET
    ]
    
    num_loops = 1
        
    for _ in range(num_loops):
     for quadro in logo:
         clear_terminal()  
         lines = quadro.split('\n')
         for line in lines:
              print(line)
              time.sleep(0.05)  
            
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')  # Sistemas Linux


def refresh():
    palavra = 'refresh'
    for loop in range(0, 3):
        palavra = palavra + '.'
        print(palavra)
        time.sleep(0.2)
    time.sleep(1)
