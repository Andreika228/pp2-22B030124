cars = ['Toyota', 'Buggatti', 'Audi', 'BMW', 'Ferrari', 'Hundai']
with open('tester.txt', "w") as file:
        for i in cars:
                file.write("%s\n" % i)

content = open('tester.txt')
print(content.read())