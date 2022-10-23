from source.DEFINE import Key
from source.DEFINE import Dicts
from source.DEFINE import Number


class TokenGroup:
    def __init__(self, value):
        self.pos = 0
        self.column = 0
        self.line = 0
        self.Token = []
        self.MakeToken(value)

    def poss(self, step=1):
        self.column += step
        self.pos += step

    def TokenIn(self, type_, value_):
        self.Token.append(
            {
                "type": type_,
                "value": value_,
                "line": self.line,
                "column": self.column,
            }
        )

    def MakeToken(self, value):
        box = ""
        x = ""

        while self.pos != len(value):
            try:
                x = str(value[self.pos])
            except IndexError:
                break

            if x in Key:
                if x == "\n" or x == "\r":
                    self.line += 1
                    self.TokenIn("Ender", None)
                if box not in Key:
                    if box in Dicts.keys():
                        self.TokenIn(Dicts[box], None)
                    else:
                        self.TokenIn("IDENTIFIER", box)
                self.poss()
                box = ""
                continue

            if x in Number:
                box += x
                self.poss
                while x not in Number:
                    try:
                        x = str(value[self.pos])
                    except IndexError:
                        break
                    box += x
                    self.poss()
                self.TokenIn("NUMBER", box)
                box = ""
                continue
            box += x
            self.poss()
