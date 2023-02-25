import socket,sys, pyfiglet
from datetime import datetime
import argparse

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print(pyfiglet.figlet_format("Made By Yuu", font = "digital" ))

parser = argparse.ArgumentParser(description='Scan target URL for open ports using scan-ports')
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

def ScanMostPort():
    common_ports = [80, 443, 22, 21, 25, 53, 110, 143, 587, 993, 995, 3306, 8080, 8443, 111, 445, 993, 1723, 137, 138, 139, 5900, 5901, 5902, 5903, 1433, 3389, 23, 161, 162, 69, 123, 389, 636, 3389, 1194, 8081, 8444, 465, 587, 514, 515, 631, 873, 2049, 111, 2049, 2048, 2047, 2046, 2045, 2044, 2043, 2042, 2041, 2040, 4045, 2869, 102, 1024, 1025, 1026, 1027, 1028, 1029, 3000, 3001, 8000, 8001, 9418, 27017, 27018, 27019, 3690, 9200, 5601, 15672, 61613, 61616, 5432, 5433, 5434, 5435, 5436, 5437, 5438, 5439, 5440, 5441, 54322, 10000, 17500, 5353, 6000, 30000, 49152, 49153, 49154, 49155, 49156, 49157]
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
        ScanMostPort()

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
        
