import pikepdf
import os
from colorama import Fore
from pypdf import PdfReader, PdfWriter
import platform
import argparse
import random

name_system = platform.system()

startagain = True

def print_banner():
    if startagain:

        banner1 = r'''

██████╗ ██╗   ██╗    ██████╗ ██████╗ ███████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝ ╚████╔╝     ██████╔╝██║  ██║█████╗      ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝   ╚██╔╝      ██╔═══╝ ██║  ██║██╔══╝      ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║        ██║       ██║     ██████╔╝██║         ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝        ╚═╝       ╚═╝     ╚═════╝ ╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                    v1.8

                Developer : Bardia Ghassemi
                                                                                                                                                                                                                
        '''

        banner2 = r'''
 
 (        )   (    (      (             (                         )       (     
 )\ )  ( /(   )\ ) )\ )   )\ )     (    )\ )    (        (     ( /(       )\ )  
(()/(  )\()) (()/((()/(  (()/(     )\  (()/(    )\       )\    )\()) (   (()/(  
 /(_))((_)\   /(_))/(_))  /(_))  (((_)  /(_))((((_)(   (((_) |((_)\  )\   /(_)) 
(_)) __ ((_) (_)) (_))_  (_))_|  )\___ (_))   )\ _ )\  )\___ |_ ((_)((_) (_))   
| _ \\ \ / / | _ \ |   \ | |_   ((/ __|| _ \  (_)_\(_)((/ __|| |/ / | __|| _ \  
|  _/ \ V /  |  _/ | |) || __|   | (__ |   /   / _ \   | (__   ' <  | _| |   /  
|_|    |_|   |_|   |___/ |_|      \___||_|_\  /_/ \_\   \___| _|\_\ |___||_|_\  

                    v1.8

                Developer : Bardia Ghassemi

        '''
        list_banners = [banner1, banner2]
        banner = random.choice(list_banners)
        print(Fore.CYAN, banner, Fore.RESET, sep='')



def Faild():
    print(Fore.RED, f'\b[-] {passtry} Password Tesded, Password Not Found.\n', Fore.RESET)
    exit(0)

def main(PDF_File, Password_File):
    global startagain
    global passtry
    while True:
            if not Password_File:
                passwordliste = False
            else:
                passwordliste = True
                # check if Default password show a warning
                for _ in range(1, 16):
                    filepath = os.getcwd()
                    _ = filepath + r'\passlist' + str(_)
                    __ = 'passlist' + str(_)
                    if passwordlist == _ or passwordlist == __:
                        print(Fore.RED, '\b[!] What you entered is a default list password and will be tried during auto-crack. Please enter another name, or rename your PasswordList.', Fore.RESET)
                        continue
            
            if PDF_File[-4:] != '.pdf':
                print(Fore.RED + '[?!] Input PDF_File Not a PDF.' + Fore.RESET)
                startagain = False
                continue

            try:
                open(PDF_File)
            except FileNotFoundError:
                print(Fore.RED + '[?!] PDF_File NOT Found.' + Fore.RESET)
                startagain = False
                continue

            if passwordliste:
                try:
                    passwordlist = open(passwordlist)
                except FileNotFoundError:
                    print(Fore.RED + '[?!] Pass_File NOT Found.' + Fore.RESET)
                    startagain = False
                    continue


            def check_pass_need():
                try:
                    pikepdf.open(PDF_File)
                    print(Fore.RED, f"\b[!] The PDF File '{PDF_File}' Has No Password.", Fore.RESET)
                    exit(0)
                except pikepdf._core.PasswordError:
                    pass

            check_pass_need()

            def remove_password(password):
                reader = PdfReader(PDF_File)
                reader.decrypt(password)

                writer = PdfWriter()
                writer.append_pages_from_reader(reader)
                writer.encrypt("")

                with open(PDF_File, "wb") as out_file:
                    writer.write(out_file)
                
                print(Fore.GREEN, f"\b[+] Password of File '{PDF_File}' REMOVED Successfully.", Fore.RESET)

            passtry = 0
            if passwordliste:
                print(Fore.YELLOW, '\b[!] Testing Your Password List.\n', Fore.RESET)
                for password in passwordlist:
                    password = password.strip("\n")
                    if password == '' or password == '\n' or password == None:
                        continue
                    try:
                        pikepdf.open(PDF_File, password=password)
                        print(Fore.GREEN, f"\b\n[+] Password : {password}", Fore.RESET)
                        ASK = input("[?] Do You Want Remove PASSWORD (Y/n): ")
                        if ASK == '' or ASK == '\n' or ASK == None or ASK.lower() == 'y':
                            remove_password(password)
                        exit(0)
                    except pikepdf._core.PasswordError:
                        passtry += 1
                        print(Fore.RED, f"\b[*] {passtry:,} Password Tesded.", Fore.RESET, end=' \r', sep='')
                
                print(Fore.RED, '\b[-] Your PassList Faild.', Fore.RESET)

            for number_of_passlist in range(1, 16):
                number_of_passlist = str(number_of_passlist)
                print(Fore.YELLOW, f'\b\n[!] Testing PassList{number_of_passlist}.', Fore.RESET)

                passlistall = open(f'DefaultPassList/passlist{number_of_passlist}.txt')

                for password in passlistall:
                    password = password.strip("\n")
                    try:
                        pikepdf.open(PDF_File, password=password)
                        print(Fore.GREEN, f"\b\n[+] Password : {password}", Fore.RESET)
                        ASK = input("[?] Do You Want Remove PASSWORD (Y/n): ")
                        if ASK == '' or ASK == '\n' or ASK == None or ASK.lower() == 'y':
                            remove_password(password)
                        exit(0)
                    except pikepdf._core.PasswordError:
                        passtry += 1
                        print(Fore.RED, f"\b[*] {passtry:,} Password Tesded.", Fore.RESET, end='\r', sep='')

                print(Fore.RED, f'\b\n[-] The Default PassList{number_of_passlist} Faild.', Fore.RESET)

            Faild()

if __name__ == '__main__':
    try:
        # print Banner
        print_banner()

        p = argparse.ArgumentParser()
        
        p.description = "(.❛ ᴗ ❛.) PDF-Cracker Is A Tool For Break The Lock Of PDF Files And Find Passwords (.❛ ᴗ ❛.)"

        p.add_argument("-f", dest="PDF_File", help="PDF File For Start Cracking", required=True)
        p.add_argument("-p", dest="PASSWORD_FILE", help="Password File For Use it in Cracking, If You Has No Password File Not Use This Option")
        
        args = p.parse_args()

        file = args.PDF_File
        passfile = args.PASSWORD_FILE

        main(file, passfile)
    except KeyboardInterrupt:
        print(Fore.RED, '\b\n[-] Quitting PDF Cracker.....', Fore.RESET)
        exit(0)
