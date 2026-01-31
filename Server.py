import Configure.init_server as init_server
import data.data_manager as data_manager

init_server.start_check()

if init_server.restart == True:

    print("The Server Need To Restart...")
    print("Run This Server Again")
    exit()

try:
    import PyQt5
    import socket
    from pystyle import Colors, Write, System, Cursor, Colorate
    from pyfiglet import figlet_format
    from platform import system as platsys, node
    from os import system, get_terminal_size
    from colorama import Fore
except:
     print("Error...")
     exit()

def _print(message, time=0.01, color=Colors.blue_to_purple):
    Write.Print(message, color, end=Colors.reset + "\n", interval=time)

def _input(message, color=Colors.blue_to_purple, time=0.01):
        Write.Input(message, color, end=Colors.reset, interval=time)



class server:

    lines:int = 700
    columns:int = 700
    titleBanner:str = "E c h o\nServer"

    def __init__(self):
        
        self.configure()
        self.command_terminal()
    
    def configure(self):
        System.Init()
        Cursor.HideCursor()
        data_manager.write_info_about_server()

        if platsys() == "Linux":
            system("clear")
        

        self.banner()

    def banner(self):

            __banner = Colorate.Horizontal(Colors.blue_to_white, "".join(line.center(get_terminal_size().columns) for line in figlet_format(self.titleBanner, "slant").splitlines()))

            print(__banner)
            _print(("This Tool Created By '! La La la'".ljust(35) + "Discord -> @uuuc").center(get_terminal_size().columns))

    def command_terminal(self):

        while True:
            r = str(input(f"{Fore.LIGHTYELLOW_EX}{node()}{Fore.WHITE}@Echo{Fore.RESET}{Fore.LIGHTGREEN_EX}${Fore.RESET}"))

            match r:

                case "1":
                    self.normal_server()
                    break
                
                case "cls" | "clear":
                    if platsys() == "Linux":
                         system("clear")
                         self.banner()

                    elif platsys() == "Windows":
                         system("cls")
                         self.banner()
                
    
    def normal_server(self):
        _print("Create Normal Server...", color=Colors.white)
        _print(f"address -> {data_manager.get_address()}, port -> {data_manager.get_port()}, listen -> {data_manager.get_listen()}", color=Colors.white)


def main():

    server()


if __name__ == "__main__":

    main()