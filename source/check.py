from source import io
# token :
KeyWord = ["int", "string", "float", "bool", "function", "if", "else"]
Key = ["\n", "\r"]
Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
Sets = ['{', '}', '[', ']', '(', ')']
Using = ["+", "-", "*", "/", "=", ">", "<", ">=", "<=", "!", "!="]
Other = [" ", "\n"]

def Token(value) :

    token = []
    column = 0
    line = 1
    pos = 0
    llm = ""

    x = ""
    while pos != len(value) :

        mod = ""
        try :
            x = str(value[pos])
        except IndexError :
            break

        if x == "\n" :
            pos += 1
            column += 1
            line += 1
            token.append(("ENDER", None, line, column, pos))
            continue
        
        if x == ';' :
            pos += 1
            column += 1
            token.append(("ENDER", None))
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
            while True :
                pos += 1
                try :
                    mod += x
                    x = str(value[pos])
                except IndexError:
                    token.append(("NUMBER", mod, line, column, pos))
                    break
                if x not in Number :
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
        token.append(("UNDEFINE", x, line, column, pos))

    return token
