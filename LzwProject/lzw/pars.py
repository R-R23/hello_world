#!/usr/bin/env python3

import argparse
import os
from LZW import compressFile as C
from LZW import utils as U
from LZW import decompressFile as dec

class Parser:
 
    def __init__(self):

        self.parser = argparse.ArgumentParser(description='LZW Compress/Decompress')
        self._args = []
        self._acceptExtCompress = ['.html','.htm','.c','.cc','.txt','.py']
        self._acceptExtDecompress = ['.lzw','.z','.Z']

   
    def action(self):
        
        self.parser = argparse.ArgumentParser(description='LZW Compress/Decompress')
        self.parser.add_argument('-v','--verbose', help = 'Add Verbosity', action='store_true', default=False)
        action = self.parser.add_mutually_exclusive_group(required=True)
        action.add_argument('-r','--recursive', nargs=1, help='Recursive mode over a directory', default = '')
        action.add_argument('-d', '--decompress', nargs='+', help='Decompress mode', default= [])
        action.add_argument('-c', '--compress', nargs='+', help='Compress mode', default = [])


        args = self.parser.parse_args()

        R = ''.join(args.recursive)
        Clist = []
        Dlist = []
        for i in args.compress:
            if os.path.isfile(i):
                Clist.append(i)
        V = args.verbose
        for j in args.decompress:
            if os.path.isfile(j):
                Dlist.append(j)
        V = args.verbose
        self.call(R=R,V=V,listC=Clist,listD=Dlist)

    def call(self,R=None,V=None, listC=None, listD=None):

        if R and os.path.isdir(R):     
             self.isaDir(R, V)
        elif listC or listD:
            for i in listC:
                self.isaFile(i,1,V)
            for j in listD:
                self.isaFile(j,2,V)
        else:
            print('Error in insertion')

    def isaFile(self, F, mode, verbose):


        filename, file_extension = os.path.splitext(F)
        initial_dim = os.path.getsize(F)

        if mode == 1:
            if file_extension in self._acceptExtCompress:                
                final_dim = C(F)
                percent = (1-(final_dim/initial_dim))*100
                if percent > 0:
                    if verbose:                               
                        print('- compression:', os.path.basename(filename), U(initial_dim), U(final_dim), "{0:.2f}".format(percent)+'%')
                        os.unlink(F)
                else:
                    if verbose:
                        print(' [*] compression aborted', filename)
                        print('- compression:', os.path.basename(filename), U(initial_dim), U(final_dim), "{0:.2f}".format(percent)+'%')
                        todelete = filename+'.Z'
                        os.unlink(todelete)
            else:
                print('!-! Extension Error (C)')
        elif mode == 2:
            if file_extension in self._acceptExtDecompress:
                final_dim = dec(F)
                if verbose:
                    print('- uncompression : ', os.path.basename(filename), U(initial_dim), U(final_dim))
                    os.unlink(F)
            else:
                print('!-! Extension Error (D)')

        else:
            print('Error in insertion')

    def isaDir(self, path, verbose):
        comprlist = []      # lista dei file da comprimere
        unused = []         # file da non toccare
        files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        # le subdirecotry che trova lì dentro
        subdir = [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension in self._acceptExtCompress:
                comprlist.append(f)
            else:
                unused.append(f)

        if verbose:
            print('\n*) File(s) unused :\n', unused, '\n')
        self.call(listC=comprlist, V=verbose)
        if subdir:
            for k in subdir:
                self.call(R=k,V=verbose)


def main():

    p = Parser()
    p.action()


main()


        
        
