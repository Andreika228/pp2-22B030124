import re
def te(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not Found"
text=input()
print(te(text))