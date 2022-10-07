Key = ["\n", "\r", " "]
Number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Dicts = {"int" : "INT",
         "string" : "STRING",
         "float" : "FLOAT",
         "bool" : "BOOL",
         "if" : "IF",
         "else" : "ELSE",
         "class" : "CLASS",
         "true" : "TRUE",
         "false" : "FALSE",
         "fin" : "FIN",
         "fun" : "FUN",
         "imp" : "IMP",
         "ret" : "RET",
         "pri" : "PRI",
         "nil" : "NIL",
         "any" : "ANY",
         "'" : "STR",
         '"' : "STR",
         "+" : "ADD",
         "-" : "SUB",
         "*" : "MUL",
         "/" : "DIV",
         "=" : "SET",
         ">" : "BST",
         "<" : "BBT",
         "!" : "NOT",
         "{" : "BOS",
         "}" : "BOE",
         "(" : "SOS",
         ")" : "SOE",
         "[" : "MOS",
         "]" : "MOE",
         "," : "AND",
         "." : "USI"}

class TokenGroup() :
    def __init__(self, value) :
        self.pos = 0
        self.column = 0
        self.line = 0
        self.Token = []
        self.MakeToken(value)

    def poss(self, step = 1) :
        self.column += step
        self.pos += step

    def TokenIn(self, type_, value_) :
        self.Token.append({"type" : type_, "value" : value_, "line" : self.line, "column" : self.column})

    def MakeToken(self, value) :
        box = ""
        x = ""

        while self.pos != len(value) :
            try : x = str(value[self.pos])
            except IndexError : break

            if x in Key :
                self.line += 1
                if box in Dicts.keys() :
                    self.TokenIn(Dicts[box], None)
                else :
                    self.TokenIn("IDENTIFIER", box)
                self.poss()
                box = ""
                continue

            if x in Number :
                box += x
                self.poss
                while x not in Number :
                    try : x = str(value[self.pos])
                    except IndexError : break
                    box +=x
                    self.poss()
                self.TokenIn("NUMBER", box)
                box = ""
                continue
            box += x
            self.poss()

