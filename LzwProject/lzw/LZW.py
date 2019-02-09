#!/usr/bin/env python3

from math import floor, ceil, log
from typing import AnyStr
import os

############ DA AGGIUNGERE LE RETURN ALLE FUNZIONE DOVE MANCA e RENDERLE PIU' VELOCI, SONO LENTE
def compressFile(infile):

    F = open(infile,'r')
    DC = compress(F.read())
    F.close()
    return writeCompressed(DC, infile)


def writeCompressed(data, infile):
    
    filename, file_extension = os.path.splitext(infile)
    outfile = filename+".Z"
    Fout = open(outfile,'wb')
    Fout.write(data)
    Fout.close()
    return os.path.getsize(outfile)

#### da migliorare
def compress(data: AnyStr) -> bytes:

    ascitoint = {i.to_bytes(1, 'big'): i for i in range(256)}
    inttoasci = {i: b for b, i in ascitoint.items()}

    if isinstance(data, str):
        data = data.encode()
    keys = ascitoint.copy()
    n_keys = 256
    compressed = []
    start= 0
    n_data = len(data)+1
    while True:
        if n_keys >= 512:
            keys = ascitoint.copy()
            n_keys = 256
        for i in range(1, n_data-start):
            w =  data[start:start+i]
            if w not in keys:
                compressed.append(keys[w[:-1]])
                keys[w] = n_keys
                start += i-1
                n_keys += 1
                break
        else:
            compressed.append(keys[w])
            break
    bits= ''.join([bin(i)[2:].zfill(9) for i in compressed])
    a = int(bits, 2).to_bytes(ceil(len(bits) / 8), 'big')
    return a

def decompressFile(infile):
    
    F = open(infile,'rb')
    UC = decompress(F.read())
    F.close()
    return writeDecompressed(UC, infile)

def writeDecompressed(data, infile):
    
    filename, file_extension = os.path.splitext(infile)
    outfile = filename#+".dec"
    Fout = open(outfile,'wb')
    Fout.write(data)
    Fout.close()
    return os.path.getsize(outfile)
    


def decompress(data: AnyStr) -> bytes:

    ascitoint = {i.to_bytes(1, 'big'): i for i in range(256)}
    inttoasci = {i: b for b, i in ascitoint.items()}

    if isinstance(data, str):
        data = data.encode()
    keys= inttoasci.copy()
    bits = bin(int.from_bytes(data, 'big'))[2:].zfill(len(data) * 8)
    n_extended_bytes= floor(len(bits) / 9)
    bits= bits[-n_extended_bytes * 9:]
    data_list = [int(bits[i*9:(i+1)*9], 2) for i in range(n_extended_bytes)]
    previous= keys[data_list[0]]
    uncompressed = [previous]
    n_keys = 256
    for i in data_list[1:]:
        if n_keys >= 512:
            keys = inttoasci.copy()
            n_keys = 256
        try:
            current = keys[i]
        except KeyError:
            current = previous + previous[:1]
        uncompressed.append(current)
        keys[n_keys] = previous + current[:1]
        previous = current
        n_keys += 1


    xxx = b''.join(uncompressed)
    return xxx


def utils(num: int) -> str:

    list = ['bytes', 'kB', 'MB', 'GB', 'TB', 'PB']
    order = int(log(num, 1024))
    number = num / 1000 ** order
    size = list[order]
    final = [str(round(number,2)), size]
    return ''.join(final)

        
