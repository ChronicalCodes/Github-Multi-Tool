import requests
import colorama 
from colorama import Fore
import random
import os
import time


class NameGenerator:

    def __init__(self):
        pass

    def main(self):
        os.system("cls") # Clears the screen
        taken = 0
        untaken = 0
        url_handler = "https://github.com/"
        no_of_names = int(input("How many names would you like to generate > "))
        no_of_chars = int(input("How many chars do you want in your name > "))

        for i in range(no_of_names):
            mylist = []
            all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9']
            
            for i in range(no_of_chars): # Does for loop for how many names user wants generated
                random_num = random.randint(0,60) # Gets random number between 0-60
                random_char = all_chars[random_num] # Gets that random numbers place in the list
                mylist.append(random_char) # Adds that random char to the list
            name = "".join(mylist) # Joins the list together
            time.sleep(1) # Attempts to stop github ratelimiting
            r = requests.get(url_handler + name) # Opens up github.com + name
            if r.status_code == 200: # Checks if name is active
                print(f"{Fore.RED}{name} is taken{Fore.RESET}")
                taken += 1 # Adds 1 to taken variable
            
            else:
                print(f"{Fore.GREEN}{name} is untaken - Added to generatednames_untaken.txt!{Fore.RESET}")
                f = open("./Database/generatednames_untaken.txt", "a") # Opens up txt
                f.write(name + "\n") # Writes the name and a new line
                f.close()
                untaken += 1 # Adds 1 to untaken variable
        
        print(f"\n{Fore.RED}Taken: {taken}{Fore.RESET} | {Fore.GREEN}Untaken: {untaken}{Fore.RESET}")
        input("Press enter to return to exit")
       
       
        