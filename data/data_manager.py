import json
import uuid
import os
from pystyle import Colors, Write, System

__path = os.path.dirname(__file__) + "/server.json"

def write_info_about_server(port=6969, listen="?", address="auto"):
    """? -> 690000000000"""
    if os.path.exists(__path) == False:
        with open(__path, "w") as file:
            data = json.dump({"address": address, "port": port, "listen": "?"}, file, indent=3)
            Write.Print("Create File [server.json]", Colors.blue_to_purple, end=Colors.reset + "\n", interval=0.01)
            Write.Print(f"Port {port}, listen {listen}, address {address}", Colors.blue_to_purple, end=Colors.reset + "\n", interval=0.01)
    

def get_port() -> int:
    return json.load(open(__path, "r"))["port"]

def get_address() -> int:
    return json.load(open(__path, "r"))["address"]

def get_listen() -> int:
    return json.load(open(__path, "r"))["listen"]