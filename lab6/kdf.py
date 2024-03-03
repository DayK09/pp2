""""
import os
from datetime import datetime
print(os.getcwd())
os.chdir('/Users/Userr/Desktop/')
print(os.listdir())
print(os.stat('ENglISH.txt'))
mod = os.stat('ENglISH.txt').st_mtime
print(datetime.fromtimestamp(mod))

for dirpath, dirnames, filenames in os.walk('/Users/Userr/Desktop/'):
    print('Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

print(os.access('C:\\Users\\Userr\\Desktop\\ENglISH.txt', os.F_OK))##TRUE
print(os.access('C:\\Users\\Userr\\Desktop\\ENglISH.txt', os.R_OK)) ###TRUE
print(os.access('C:\\Users\\Userr\\Desktop\\ENglISH.txt', os.W_OK))  ###TRUE
print(os.access('C:\\Users\\Userr\\Desktop\\ENglISH.txt', os.X_OK))  ###TRUE


print(os.path.exists('C:\\Users\\Userr\\Desktop\\ENglISH.txt')) ###true



with open('C:\\Users\\Userr\\Desktop\\ENglISH.txt', 'r') as fcc_file:
    file = fcc_file.read()
    l = 0
    for string in file:
        l += len(string.split())
    print(l)
   
l = ['I', 'like', 'coffee']
with open('demo.txt', 'w') as fw:
    for i in l:
        fw.write(i + '\n')
        
with open('demo.txt') as r:
    pr = r.read()
    print(pr, end='')




import string

for abc in string.ascii_uppercase:
    with open(abc + '.txt', 'a') as r:
        r.writelines(abc)
    

"""