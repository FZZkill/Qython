"""
# Powered by FZZkill
# Code with neovim
# Project: Qython
# author: FZZkill
# License: Mozilla Public License 2
"""
from src import funs
lsFile = []
# Token stream
token = []
items = []
types = {}
ramdoms = 0
TokenStream = []

KEYWORD_TYPE = ("int", "string", "float", "char")
KEYWORD_LINE = ("void")
KEYWORD_CLAS = ("l")
KEYWORD_CLAS_l = ["println", "print"]

def check(Items : str) -> list :
    global lsFile, types, items, token, TokenStream, ramdoms
    lsFile = Items.split("\n")
    for i in range(len(lsFile)-1):
        lsLine = lsFile[i].split(" ")
        lsPop = lsFile[i].split(".")
        # [number, x, =, 15]
        # types = {x : [15, number]}
        for j in KEYWORD_TYPE :
            if lsLine[0] == j and lsLine[2] == '=':
                types[lsLine[1]] = lsLine[1]+"="+lsLine[3] # Vaule, Mode, Type
                token.append(lsLine)
                if items.count(lsLine[1]) >= 1:
                    raise Exception(lsLine[1] + " has times in line:" + str(i + 1) + "\n" + lsFile[i])
                items.append(lsLine[1])
        ramdoms = ramdoms + 1
        for j in KEYWORD_CLAS :
            if lsPop[0] == j :
                # 撞函数库
                functions = lsPop[1].split("(")
                print("xxx", functions)
                if functions[0] == "println":
                    functions = functions[1].split(")")
                    cmd = "COMMAND"+str(ramdoms)
                    items.append(cmd)
                    types[cmd] = funs.Fprintln(functions[0])
                    token.append("Function")
        ramdoms = ramdoms + 1
    ramdoms = ramdoms + 1

    TokenStream.append(items)
    TokenStream.append(types)
    TokenStream.append(token)
    return TokenStream

def uncheck(TokenStream = TokenStream) -> str :
    objs = ""
    for key in TokenStream[0] :
        # objs = objs + key + str(TokenStream[1][key][1]) + str(TokenStream[1][key][0]) + "\n"
        objs = objs + TokenStream[1][key] + "\n"
    return objs
