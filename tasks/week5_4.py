def generator(p):
    for i in p:
        for j in i:
            if j[1] == let:
                yield i
p=input("cities = ")
let=input("letter = ")

print(next(generator))


