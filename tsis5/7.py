import re
def transfomation(text):
    return ' '.join(x.capitalize() or '_' for x in text.split('_'))
text = input()
print(transfomation(text))