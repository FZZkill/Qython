# 文法
Error = False
types = ["INT", "STRING", "BOOL", "FLOAT"]
determiner = ["PRI", "PRO"]
boolean = ["TRUE", "FALSE"]
# Other = ["class", "function", "if", "else", "imp", "const", "ret"]

def parser(Token : list) :
    ps = Token_Append_KeyWords(Token)
    return ps

def Token_Append_KeyWords(Token) :
    global Error
    parser = [{"type": "POP"}]

    while len(Token) != 0:
        x = Token[0]
        Token.pop(0)

        if x["type"] in types :
            if parser[-1]["type"] in types :
                Error = True
                print("Error: Too many types! in line: ", x["line"], " ,in column: ", x["column"])
                continue
            parser.append(x)
            continue

        if x["type"] in determiner :
            if parser[-1]["type"] in determiner :
                Error = True
                print("Error: Too many types! in line: ", x["line"], " ,in column: ", x["column"])
                continue
            parser.append(x)
            continue

        if x["type"] in boolean :
            if parser[-1]["type"] in boolean :
                Error = True
                print("Error: Too many types! in line: ", x["line"], " ,in column: ", x["column"])
                continue
            parser.append(x)
            continue
        else :
            if x["type"] == "IDENTIFIER" :
                if parser[-1]["type"] == "IDENTIFIER" :
                    Error = True
                    print("Error: Too many identifiers! in line: ", x["line"], " ,in column: ", x["column"])
                    continue
                parser.append(x)
                continue
            if x["type"] == "ENDER" :
                if parser[-1]["type"] == "ENDER" :
                    continue
                parser.append(x)
                continue
            else :
                if x["type"] == "CLASS" :
                    if parser[-1]["type"] == "CLASS" :
                        Error = True
                        print("Error: Too many CLASS! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue

                if x["type"] == "FUNCTION" :
                    if parser[-1]["type"] == "FUNCTION" :
                        Error = True
                        print("Error: Too many FUNCTION! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue

                if x["type"] == "IF" :
                    if parser[-1]["type"] == "IF" :
                        Error = True
                        print("Error: Too many IF! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue
                if x["type"] == "ELSE" :
                    if parser[-1]["type"] == "ELSE" :
                        Error = True
                        print("Error: Too many ELSE! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue

                if x["type"] == "IMP" :
                    if parser[-1]["type"] == "IMP" :
                        Error = True
                        print("Error: Too many IMP! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue
                if x["type"] == "CONST" :
                    if parser[-1]["type"] == "CONST" :
                        Error = True
                        print("Error: Too many CONST! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue
                if x["type"] == "STR" :
                    if parser[-1]["type"] == "STR" :
                        Error = True
                        print("Error: Too many string! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue
                if x["type"] == "NUMBER" :
                    if parser[-1]["type"] == "NUMBER" :
                        Error = True
                        print("Error: Too many number! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continuk
                if x["type"] == "RET" :
                    if parser[-1]["type"] == "RET" :
                        Error = True
                        print("Error: Too many RET! in line: ", x["line"], " ,in column: ", x["column"])
                        continue
                    parser.append(x)
                    continue
                else :
                    parser.append(x)
    parser.pop(0)
    return parser
