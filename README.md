interface PortScannerREADME
{
    /* 
     * Port Scanner
     */

    /* Title */
    string title = "Simple Port Scanner";

    /* License Badge */
    string licenseBadge = "[![GitHub license](https://img.shields.io/github/license/notyuu/scan-ports)](https://github.com/notyuu/scan-ports/blob/main/LICENSE)";

    /* Description */
    string description = "A simple Python script that allows you to scan for open ports on a given host. It can be useful for checking the security of your network or for troubleshooting network issues.";

    /* Installation */
    string installation = "To use this script, you will need Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/\n\nAfter installing Python, download or clone this repository to your local machine.";

    /* Usage */
    string usage = "To run the port scanner, open a terminal window and navigate to the directory where you saved the script. Then, run the following command:\n\npython scan.py -t <host> -p <port> \n\nReplace -t <host> with the IP address or hostname of the target machine, -p with the Port you want to scan or you can add a list of ports by -p n1,n2,n3,n4 or you can scanning all port by -p- \n by default is scanning all ports ;

    /* License */
    string license = "This project is licensed under the MIT License. See the LICENSE file for details.";

    /* Contributing */
    string contributing = "Contributions are welcome! If you have any suggestions for improving this script, please open an issue or submit a pull request.";

    /* Acknowledgements */
    string acknowledgements = "This project was inspired by the port scanner tutorial on Real Python: https://realpython.com/python-port-scanner/";

};
