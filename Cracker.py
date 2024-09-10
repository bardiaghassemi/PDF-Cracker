import pikepdf
import os
from colorama import Fore
from pypdf import PdfReader, PdfWriter

startagain = True

def print_banner():
    if startagain:
        os.system('cls')

        banner = r'''
    _______   _______   ________         ______   _______    ______    ______   __    __  ________  _______  
    |       \ |       \ |        \       /      \ |       \  /      \  /      \ |  \  /  \|        \|       \ 
    | $$$$$$$\| $$$$$$$\| $$$$$$$$      |  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$$| $$$$$$$\
    | $$__/ $$| $$  | $$| $$__          | $$   \$$| $$__| $$| $$__| $$| $$   \$$| $$/  $$ | $$__    | $$__| $$
    | $$    $$| $$  | $$| $$  \         | $$      | $$    $$| $$    $$| $$      | $$  $$  | $$  \   | $$    $$
    | $$$$$$$ | $$  | $$| $$$$$         | $$   __ | $$$$$$$\| $$$$$$$$| $$   __ | $$$$$\  | $$$$$   | $$$$$$$\
    | $$      | $$__/ $$| $$            | $$__/  \| $$  | $$| $$  | $$| $$__/  \| $$ \$$\ | $$_____ | $$  | $$
    | $$      | $$    $$| $$             \$$    $$| $$  | $$| $$  | $$ \$$    $$| $$  \$$\| $$     \| $$  | $$
    \$$       \$$$$$$$  \$$               \$$$$$$  \$$   \$$ \$$   \$$  \$$$$$$  \$$   \$$ \$$$$$$$$ \$$   \$$

                    v1.3         

                Developer : Bardia Ghassemi
                                                                                                                                                                                                                            
        '''

        print(Fore.CYAN, banner, Fore.RESET, sep='')

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

def Faild():
    print(Fore.RED, f'\b[-] {passtry} Password Tesded, Password Not Found.\n', Fore.RESET)
    show_cursor()
    exit(0)

def main():
    global startagain
    global passtry
    while True:
        try:
            # print Banner
            print_banner()

            # start Cracking!!!
            pdf_file = input('[?] Enter PDF_Name With Format: ')
            passwordlist = input('[?] Enter PassFile With Format: ')

            if passwordlist == '' or passwordlist == None or passwordlist == '\n':
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
                try:
                    passwordlist = open(passwordlist)
                except FileNotFoundError:
                    print(Fore.RED + '[?!] Pass_File NOT Found.' + Fore.RESET)
                    startagain = False
                    continue
            
            if pdf_file[-4:] != '.pdf':
                print(Fore.RED + '[?!] Input PDF_File Not a PDF.' + Fore.RESET)
                startagain = False
                continue

            try:
                open(pdf_file)
            except FileNotFoundError:
                print(Fore.RED + '[?!] PDf_File NOT Found.' + Fore.RESET)
                startagain = False
                continue

            hide_cursor()

            def check_pass_need():
                try:
                    pikepdf.open(pdf_file)
                    print(Fore.RED, f"\b[!] The PDF File '{pdf_file}' has No Password.", Fore.RESET)
                    show_cursor()
                    exit(0)
                except pikepdf._core.PasswordError:
                    pass

            check_pass_need()

            def remove_password(password):
                show_cursor()
                reader = PdfReader(pdf_file)
                reader.decrypt(password)

                writer = PdfWriter()
                writer.append_pages_from_reader(reader)
                writer.encrypt("")

                with open(pdf_file, "wb") as out_file:
                    writer.write(out_file)
                
                print(Fore.GREEN, f"\bPassword of File '{pdf_file}' REMOVED Successfully.", Fore.RESET)

            passtry = 1
            if passwordliste:
                print(Fore.YELLOW, '\b[!] Testing Your Password List.\n', Fore.RESET)
                for password in passwordlist:
                    password = password.strip("\n")
                    if password == '' or password == '\n' or password == None:
                        continue
                    try:
                        pikepdf.open(pdf_file, password=password)
                        print(Fore.GREEN, f"\b\n[+] Password : {password}", Fore.RESET)
                        show_cursor()
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
                        pikepdf.open(pdf_file, password=password)
                        print(Fore.GREEN, f"\b\n[+] Password : {password}", Fore.RESET)
                        ASK = input("[?] Do You Want Remove PASSWORD (Y/n): ")
                        if ASK == '' or ASK == '\n' or ASK == None or ASK.lower() == 'y':
                            remove_password(password)
                        show_cursor()
                        exit(0)
                    except pikepdf._core.PasswordError:
                        passtry += 1
                        print(Fore.RED, f"\b[*] {passtry:,} Password Tesded.", Fore.RESET, end='\r', sep='')

                print(Fore.RED, f'\b\n[-] PassList{number_of_passlist} Faild.', Fore.RESET)

            Faild()
        except KeyboardInterrupt:
            print(Fore.RED, '\b\n[-] Quiting PDF Cracker.....', Fore.RESET)
            show_cursor()
            exit(0)

if __name__ == '__main__':
    main()
