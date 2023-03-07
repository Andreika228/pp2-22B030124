import os 
if os.path.exists("C:\\Users\\ПК\\Desktop\\Tester2.txt"):
    os.remove("C:\\Users\\ПК\\Desktop\\Tester2.txt")
else:
    print("File does not exist")