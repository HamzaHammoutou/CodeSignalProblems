import re
def variableName(name):
    pattern = "^[a-zA-Z_]+[a-zA-Z_0-9]*$"
    return re.match(pattern, name) != None