def read(filePath : str) :
    with open(filePath, 'r') as f:
        return f.read(), filePath

def only_read(filePath : str) :
    return read(filePath)[0]

def write(filePath : str, Items : str) :
    with open(filePath, 'w') as f:
        return f.write(Items), filePath

def reNote(Items : str) -> str :
    Items = Items.split("\n")
    obj = ""
    for i in Items:
        try :
            m = i.index('//')
            obj = obj + i[:m] + "\n"
        except :
            obj = obj + i + "\n"
    return obj
   
