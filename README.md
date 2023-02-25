# Simple Port Scanner

[![GitHub license](https://img.shields.io/github/license/notyuu/scan-ports)](https://github.com/notyuu/scan-ports/blob/main/LICENSE)

## Description

A simple Python script that allows you to scan for open ports on a given host. It can be useful for checking the security of your network or for troubleshooting network issues.

## Installation

To use this script, you will need Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/

After installing Python, download or clone this repository to your local machine.

`git clone https://github.com/notyuu/scan-ports.git`

`cd scan-ports`

`pip install pyfiglet && pip install argparse`



## Usage

`python scan.py -h`

![alt text](https://github.com/notyuu/scan-ports/blob/main/screenshot/usage.png)

To run the port scanner, open a terminal and navigate to the directory where you saved the script. Then, run the following command:


`python scan.py -t scanme.nmap.org -s` Replace `-t <host>` with the IP address or hostname of the target machine, `-p <port>` with the port you want to scan or `-p n1,n2,n3,n4` if you want to scan a list of ports or you can use `-p-` to scan All ports from 1:65535 .

by Default is scanning All ports.

also you can use `-m` or `--mostports` to scan the most popular 100 port maybe open, the list of it .

if you want to see the prosses when scaning all ports you can use `-s` or `--show`.



![alt text](https://github.com/notyuu/scan-ports/blob/main/screenshot/scan.png)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! If you have any suggestions for improving this script, please open an issue or submit a pull request.

## Acknowledgements

This project was inspired by the port scanner tutorial on Real Python: https://realpython.com/python-port-scanner/

## Contact Me

Discord: Yuu#8192
