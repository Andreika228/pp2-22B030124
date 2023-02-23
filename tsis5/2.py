import re
def te(text):
    patterns ='^ab{2,3}'
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not Found"
text= input()
print(te(text))