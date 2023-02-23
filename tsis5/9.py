import re
def trans(text):
    return re.sub(r"(\w)([A-Z])",r"\1 \2", text)
text= input()
print(trans(text))