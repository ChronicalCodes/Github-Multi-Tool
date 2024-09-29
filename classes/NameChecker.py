import requests 
import random 
import colorama
from colorama import Fore
import os
import time


class NameChecker:

    def __init__(self):
        pass
    
    def main(self):
        os.system("cls") # Clears screen
        print(Fore.GREEN + "Loading" + Fore.RESET)
        taken = 0
        untaken = 0
        url_handler = "https://github.com/"
        mylist = []

        with open("./Database/loaded_names.txt", "r") as f: # Loads up the txt
            for line in f:
                mylist.append(line.strip()) # Appends lines from txt to file excluding \n
        os.system("cls")
        for i in mylist:
            time.sleep(1) # Attempts to stop githubs ratelimiting
            
            r = requests.get(url_handler + i) # Gets request of the github.com + the name
            if r.status_code == 200: # Checks if active
                print(f"{Fore.RED}{i} - Taken{Fore.RESET}")
                taken += 1 # Adds 1 to taken variable
            else:
                print(f"{Fore.GREEN}{i} - Available{Fore.RESET}")
                f = open("./Database/checkednames_valid.txt", "a") # Opens txt
                f.write(i + "\n") # Writes the name
                f.close()
                untaken += 1 # Adds 1 to untaken variable
            
        
        print(f"\n{Fore.RED}Taken: {taken}{Fore.RESET} | {Fore.GREEN}Untaken: {untaken}{Fore.RESET}")
        input("Press enter to exit")
        