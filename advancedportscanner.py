#!/bin/env/ python
from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(tgtHost, tgtPorts):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPorts))
        print(colored(" [+] %d/tcp Open" % tgtPorts, 'green'))
    except:
        print(colored(" [-] %d/tcp Closed" % tgtPorts, 'red'))

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print ("Unknown Host %s " % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(" [+] Scan Results for: " + tgtName[0])
    except:
        print(" [+] Scan Results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPorts in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPorts)))
        t.start()

def main():
    parser = optparse.OptionParser("Usage of program: " + "--host <target host> -p <target port>")
    parser.add_option("--host", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-p", dest="tgtPorts", type="string", help="specify target ports separated by comma")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(",")
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()
#made by EazyModz
