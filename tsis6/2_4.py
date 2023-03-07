lines =0
with open (r'C:\Users\ПК\Desktop\Tester.txt', 'r') as file:
    for line in file:
        lines+=1
print("Number of lines: ", lines)