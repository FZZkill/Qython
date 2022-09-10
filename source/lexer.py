from source import io
# token :
KeyWord = ["int", "string", "float", "bool", "function", "if", "else", "class"]
Key = ["\n", "\r"]
Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
PSMD = ['+', '-', '*', '/']
Operator = ["==", ">", "<", ">=", "<=", "!", "!="]
Other = [" ", "\n"]

def Token(value) :

    token = []
    column = 0
    line = 1
    pos = 0
    llm = ""
    box = ""
    x = ""
    while pos != len(value) :

        mod = ""
        try :
            x = str(value[pos])
        except IndexError :
            break

        if x == "\n":

            if box in KeyWord :
                token.append((box.upper(), None, line, column, pos))
            elif box != "" and box != " ":
                token.append(("IDENTIFIER", box, line, column, pos))
            box = ""

            pos += 1
            column += 1
            line += 1
            if token[-1][0] == "ENDER" :
                continue
            else :
                token.append(("ENDER", None, line, column, pos))
                continue

        if x == ';' :
            if box in KeyWord :
                token.append((box.upper(), None, line, column, pos))
            elif box != "" and box != " ":
                token.append(("IDENTIFIER", box, line, column, pos))
            box = ""
            pos += 1
            column += 1
            if token[-1][0] == "ENDER" :
                continue
            else :
                token.append(("ENDER", None, line, column, pos))
                continue

        # 是空格
        if x == ' ': 
            if box in KeyWord :
                token.append((box.upper(), None, line, column, pos))
            elif box != "" and box != " ":
                token.append(("IDENTIFIER", box, line, column, pos))
            box = ""
            pos += 1
            column += 1
            continue

        # 调用

        if x == "." :
            pos += 1
            token.append(("GIT", None, line, column, pos))
            continue

        # 是字符串
        if x == '"' :
            pos += 1
            b = value.index('"', pos)
            mod = value[pos:b]
            build = mod.count("\n")
            line + build
            column += b
            pos += b
            token.append(("STRING", mod, line, column, pos))
            continue

        if x == "'" :
            pos += 1
            b = value.index("'", pos)
            mod = value[pos:b]
            build = mod.count("\n")
            line + build
            column += b
            pos += b
            token.append(("STRING", mod, line, column, pos))
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
                        raise Exception("Fuck You Float '.'")
                    if x == '.' and not floats:
                        floats = True

                except IndexError:
                    if floats :
                        token.append(("FLOAT", mod, line, column, pos))
                    else :
                        token.append(("NUMBER", mod, line, column, pos))
                    break
                if x not in Number and x != ".":
                    if floats :
                        token.append(("FLOAT", mod, line, column, pos))
                    else :
                        token.append(("NUMBER", mod, line, column, pos))
                    break
            continue

        # 是限定符
        if x == "{" or x == "}" :
            pos += 1
            token.append(("BIGLIMINT", x, line, column, pos))
            continue
        if x == "[" or x == "]" :
            pos += 1
            token.append(("MIDDLELIMINT", x, line, column, pos))
            continue
        if x == "(" or x == ")" :
            pos += 1
            token.append(("SMALLLIMINT", x, line, column, pos))
            continue

        # 是操作符
        if x in Operator :
            llm = ""
            pos += 1
            llm += x
            if value[pos] in Operator :
                llm += value[pos]
                pos += 1
                token.append(("OPERATOR", llm, line, column, pos))
            else :
                token.append(("OPERATOR", llm, line, column, pos))
            continue

        # 是 赋值符 :
        if x == '=' :
            pos += 1
            if token[-1][0] == "SET" :
                token.pop()
                token.append(("OPERATOR", "==", line, column, pos))
            else :
                token.append(("SET", x, line, column, pos))
            continue

        # 是加减乘除
        if x in PSMD :
            pos += 1
            token.append(("PSMD", x, line, column, pos))

#         if llm in KeyWord :
            # token.append((llm, None, line, column, pos))
        # elif llm in Operator :
            # token.append(("OPERATOR", llm, line, column, pos))
        # elif llm in Limint :
            # token.append(("CONTROL", llm, line, column, pos))
        # elif llm.isdigit() :
            # token.append(("NUMBER", llm, line, column, pos))
        # else :
        pos+=1
        box += x
    return token
