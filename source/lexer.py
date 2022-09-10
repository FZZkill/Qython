from source import io
# token :
KeyWord = ["int", "string", "float", "bool", "function", "if", "else"]
Key = ["\n", "\r"]
Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Sets = ['{', '}', '[', ']', '(', ')']
Using = ["+", "-", "*", "/", "=", ">", "<", ">=", "<=", "!", "!="]
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

        
#         if llm in KeyWord :
            # token.append((llm, None, line, column, pos))
        # elif llm in Using :
            # token.append(("OPERATOR", llm, line, column, pos))
        # elif llm in Sets :
            # token.append(("CONTROL", llm, line, column, pos))
        # elif llm.isdigit() :
            # token.append(("NUMBER", llm, line, column, pos))
        # else :
        pos+=1
        box += x
    return token
