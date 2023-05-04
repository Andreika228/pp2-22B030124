import os
path = 'C:\\Users\\ПК\\Desktop\\pp2-22B030124'
print("Only directories:")
print([ i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i)) ])
print("\n Only files:")
print([ i for i in os.listdir(path) if not os.path.isdir(os.path.join(path, i)) ])
print("\n All directories and files :")
print([ i for i in os.listdir(path)])