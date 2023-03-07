import os
print("Test: is path exists or not:")
path = r'C:\\Users\\ПК\\Desktop\\Грант.rtf'
print(os.path.exists(path))
path = r'C:\\Users\\ПК\\Desktop\\Универ\\Линейная алгебра\\H.w14.09.2022.pdf'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDirectory name of the path:")
print(os.path.dirname(path))