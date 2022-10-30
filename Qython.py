#!/usr/bin/python3.10

import sys

from source import io
from source.front import lexer
from source.front import parser

argc = sys.argv

version = False
compiler = False
about = False
output = False
default = False

files = []


def func():
    print(
        """
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
            """
    )


def check_1(argc):
    global files, compiler, version, compiler, about, output, default
    for i in argc:
        if i == "--Complier" or i == "-c" or i == "-f":
            compiler = True
        elif i == "--version" or i == "-v":
            version = True
        elif i == "--about":
            about = True
        elif i == "--output" or i == "-o":
            output = True
        elif i == "--exit":
            sys.exit(0)
        elif compiler:
            files.append(i)
        elif io.isFile(i):
            files.append(i)
        else:
            print("Error in " + i)


if __name__ == "__main__":
    check_1(argc)
    if len(files) > 1:
        for i in range(len(files) - 1):
            sb = io.readInString(files[1])
            print(sb[-1])
            while True:
                if sb[-1] == "" or sb[-1] == " ":
                    print(sb[-1])
                    del sb[-1]
                    continue
                break
            TK = lexer.Lexer(sb)
            print(TK.Token)
            PR = parser.Parser(TK.Token)
            print(PR.parser)
    elif len(argc) > 1:
        if about:
            func()
    else:
        func()
