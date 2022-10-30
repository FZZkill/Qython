# Append

class Parser():

    def __init__(self, Token):
        self.pos = 0
        self.column = 0
        self.line = 0
        self.parser = []
        self.MakeParser(Token)

    def MakeParser(self, Token):
        # 重复
        self.parser.append(Token.pop(0))
        while True:
            if len(Token) == 0:
                break
            if self.parser[len(self.parser) - 1]["type"] == Token[0]["type"]:
                print("Error! # TODO")
                Token.pop(0)
                # TODO
                continue
            self.parser.append(Token.pop(0))
        # 字符串合并
