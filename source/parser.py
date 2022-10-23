# Append

class Parser():

    def __init__(self, Token):
        self.pos = 0
        self.column = 0
        self.line = 0
        self.Parser = []
        self.MakePerser(Token)

    def ThrowError(self, TokenLine, ErrorType):
        print("Error: find",
              ErrorType,
              "by",
              TokenLine["type"],
              "Error, at line:",
              TokenLine["line"],
              ", and column:",
              TokenLine["column"])

    def MakePerser(self, Token):
        # 重复
        self.Parser.append(Token.pop(0))
        while True:
            if len(Token) == 0:
                break
            if self.Parser[len(self.Parser) - 1]["type"] == Token[0]["type"]:
                self.ThrowError(Token.pop(0), "Repeat")
                continue
            self.Parser.append(Token.pop(0))
