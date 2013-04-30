'''
Created on Apr 26, 2013

@author: cforker
'''
from itertools import count
from Protein import Protein
from time import time

def leadingZeroes(binstring,length):
    return '0'*(length-len(binstring[2:])) + binstring[2:]

if __name__ == '__main__':
    t0 = time()
    N = 8
    # binary representation of proteins. 1=H,0=P
    for prot in count():
        if (prot == 2**N):
            break
        sprot = leadingZeroes(bin(prot),N)
        #print sprot
          
    ptest = Protein('01011111')
    ptest.setFolding([0,1,1,-1,-1,1])
    ptest.foldingDimensions()
    ptest.buildGrid()
    ptest.countHBonds()
    ptest.printEverything()
    t1 = time()
    print "Execution Time",round((t1 - t0)*1000),"ms"