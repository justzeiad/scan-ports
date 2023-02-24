import socket,sys, pyfiglet
from datetime import datetime
import argparse

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print(pyfiglet.figlet_format("Made By Yuu", font = "digital" ))

parser = argparse.ArgumentParser(description='Scan target URL for open ports using nmap')
parser.add_argument('-t', '--target', type=str,nargs='?', required=True,
                    help='Target URL or IP address')
parser.add_argument('-p', '--port', type=str, nargs='?', default='-',
                    help='Target port number(s). Use -p- to scan all ports.')
parser.add_argument('-s', '--show', action='store_true',
                    help='Show the result')

parser.add_argument('-m', '--mostports', action='store_true', help='Scanning Most popular ports')


args = parser.parse_args()

target = args.target
port = args.port
show = args.show
most = args.mostports

def Header():
    print("-"*50)
    print("Scaning Target: ", target , f"({socket.gethostbyname(target)})")
    print("Scaning Start At: " , str(datetime.now()))
    print("-"*50)

Header()



def ScanAll():
    for p in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, p))
            
        if result == 0:
            printer = f"\033[32m[+]\033[0m \033[32m{HservByPort(p)}\033[0m Port \033[32m{p}\033[0m Is Open"
            print(printer)
        else:
            if show:
                printer = f"\033[31m[-]\033[0m \033[31m{HservByPort(p)}\033[0m Port \033[31m{p}\033[0m Is Close"
                print(printer)

        s.close()


def ScanPort(port):
    ports = port.split(',')

    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, int(p)))
        if result == 0:
            printer = f"\033[32m[+]\033[0m \033[32m{HservByPort(p)}\033[0m Port \033[32m{p}\033[0m Is Open"
            print(printer)
            
        else:
            printer = f"\033[31m[-]\033[0m \033[31m{HservByPort(p)}\033[0m Port \033[31m{p}\033[0m Is Close"
            print(printer)
        
        s.close()


def HservByPort(p):
    try:
        serv = socket.getservbyport(int(p))
    except OSError:
        serv = "Unknown"
    return serv

def ScanMustPort():
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 5432, 8080]
    for n in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, n))
        if result ==0:
            printer = f"\033[32m[+]\033[0m \033[32m{HservByPort(n)}\033[0m Port \033[32m{n}\033[0m Is Open"
            print(printer)
        else:
            printer = f"\033[31m[-]\033[0m \033[31m{HservByPort(n)}\033[0m Port \033[31m{n}\033[0m Is Close"
            print(printer)
        s.close()


try:
    if most:
        ScanMustPort()

    elif port == '-':
        ScanAll()

    else:
        ScanPort(port)
        

except KeyboardInterrupt:
        print("\n \033[1;33;40mExiting Program !\033[0m")
        sys.exit()


except socket.gaierror:
        print("\n \033[1;33;40mThe hostname cannot be reached !\033[0m")
        sys.exit()
        
