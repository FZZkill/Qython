from source.DEFINE import Keywords  # Keyword
from source.DEFINE import Word  # Words
from source.DEFINE import Number  # Number
from source.DEFINE import Key  # Keyword


class Lexer:
    def __init__(self, value):
        self.pos = 0
        self.column = 0
        self.line = 0
        self.Token = []
        self.MakeToken(value)

    def poss(self, step=1):
        self.column += step
        self.pos += step

    def poss_line(self, x, step=1):
        if x == "\n" or x == "\r":
            self.line += 1
            self.TokenIn("Ender", None)

    def isAdd(self, box):
        if box in Keywords.keys():
            self.TokenIn(Keywords[box], None)
        # Is Word
        elif box in Word.keys():
            self.TokenIn(Word[box], None)
        # Else is identifier
        else:
            self.TokenIn("IDENTIFIER", box)
        self.poss()

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
        box, x, lenght = "", "", len(value) - 1

        while self.pos != lenght:
            try:
                x = str(value[self.pos])
            except IndexError:
                break

            if x in Key or x in Word.keys():
                self.poss_line(x)
                self.isAdd(box)
                box = ""
                continue

            if x in Number:
                box += x
                self.poss()
                while True:
                    try:
                        x = str(value[self.pos])
                        if x not in Number:
                            break
                    except IndexError:
                        break
                    box += x
                    self.poss()
                self.TokenIn("NUMBER", box)
                box = ""
                continue
            box += x
            self.poss()
        self.TokenIn("EOF", "ENDOFFILE")
