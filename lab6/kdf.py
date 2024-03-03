
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

with open('ENglISH.txt', 'r') as f, open('demo.txt', 'a') as r:
    for i in f:
        r.write(i)

with open('demo.txt') as p:
    pr = p.read()
    print(pr)
    
import os
if os.path.exists('delete.txt') == True:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'delete.txt')
    os.remove(path)
else:
    print("NOT FOUND")

    

