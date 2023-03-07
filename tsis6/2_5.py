color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('tester.txt', "w") as file:
        for i in color:
                file.write("%s\n" % i)

content = open('tester.txt')
print(content.read())