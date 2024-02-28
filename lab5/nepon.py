
import re

def findre(s):
    result = re.search(r"ab*", s)
    if result:
        print("Find")
    else:
        print("Not find")

s = input()
findre(s)


import re

def findreg(s):
    res = re.search(r"ab{2,3}", s)
    if res:
        print(res[0])
    else:
        print("Nooo")

s = input()
findreg(s)



import re
def process_string(s):
    res= re.split('-', s)
    for result in res:
        if not result.isupper():
            print(result)

s = input()
process_string(s)





import re

def findre(s):
    result = re.search(r"[A-Z]+[a-z]", s)
    if result:
        print("Find")
    else:
        print("Not find")

s = input()
findre(s)

import re

def findre(s):
    result = re.search(r"a.*b$", s)
    if result:
        print("Find")
    else:
        print("Not find")

s = input()
findre(s)



import re 

def findreg(s):
    res = re.sub("[ ,.]", ":", s)
    print(res)

s = input()
findreg(s)



import re
def sn(s):
        return ''.join(x.capitalize() or '_' for x in s.split('_'))

print(sn('python_exercises'))


import re
def upp(s):
    res = re.findall(r"[A-Z][a-z]*", s)
    print(res)
s = input()
upp(s)


import re
def prob(s):
    return ' '.join(re.findall(r"[A-Z][a-z]*", s))
s = input()
result = prob(s)
print(result)
