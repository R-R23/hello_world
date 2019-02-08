#!/bin/bash
a=${1?Error: no parameter given }
b=${2}
if [ $a == "-v" ]; then
    ../lzw/pars.py $a -d $b
else
    ../lzw/pars.py -d $a
fi

