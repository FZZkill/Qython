KeyWord = ["int", "string", "float", "bool", "function", "if", "else", "class", "true", "false", "imp", "const", "ret", "pri", "pro"]
Key = ["\n", "\r"]
Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
PSMD = ['+', '-', '*', '/']
Operator = ["==", ">", "<", ">=", "<=", "!", "!="]

def Token(value) :

    # token = [{"type" : "POP"}]
    token = [{"type":"pop", "value" : None}]
    column = 0
    line = 1
    pos = 0
    box = ""
    x = ""
    while pos != len(value) :

        mod = ""
        try :
            x = str(value[pos])
        except IndexError :
            break
        if x in Key:
            if box in KeyWord :
                token.append({"type" : box.upper(), "value" : None, "line" : line, "column" : column,"pos": pos})
            elif box != "" and box != " ":
                token.append({"type" : "IDENTIFIER", "value" : box, "line" : line, "column" : column,"pos": pos})
            box = ""
            pos += 1
            column += 1
            continue

        if x == ';' :
            if box in KeyWord :
                token.append({"type" : box.upper(), "value" : None, "line" : line, "column" : column,"pos": pos})
            elif box != "" and box != " ":
                token.append({"type" : "IDENTIFIER", "value" : box, "line" : line, "column" : column,"pos": pos})
            box = ""
            pos += 1
            column += 1
            if token[-1]["type"] == "ENDER" :
                continue
            else :
                token.append({"type" : "ENDER", "value" : None, "line" : line, "column" : column,"pos": pos})
                continue
        if x == ',' :
            if box in KeyWord :
                token.append({"type" : box.upper(), "value" : None, "line" : line, "column" : column,"pos": pos})
            elif box != "" and box != " ":
                token.append({"type" : "IDENTIFIER", "value" : box, "line" : line, "column" : column,"pos": pos})
            box = ""
            pos += 1
            column += 1
            if token[-1]["type"] == "ANDDER" :
                continue
            else :
                token.append({"type" : "ENDER", "value" : None, "line" : line, "column" : column,"pos": pos})
                continue


        # 是空格
        if x == ' ':
            if box in KeyWord :
                token.append({"type" : box.upper(), "value" : None, "line" : line, "column" : column,"pos": pos})
            elif box != "" and box != " ":
                token.append({"type" : "IDENTIFIER", "value" : box, "line" : line, "column" : column,"pos": pos})
            box = ""
            pos += 1
            column += 1
            continue

        # 调用
        if x == "." :
            pos += 1
            token.append({"type" : "DO", "value" : None, "line" : line, "column" : column,"pos": pos})
            continue

        # 是字符串
        if x == '"' :
            pos += 1
            b = value.index('"', pos)
            try :
                mod = value[pos:b]
            except IndexError :
                print("Error: No string end ! in line: ", x["line"], " ,in column: ", x["column"])
            build = mod.count("\n")
            line + build
            column += b
            pos += b
            token.append({"type" : "STR", "value" : mod, "line" : line, "column" : column,"pos": pos})
            continue

        if x == "'" :
            pos += 1
            try :
                b = value.index("'", pos)
            except IndexError :
                print("Error: Your single quotes are missing! in line :", line, " , in column", column)
            mod = value[pos:b]
            build = mod.count("\n")
            line + build
            column += b
            pos += b
            token.append({"type" : "STRING", "value" : None, "line" : line, "column" : column,"pos": pos})
            continue

        # 是数字
        if x in Number :
            floats = False
            while True :
                pos += 1
                try :
                    mod += x
                    x = str(value[pos])
                    if x == '.' and floats :
                        print("Error: Too many .! in line :", line, " ,in column :", column)
                    if x == '.' and not floats:
                        floats = True
                except IndexError:
                    if floats :
                        token.append({"type" : "FLOATNUMBER", "value" : mod, "line" : line, "column" : column,"pos": pos})
                    else :
                        token.append({"type" : "NUMBER", "value" : mod, "line" : line, "column" : column,"pos": pos})
                    break
                if x not in Number and x != ".":
                    if floats :
                        token.append({"type" : "FLOATNUMBER", "value" : mod, "line" : line, "column" : column,"pos": pos})
                    else :
                        token.append({"type" : "NUMBER", "value" : mod, "line" : line, "column" : column,"pos": pos})
                    break
            continue

        # 是限定符
        if x == "{" or x == "}" :
            if x == "{" :
                pos += 1
                token.append({"type" : "BIGLIMINTO", "value" : x, "line" : line, "column" : column,"pos": pos})
            else :
                token.append({"type" : "BIGLIMINTC", "value" : x, "line" : line, "column" : column,"pos": pos})
            continue

        if x == "[" or x == "]" :
            if x == "[" :
                pos += 1
                token.append({"type" : "MIDDLELIMINTO", "value" : x, "line" : line, "column" : column,"pos": pos})
            else :
                token.append({"type" : "MIDDLELIMINTC", "value" : x, "line" : line, "column" : column,"pos": pos})
            continue

        if x == "(" or x == ")" :
            if x == "(" :
                pos += 1
                token.append({"type" : "SMALLLIMINTO", "value" : x, "line" : line, "column" : column,"pos": pos})
            else :
                token.append({"type" : "SMALLLIMINTC", "value" : x, "line" : line, "column" : column,"pos": pos})
            continue

        # 是操作符
        if x in Operator :
            pos += 1
            pos += 1
            token.append({"type" : "OPERATOR", "value" : x, "line" : line, "column" : column,"pos": pos})
            continue

        # 是 赋值符 :
        if x == '=' :
            pos += 1
            #
            if token[-1]["type"] == "SET" :
                token.pop()
                token.append({"type": "OPERATOR", "value": "==", "line": line, "column":column, "pos":pos})
            else :
                token.append({"type": "SET", "value": "=", "line": line, "column":column, "pos":pos})
            continue

        # 是加减乘除
        if x in PSMD :
            pos += 1
            token.append({"type": "PSMD", "value": x, "line": line, "column":column, "pos":pos})

        column += 1
        pos += 1
        box += x
    token.pop(0)
    return token
