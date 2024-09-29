import requests 
import random 
import colorama
from colorama import Fore
import os
import time

class SingleNameChecker:
    
    def __init__(self):
        pass

    def main(self):
        os.system("cls")
        url_handler = "https://github.com/"
        name = input("What name would you like to check > ")
        
        r = requests.get(url_handler + name)
        if r.status_code == 200:
            print(f"{Fore.RED}Name taken{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}Name available{Fore.RESET}")
        
        input("Press enter to exit")

