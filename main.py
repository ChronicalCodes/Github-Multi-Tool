# Github MultiTool
# Load names to check into "loaded_names.txt"

import requests
import colorama 
from colorama import Fore
import random
import os
from classes.NameGenerator import NameGenerator
from classes.NameChecker import NameChecker                        # Imports classes from other folder/files
from classes.SingleNameChecker import SingleNameChecker



class Startup:
    
    def __init__(self): # Initialization
        pass
    
    def main(self):
        os.system("cls") # Clears screen
        print(f"""

{Fore.MAGENTA}
  ____ _ _   _           _       __  __       _ _   _     _____           _ 
 / ___(_) |_| |__  _   _| |__   |  \/  |_   _| | |_(_)   |_   _|__   ___ | |
| |  _| | __| '_ \| | | | '_ \  | |\/| | | | | | __| |_____| |/ _ \ / _ \| |
| |_| | | |_| | | | |_| | |_) | | |  | | |_| | | |_| |_____| | (_) | (_) | |
 \____|_|\__|_| |_|\__,_|_.__/  |_|  |_|\__,_|_|\__|_|     |_|\___/ \___/|_| {Fore.RESET}

                                    {Fore.BLUE}Created by ChronicalCodes{Fore.RESET}

   {Fore.BLUE}           [1] Name Checker 
              [2] Single Name Checker
              [3] Name Generator
              [4] Exit{Fore.RESET}

""")
        
        choice = input(f"{Fore.GREEN}Select your choice > {Fore.RESET}") # Input for choice

        if choice == "1":
            nc = NameChecker()
            nc.main() # Initializes main in NameChecker
        if choice == "2":
            snc = SingleNameChecker()
            snc.main() # Initializes main in SingleNameChecker 
        if choice == "3":
            ng = NameGenerator()
            ng.main() # Initializes main in NameGenerator
        if choice == "4":
            print("Thanks for using Github Multi-Tool")
        else:
            self.main() # Initializes main in Startup incase of wrong input

s = Startup()
s.main()