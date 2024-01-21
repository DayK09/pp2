#ex 1
x = "Hello World!"
print(len(x))

# ex 2
txt = "Hello World!"
print(txt[0])

#ex 3
txt = "Hello World"
print(txt[2:5])

#ex 4
txt = " Hello, World! "
print(txt.strip())

#ex 5
txt = "Hello, World!"
txt = txt.upper()
print(txt)

#ex 6
txt = "Hello, World!"
txt = txt.lower()
print(txt)

#ex 7
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)

#ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
