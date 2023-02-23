import re
def te(text):
    patterns = '^a.*?b$'
    if re.search(patterns,text):
        return "Found"
    else:
        return "Not Found"
text=input()
print(te(text))