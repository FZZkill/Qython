from source import io
# token : 
KeyWord = ["int", "string", "float", "bool"]

Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
Sets = ["{", "}", "[", "]", "(", ")"]
Using = ["+", "-", "*", "/", "=", ">", "<", ">=", "<="]
Other = [" ", "\n"]
def Token(value) :

    token = []
    # vaule = "int x = 1"
    column = 0
    line = 0
    pos = 0
    llm = ""

    while True :
        x = ""
        try :
            x = str(value[pos])
        except IndexError :
            break

        if x == "\n" or x == ';' :
            pos += 1
            line += 1
            column = 0
            llm = ""
            continue
        if x == " " :
            pos += 1
            column += 1
            continue

        while x in Letter:
            llm += x
            pos += 1
            x = str(value[pos])
            if x == " " :
                break

        while x in Number :
            llm += x
            pos += 1
            x = str(value[pos])
            if x == " " :
                break

        while x in Using :
            llm += x
            pos += 1
            x = str(value[pos])
            if x == " " :
                break

        if llm in KeyWord :
            token.append((llm, None))
        elif llm in Using :
            token.append(("OPERATOR", llm))
        elif llm.isdigit() :
            token.append(("NUMBER", llm))
        else :
            token.append(("UNDEFINE", llm))
        llm = ""

    return token
