from pip import main
from os import system
from platform import system as platsys

restart = False

def install(library):
    main(["install", library])

def check_and_install(package):


    try:
        __import__(package)

        return False
    except:
        print(f"{package} Not Installed ....")
        install(package)
        restart = True



def start_check() -> bool:
    libraries = ["pystyle", "pyfiglet", "requests", "numpy", "pandas", "tabulate", "colorama"]
    
    for library in libraries:
        check_and_install(library)

    return restart
