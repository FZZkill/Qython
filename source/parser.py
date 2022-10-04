# 文法
KeyWord = ["INT", "STRING", "FLOAT", "BOOL", "FUNCTION", "IF", "ELSE", "CLASS", "TRUE", "FALSE", "IMP", "CONST", "RET", "PRI", "PRO"]
Error = False
types = ["INT", "STRING", "BOOL", "FLOAT"]
Types_in = {"INT" : "NUMBER", "STRING": "STR", "FLOAT" : "FLOATNUMBER"}
determiner = ["PRI", "PRO"]
boolean = ["TRUE", "FALSE"]

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

def Token_Append_Type(Token):
    global Error
    parser = []
    tp = "NULL"
    booll = False
    while len(Token) != 0:
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
