
import getopt
import os, sys

def showHelp():
    print("Read memory info of a process in Linux")
    print("Parameters:")
    print("   -p  Process id")
    print("   -a  Memory address")
    print("   -s  Size of memory to show")

def readProcMem(p, a, s):
    pass

def getAddrFromInput(v):
    if len(v) <= 2: return int(v)

    if v[:2] == "0x" or v[:2] == "0X": return int(v, 16)
    else:                              return int(v)

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hp:a:s:')

    pid, addr, size = 0, 0, 0
    for k, v in opts:
        if k == "-h": showHelp()
        if k == "-p": pid = int(v)
        if k == "-a": addr = getAddrFromInput(v)
        if k == "-s": size = int(v)
        
    print(pid, addr, size)
    readProcMem(pid, addr, size)
