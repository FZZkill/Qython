#!/usr/bin/python3.10

import sys
from src import check
from src import io


if len(sys.argv) == 1 :
    print("""
|==MENU==|

Qython 

--version (about) -- Get info of about
--compiler (-f, -c) -- Compiler
    If you using '-f', You should using '-o', just like:
        
        qython -f example.qyt -o example.py



|==MENU==|


    """)
elif sys.argv[1] == "about" or sys.argv[1] == "--version":
    print("""
    This is my project to write a small compiler.
    It can compile Qython code to Python just like TypeScript to JavaScript.
    P.S: This is an exercise program, and I uploaded it to Github when I thought it was fun.
    This program may stop at some point.
    Version: 1.0
    """)
elif sys.argv[1] == "-c" or sys.argv[1] == "--compiler" :
    reader = io.only_read(sys.argv[2])
    reader = io.reNote(reader)
    print(reader)
    TokenStream = check.check(reader)
    print(TokenStream)
    io.write(sys.argv[2][:-3]+"py", check.uncheck(TokenStream))
