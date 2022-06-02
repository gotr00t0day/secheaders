import argparse
import requests
from colorama import Fore

requests.packages.urllib3.disable_warnings()

banner = """"

███████ ███████  ██████     ██   ██ ███████  █████  ██████  ███████ ██████  ███████ 
██      ██      ██          ██   ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      
███████ █████   ██          ███████ █████   ███████ ██   ██ █████   ██████  ███████ 
     ██ ██      ██          ██   ██ ██      ██   ██ ██   ██ ██      ██   ██      ██ 
███████ ███████  ██████     ██   ██ ███████ ██   ██ ██████  ███████ ██   ██ ███████ 

Author: c0d3ninja
Version: 1.0


"""

print(f"{Fore.CYAN} {banner}")

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('-hs', '--headers', action='store', nargs='+',
                   help="add multiple headers",
                   metavar="headers")

parser.add_argument('-t', '--target',
                    type=str, help='scan for security headers',
                    metavar='domain.com')

args = parser.parse_args()

if args.target:
    if args.headers:
        security_headers = args.headers
        session = requests.Session()
        no_sec = []
        found_hd = []
        no_dup = []
        no_dup_found = []
        lower = [x.lower() for x in security_headers]
        capital = [x.upper() for x in security_headers]
        resp = session.get(f"{args.target}", verify=False)
        print(f"{Fore.CYAN}Domain: {Fore.GREEN}{args.target}\n")
        for item, key in resp.headers.items():
            for sec_headers in security_headers:
                if sec_headers == item or lower == item or capital == item:
                    found_hd.append(sec_headers)
                    [no_dup_found.append(x) for x in found_hd if x not in no_dup_found]
            print(f"{Fore.CYAN}{item}: {Fore.YELLOW}{key}")
        no_dup = ", ".join(no_dup)
        print("\n")
        print(f"{Fore.GREEN} Found Security Headers: {Fore.YELLOW} {len(no_dup_found)}\n")
        no_dup_found = ", ".join(no_dup_found)
        print(f"{Fore.YELLOW} {no_dup_found}\n")
        no_headers = [
        item for item in security_headers if item not in no_dup_found]
        print(f"{Fore.RED} Found Missing headers: {Fore.YELLOW} {len(no_headers)}\n")
        no_headers = ", ".join(no_headers)
        print(f"{Fore.YELLOW} {no_headers}")
