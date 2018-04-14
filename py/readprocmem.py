
import getopt
import os, sys
import re

def showHelp():
    print("Read memory info of a process in Linux")
    print("Parameters:")
    print("   -p  Process id")
    print("   -a  Memory address")
    print("   -s  Size of memory to show")

def printMemInHex(chunk, size):
    i = 0
    chunk_str = chunk[:]
    offset = 0
    for b in chunk:
        i = i + 1
        offset = offset + 1
        print(hex(ord(b))[2:].zfill(2) + " "),
        if i < 16: continue
        print("   " * (16 - i)),
        print("     : "),
        print(chunk_str[(offset-i):offset])
        i = 0
    #pass

def readProcMem(p, a, s):
    ppath = "/proc/" + str(p) + "/"
    maps_file = open(ppath + "maps", 'r')
    mem_file = open(ppath + "mem", 'r', 0)
    for line in maps_file.readlines():  # for each mapped region
        m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
        if m.group(3) == 'r':  # if this is a readable region
            start = int(m.group(1), 16)
            end = int(m.group(2), 16)
            
            if a >= start and a <= end:
                mem_file.seek(a)  # seek to region start
                chunk = mem_file.read(min(s, (end - a)))
                printMemInHex(chunk, min(s, (end - a)))
    maps_file.close()
    mem_file.close()

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
