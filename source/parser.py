# 文法
from lexer import Obstract



# print("Error: Too many types (" + x["type"] + ")! in line: ", x["line"], " ,in column: ", x["column"])
KeyWord = ["INT", "STRING", "FLOAT", "BOOL", "FUN", "IF", "ELSE", "CLASS", "TRUE", "FALSE", "IMP", "CONST", "RET", "PRI", "PRO", "VOID", "ANY"]
Error = False
types = ["INT", "STRING", "BOOL", "FLOAT"]
types_fun = ["INT", "STRING", "BOOL", "FLOAT", "VOID", "ANY"]
Types_in = {"INT" : "NUMBER", "STRING": "STR", "FLOAT" : "FLOATNUMBER"}
determiner = ["PRI", "PRO"]

def parser(Token : list) :
    ps = Token_Append_KeyWords(Token)
    ps = Token_Append_Type(ps)
    return ps

def Token_Append_KeyWords(Token : list) :
    global Error
    parser = [{"type" : "POP"}]
    while len(Token) != 0:
        x = Token[0]
        Token.pop(0)
        if x["type"] == parser[-1]["type"]:
            Error = True
            print("Error: Too many types (" + x["type"] + ")! in line: ", x["line"], " ,in column: ", x["column"])
            continue
        parser.append(x)
        continue
    parser.pop(0)
    return parser

def Function_True(PDD : list) :
    # TODO < Function >
    pass

"""
function ->
<Obstract_> = ( <Obstract )
<Obstract> = <type> <identifier>
<Obstract> = <Obstract> ,
<Obstract> = 
function <type> <identifier> <Obstract_> {  }
"""


def Token_Append_Function(Token : list) :
    bm = 0
    PDD = 0
    parser = []
    global Error
    while len(Token) != 0:
        x = Token[0]
        Token.pop(0)
        b = x["type"]
        if b != "FUN" :
            parser.append(x)
            continue
        PDD.append(x)
        x = Token[0]
        Token.pop(0)
        b = x["type"]
        # fun Type Identifier (  ) {  }
        if b not in types_fun :
            Error = True
            print("Error: Error of function return type! in line: ", x["line"], " ,in column: ", x["column"])
            x["type"] = "ANY"
        PDD.append(x)
        x = Token[0]
        Token.pop(0)
        b = x["type"]
        if b != "IDENTIFIER" :
            Error = True
            print("Error: Error of function name! in line: ", x["line"], " ,in column: ", x["column"])
            x["type"] = "IDENTIFIER"
        PDD.append(x)
        x = Token[0]
        Token.pop(0)
        b = x["type"]
        if b == "(" :
            while b == ")" :
                PDD.append(x)
                x = Token[0]
                Token.pop(0)
                b = x["type"]
                if b == "ENDER" :
                    Error = True
                    print("Error: Error of function )! in line: ", x["line"], " ,in column: ", x["column"])
                    x["type"] == ")"
                    break
            x = Token[0]
            Token.pop(0)
            b = x["type"]           
            if b == "{" :
                bm += 1
                while bm == 0 :
                    x = Token[0]
                    Token.pop(0)
                    b = x["type"]
                    if b == "{" :
                        bm += 1
                    elif b == "}" :
                        bm -= 1
            else :
                Error = True
                print("Error: Error of function {! in line: ", x["line"], " ,in column: ", x["column"])
        else :
            Error = True
            print("Error: Error of function (! in line: ", x["line"], " ,in column: ", x["column"])
        u = Function_True(PDD)
        parser.append(u)
    return parser
                



def Token_Append(Token : list) :
    sm = 0
    zm = 0
    bm = 0
    global Error
    parser = []
    while len(Token) != 0 :
        x = Token[0]
        Token.pop(0)
        b = x["type"]
        # 太小

        if b in Obstract :
            if b == "(" :
                sm += 1
            elif b == ")" :
                sm -= 1
            elif b == "[" :
                zm += 1
            elif b == "]" :
                zm -= 1
            elif b == "{" :
                bm += 1
            else :
                bm -= 1
            parser.append(x)
            if sm > 0 or zm > 0 or bm > 0:
                Error = True
                print("Error: Paired parentheses could not be found ! in line: ", x["line"], " ,in column: ", x["column"])
                continue
            continue
        parser.append(x)
    return parser

def Token_Append_Type(Token):
    global Error
    parser = []
    tp = "NULL"
    booll = False
    while len(Token) != 0 :
        x = Token[0]
        Token.pop(0)
        if x["type"] in types :
            parser.append(x)
            tp = x["type"]
            if x["type"] == "BOOL" :
                booll = True
            x = Token[0]
            Token.pop(0)
            if x["type"] == "IDENTIFIER" :
                parser.append(x)
                x = Token[0]
                Token.pop(0)
                if x["type"] == "SET" :
                    parser.append(x)
                    x = Token[0]
                    Token.pop(0)
                    if booll :
                        if x["type"] == "TRUE" or x["type"] == "FALSE":
                            parser.append(x)
                            print("Error: No Bool Type ! in line: ", x["line"], " ,in column: ", x["column"])
                            continue
                    if x["type"] == Types_in[tp] :
                        parser.append(x)
                        continue
                    else :
                        Error = True
                        print("Error: No Type "+ tp +" to "+ x["type"]+" ! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                else :
                    Error = True
                    print("Error: No rule ! in line: ", x["line"], " ,in column: ", x["column"])
                    continue
            else :
                Error = True
                print("Error: No rule ! in line: ", x["line"], " ,in column: ", x["column"])
                continue
        else :
            parser.append(x)
    return parser
