lines =0
with open ('Tester.docx',encoding="utf-8") as file:
    for line in file:
        lines+=1
print("Number of lines: ", lines)