import os
print('Exist:', os.access('C:\\Users\\ПК\\Desktop\\C Грант.docx', os.F_OK))
print('Readable:', os.access('C:\\Users\\ПК\\Desktop\\C Грант.docx', os.R_OK))
print('Writable:', os.access('C:\\Users\\ПК\\Desktop\\C Грант.docx', os.W_OK))
print('Executable:', os.access('C:\\Users\\ПК\\Desktop\\C Грант.docx', os.X_OK))