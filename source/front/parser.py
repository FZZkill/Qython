# Append


class Parser:
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
            b = self.parser[len(self.parser) - 1]
            if len(Token) == 0:
                break
            # if b["type"] == Token[0]["type"]:
            # print("Error! # TODO")
            # Token.pop(0)
            # # TODO
            # continue
            self.parser.append(Token.pop(0))
            # String appends
            if b["type"] == "ST2":
                Token.pop(0)
                string = "'"
                while True:
                    string += str(Token.pop(0)["value"])
                    if string[-1] == "'":
                        break
                self.parser.append({"type": "string", "value": string})
            if b["type"] == "ST1":
                Token.pop(0)
                string = '"'
                while True:
                    string += str(Token.pop(0)["value"])
                    if string[-1] == '"':
                        break
                self.parser.append({"type": "string", "value": string})
