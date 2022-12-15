try:
    import pyfiglet
    from rich.console import Console
    from rich.console import RenderGroup
    from rich.panel import Panel
    from rich.prompt import IntPrompt
    from rich.progress import Progress,track
    from tqdm import tqdm
    from os import walk
    from os import system
    from time import sleep
    from random import randint
    import ctypes
    import time
    import sys
    import os
    import json
    import requests
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system('pip install pyfiglet')
    os.system('pip install rich')
    os.system('pip install tqdm')
    os.system('pip install os')
    os.system('pip install sys')
    os.system('pip install time')
    os.system('pip install random')
    os.system('pip install ctypes')
    os.system('pip install json')
    os.system('pip install requests')
    os.system('pip install colorama')

with open('teks.json', 'r') as data_file:
    json_data = data_file.read()

teks = json.loads(json_data)

ctypes.windll.kernel32.SetConsoleTitleW("ASR Tools")
os.system('cls')
con = Console()

def one():
    os.system('cls')
    print(" ")
    result = pyfiglet.figlet_format("=WEBSITE=", font = "banner4")
    con.print(result,style="bold blue")
    con.print("Always be wise and responsible when using this tool. Be careful when using it because... click to see more", style="bold blue")
    tasks = ['Trying to slip XSS','Trying inject an SQL Injection','Injecting some Malware','Injecting air Kali','Buying the Domain and Paying to ####Mart']
    
    stuff = RenderGroup(
        Panel("1 | Deface"),
        Panel("2 | DDOS"),
        Panel("3 | Back to Menu"),
    )
    con.print(Panel(stuff),style="bold blue")
    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3'])
    os.system('cls')
    if answer == 1:
        result = pyfiglet.figlet_format("=DEFACER=", font = "banner4")
        con.print(result,style="bold blue")
        turl = input("Please enter URL target: ")
        con.print("Downloading & Rendering", turl, style="bold green")
        for i in tqdm(range(100)):
            sleep(0.1)
        con.print("Scanning for Vulnerability in", turl, style="bold green")
        for i in tqdm(range(100)):
            sleep(0.3)
        con.print("Performing pentesting on the target", style="bold green")
        with con.status("[bold green]Working on...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(randint(5,10))
                con.log(f"{task} complete", style="bold green")
        con.print("Login into cPanel...")
        sleep(randint(5,8))
        con.print("Failed login to cPanel!", style="bold red")
        sleep(5)
        con.print("Start Bruteforcing the login page...")
        sleep(randint(5,10))
        con.print("Login into cPanel Success!", style="bold green")
        input("Are you sure you want to deface this website?  [Y/N] : ")
        filed = input("Select the html/xml/php file that you want to upload to the website : ")
        con.print("Uploading", filed,"into cPanel", style="bold green")
        for i in tqdm(range(100)):
            sleep(0.1)
        #disable()
        input("Success! [Press Any Key to Back]")
        menu()
        sleep(10)
    if answer == 2:
        result = pyfiglet.figlet_format("=DDOS=", font = "banner4")
        con.print(result,style="bold blue")
        turl = input("Please enter IP/Domain/Server target: ")
        os.system('cls')
        os.system('ping ' + turl + ' -n 25')
        sleep(10)
        input("Success! [Press Any Key to Back]")
        menu()
    else :
        menu()

def two():
    os.system('cls')
    print(" ")
    result = pyfiglet.figlet_format("=TROLLER=", font = "banner4")
    con.print(result,style="bold blue")
    con.print("Always be wise and responsible when using this tool. Be careful when using it because... click to see more", style="bold blue")
    
    stuff = RenderGroup(
        Panel("1 | NGL Troller"),
        Panel("2 | Back to Menu"),
    )
    con.print(Panel(stuff),style="bold blue")
    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3'])
    if answer == 1:
        os.system("cls")
        r = requests.Session()
        result = pyfiglet.figlet_format("=NGL.LINK=", font = "banner4")
        con.print(result,style="bold cyan")
        print(f"{Fore.LIGHTCYAN_EX}NGL.LINK Spammer!")
        # Target is the username not the full link, I made it easier for people to use! 
        target = input(f"Enter Target: ")
        texs = input(f"Enter text here, input `random` if wanna sent Random Text: ")
        start = input(f"Are you Ready? Y/N: ").upper()
        def spam():
            questions_count = 0
            url = f"https://ngl.link/{target}"
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
            }
            while True:
                if texs == "random":
                    payload = {
                        "question": str(teks[randint(1,104)])
                    }
                else :
                    payload = {
                        "question": str(texs) + " - " + str(randint(1,1000))
                    }
                spam = r.post(url, headers=headers, data=payload)
                questions_count += 1
                print(f"{questions_count} Questions Sent to: {target} with {payload}")
                sleep(randint(1,3))
            input("Success! [Press Any Key to Back]")
            menu()
        if start == "Y":
            spam()
        else:
            print("Invalid Response")
            menu()
    else :
        menu()
def enable():
    os.system('netsh interface set interface "Wi-Fi" enabled')
def disable():
    os.system('netsh interface set interface "Wi-Fi" disabled')

def menu():
    print(" ")
    banner = pyfiglet.figlet_format("ASRSX_",font="starwars")
    # then printing that out with rich console and a little intro
    con.print(banner,style="bold green")
    con.print("Its Art but it doesn't explode and it can be seen but it can't be touched.",style="bold green")
    con.print("Dont forget like, subscribe/follow, and share :)", style="bold green")


    stuff = RenderGroup(
        Panel("1 | Website Hacking"),
        Panel("2 | Troll Tools"),
    )
    con.print(Panel(stuff),style="bold green")
    answer = IntPrompt.ask("Which one do you pick? ",choices=['1','2','3'])
    os.system('cls')
    if answer == 1:
        one()
    if answer == 2:
        two()
    if answer == 3:
        tasks = ['tes','tesss']

        with con.status("[bold green]Working on...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(randint(1,5))
                con.log(f"{task} complete", style="bold green")
        #disable()
        sleep(10)
    if answer == 4:
        enable()
        sleep(10)


menu()
