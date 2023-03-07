import os
path = 'C:\\Users\\ПК\\Desktop\\pp2-22B030124'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\n Only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\n All directories and files :")
print([ name for name in os.listdir(path)])