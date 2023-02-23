import re 
def fe(text):
    return re.findall('[A-Z][^A-Z]*', text)
text=input()
print(fe(text))