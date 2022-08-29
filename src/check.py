"""
# Powered by FZZkill
# Code with neovim
# Project: Qython
# author: FZZkill
# License: Mozilla Public License 2
"""

import io
lsFile = []
# Token stream
token = []
items = []
types = {}

TokenStream = []

KEYWORD_TYPE = ["int", "string", "float", "char"]
KEYWORD_LINE = ["void"]
def check(Items : str) -> list :
    global lsFile, types, items, token, TokenStream
    lsFile = Items.split("\n")
    for i in range(len(lsFile)-1):
        lsLine = lsFile[i].split(" ")
        # [number, x, =, 15]
        # types = {x : [15, number]}
        for j in KEYWORD_TYPE :
            if lsLine[0] == j and lsLine[2] == '=':
                types[lsLine[1]] = [lsLine[3], "=", lsLine[0]] # Vaule, Mode, Type
                token.append(lsLine)
                if items.count(lsLine[1]) >= 1:
                    raise Exception(lsLine[1] + " has times in line:" + str(i + 1) + "\n" + lsFile[i])
                items.append(lsLine[1])
    TokenStream.append(items)
    TokenStream.append(types)
    TokenStream.append(token)
    return TokenStream

def uncheck(TokenStream = TokenStream) -> str :
    objs = ""
    for key in TokenStream[1] :
        objs = objs + key + str(TokenStream[1][key][1]) + str(TokenStream[1][key][0]) + "\n"
    return objs
