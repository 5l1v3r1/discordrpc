import time, pypresence, struct, os, colorama

from pypresence import *
from colorama import Fore

def startup():
    os.system('cls')
    
    print(f"""
    {Fore.BLUE}██████╗ ██╗ ██████╗ █████╗  █████╗ ██████╗ ██████╗       ██████╗ ██████╗  █████╗
    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗██╔══██╗{Fore.CYAN}
    ██║  ██║██║╚█████╗ ██║  ╚═╝██║  ██║██████╔╝██║  ██║█████╗██████╔╝██████╔╝██║  ╚═╝
    ██║  ██║██║ ╚═══██╗██║  ██╗██║  ██║██╔══██╗██║  ██║╚════╝██╔══██╗██╔═══╝ ██║  ██╗{Fore.RESET}
    ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║  ██║██████╔╝      ██║  ██║██║     ╚█████╔╝
    ╚═════╝ ╚═╝╚═════╝  ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝       ╚═╝  ╚═╝╚═╝      ╚════╝ 
    """)

#inputs with colorama due to cmd not supporting it with standard input
clientidinput = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Client ID: '
rpcstatusinput = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Status: '
rpcdetailsinput = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Details: '
refreshtimeinput = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Refresh Time: '

largeiconname_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Large Icons Name: '
largeicontext_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your Large Icons Text: '
smalliconname_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your applications Small Icons Name: '
smallicontext_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your Small Icons Text: '

button1text_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your 1st Buttons Name: '
button1link_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your 1st Buttons Link: '
button2text_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your 2nd Buttons Name: '
button2link_input = f'[{Fore.BLUE}+{Fore.RESET}] Please enter your 2nd Buttons Link: '

startup()

#get user information
clientID = input(f'{clientidinput}')
print(' ')
rpcstatus = input(f'{rpcstatusinput}')
print(' ')
rpcdetails = input(f'{rpcdetailsinput}')
print(' ')
refreshtime = input(f'{refreshtimeinput}')
print(' ')
largeiconname = input(f'{largeiconname_input}')
print(' ')
largeicontext = input(f'{largeicontext_input}')
print(' ')
smalliconname = input(f'{smalliconname_input}')
print(' ')
smallicontext = input(f'{smallicontext_input}')
print(' ')
button1text = input(f'{button1text_input}')
print(' ')
button1link = input(f'{button1link_input}')
print(' ')
button2text = input(f'{button2text_input}')
print(' ')
button2link = input(f'{button2link_input}')
print(' ')

startup()

print(f'[{Fore.BLUE}+{Fore.RESET}] Discord-RPC Started Successfully...')

#setup rpc connection to discord client
RPC = Presence(clientID)
RPC.connect()
starttime = int(time.time())

try:
    while True:
        #set vars for discord
        RPC.update(
            state = rpcdetails,
            details = rpcstatus,
            large_image = largeiconname,
            large_text = largeicontext,
            small_image = smalliconname,
            small_text = smallicontext,
            start = starttime,
            buttons = [{"label": button1text, "url": button1link}, {"label": button2text, "url": button2link}]
        )
        #refresh with our variable
        time.sleep(int(refreshtime))

#error diagnosis / print errors
except pypresence.exceptions.InvalidPipe as error1:
    print(f"\n[{Fore.RED}!{Fore.RESET}] Make sure Discord is Running!")
except pypresence.exceptions.InvalidID  as error2:
    print(f"\n[{Fore.RED}!{Fore.RESET}] Invalid Client ID!")
except struct.error as error3:
    print(f"\n[{Fore.RED}!{Fore.RESET}] Invalid Client ID!")
except pypresence.exceptions.ServerError as error4:
    print(f"\n[{Fore.RED}!{Fore.RESET}] Please make sure you entered the correct Link/Name/ID.")
