import re
def te(text):
    patterns = '^[A-Z]+[a-z]+$'
    if re.search(patterns,text):
        return "Found"
    else:
        return "Not Found"
text = input()
print(te(text))