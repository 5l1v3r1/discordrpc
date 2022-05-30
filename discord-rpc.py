import time, struct, os, colorama
from pypresence import *

class DiscordRPC:
    """ Discord Rich Presence Controller """

    def __init__(RPC):
        clientid = input(f'[?] Applications Client ID: ')
        rpcstatus = input(f'[?] Applications Status: ')
        rpcdetails = input(f'[?] Applications Details: ')
        refreshtime = input(f'[?] Applications Refresh Time: ')

        largeiconname = input(f'[?] Applications Large Icons Name: ')
        largeicontext = input(f'[?] Large Icons Text: ')
        smalliconname = input(f'[?] Applications Small Icons Name: ')
        smallicontext = input(f'[?] Small Icons Text: ')

        button1text = input(f'[?] 1st Buttons Name: ')
        button1link = input(f'[?] 1st Buttons Link: ')
        button2text = input(f'[?] 2nd Buttons Name: ')
        button2link = input(f'[?] 2nd Buttons Link: ')

    def Menu(RPC):
        os.system('cls')
        print(f"""
        ██████╗ ██╗ ██████╗ █████╗  █████╗ ██████╗ ██████╗       ██████╗ ██████╗  █████╗
        ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗██╔══██╗
        ██║  ██║██║╚█████╗ ██║  ╚═╝██║  ██║██████╔╝██║  ██║█████╗██████╔╝██████╔╝██║  ╚═╝
        ██║  ██║██║ ╚═══██╗██║  ██╗██║  ██║██╔══██╗██║  ██║╚════╝██╔══██╗██╔═══╝ ██║  ██╗
        ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║  ██║██████╔╝      ██║  ██║██║     ╚█████╔╝
        ╚═════╝ ╚═╝╚═════╝  ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═════╝       ╚═╝  ╚═╝╚═╝      ╚════╝ 
        """)

    def Start(RPC):
        RPC.Menu()
        RPC = Presence(RPC.clientid)
        RPC.connect()
        starttime = int(time.time())

        try:
            print(f'[/] Discord-RPC Started Successfully...')
            while True:
                RPC.update(
                    state = RPC.rpcdetails,
                    details = RPC.rpcstatus,
                    large_image = RPC.largeiconname,
                    large_text = RPC.largeicontext,
                    small_image = RPC.smalliconname,
                    small_text = RPC.smallicontext,
                    start = starttime,
                    buttons = [
                        {"label": RPC.button1text, "url": RPC.button1link},
                        {"label": RPC.button2text, "url": RPC.button2link}
                    ]
                )
                time.sleep(int(refreshtime))
        except pypresence.exceptions.InvalidPipe:
            print(f"\n[!] Make sure Discord is Running!")
        except pypresence.exceptions.ServerError:
            print(f"\n[!] Please make sure you entered the correct Values!")

RPC = DiscordRPC()
RPC.Start()
