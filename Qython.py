#!/usr/bin/python3.10

import sys

from source import check
from source import io

argc = sys.argv

version = False
compiler = False
about = False
output = False
default = False

files = []

def func() :
    print("""
            This is Qython Complier
            Qython to Python, just like tsc of TypeScript
            ===========
            default :
                Can to complier

            --version :
                print version

            --Complier / -c :
                Complier file

                    --output / -o :
                        set output file name
                        Note that the operation name is from left to right!

            --about :
                show this

            --exit:
                not to do
            """)

def check_1(argc) :
    global files, compiler, version, compiler, about, output, default
    flame = False
    for i in argc :
        if i == "--Complier" or i == "-c" :
            compiler = True
        elif i == "--version" or i == "-v" :
            version = True
        elif i == "--about" :
            about = True
        elif i == "--output" or i == "-o" :
            output = True
        elif i == "--exit" :
            sys.exit(0)
        elif compiler :
            files.append(i)
        elif io.isFile(i) :
            files.append(i)
        else :
            raise Exception("Error in "+ i)

if __name__ == "__main__" :
    check_1(argc)
    sb = io.readInString(files[1])
    # print(sb)
    u = check.Token(sb)
    print(u)

