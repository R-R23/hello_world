#!/bin/bash
a=${1?Error: no parameter given}
b=${2}
if [ $a == "-v" ]; then
    if [ $b == "-r" ]; then
        c=${3}
        ../lzw/__main__.py $a $b $c
    else
        ../lzw/__main__.py $a -c $b
    fi
elif [ $a == "-r" ]; then
    ../lzw/__main__.py $a $b
else
    ../lzw/__main__.py -c $a
fi
