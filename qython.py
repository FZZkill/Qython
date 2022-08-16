import sys

if len(sys.argv) == 0 :
    print("""
|==MENU==|

Qython 

--version (about) -- Get info of about
--compiler (-f, -c) -- Compiler
    If you using '-f', You should using '-o', just like:
        
        qython -f example.qyt -o example.py



|==MENU==|


    """)
elif sys.argv[0] == "about" or sys.argv[0] == "--version":
    print("""
    This is my project to write a small compiler.
    It can compile Qython code to Python just like TypeScript to JavaScript.
    P.S: This is an exercise program, and I uploaded it to Github when I thought it was fun.
    This program may stop at some point.
    Version: 1.0
    """)
