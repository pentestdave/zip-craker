import zipfile
import sys

from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, init

# Reset colorama
init(autoreset=True)

# Specify wordlists rockyou path
wordlist = sys.argv[2]

# Specify zip file path
zip_file = sys.argv[1]

# Store and init the zip file name into a variable
init_zip = zipfile.ZipFile(zip_file)

# Check if it's encrypted or not
enc_ask = input("Is the ZIP file encrypted? y/n: ")

def extract(wordlist=wordlist):

    if enc_ask.lower() == "y":
        # Get and print the length of the rockyou file
        word_len = len(list(open(wordlist, "rb")))
        print(f"Total passwords to test: {word_len}")

        with open(wordlist, "rb") as wordlist:
            for word in tqdm(wordlist, total=word_len, unit="word"):
                try:
                    init_zip.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    sleep(2)
                    print(f"{Fore.GREEN + Style.BRIGHT}[+] Password found: {word.decode().strip()}")
                    sys.exit()
        sleep(2)
        print(f"{Fore.MAGENTA + Style.BRIGHT}[*] Password not found in {wordlist}, try others!")

    elif enc_ask.lower() == "n":
        try:
            print(f"{Fore.MAGENTA + Style.BRIGHT}[*] Extracting....")
            sleep(1)
            init_zip.extractall()
            sleep(2)
            print(f"{Fore.GREEN + Style.BRIGHT}[+] File extracted!")
        except:
            print(f"{Fore.RED + Style.BRIGHT}[!] The specfied ZIP file is encrypted!")
    else:
        print(f"{Fore.MAGENTA + Style.BRIGHT}[*] Command not recognized. Enter \"y\" for YES or \"n\" for NO!")

# Call extract function
extract()