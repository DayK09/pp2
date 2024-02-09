#ex1

def recipe(n):
    ounce = 28.3495231
    return ounce * n

n = int(input())
res = recipe(n)
print(res)  #{n = 2; → 56.69990462}

#ex2

def Fahrenheit(f):
    c = (5/9)*(f-32)
    return c

f = int(input())
res = Fahrenheit(f)
print(res)



#ex3

def solve(numheads, numlegs):
    legchic = 2
    legrab = 4
    s = numheads-((numlegs - (numheads * legchic))/2)
    c = (numlegs - (numheads * legchic))/2
    return s, c

numheads = int(input())
numlegs = int(input())
res = solve(numheads, numlegs)
print(res)






#ex5
import itertools

s = input()
perm_s = itertools.permutations(s)
for string in perm_s:
    print(string)


#ex6
def reverse_string(string):
    reversed_string = string.split()
    return " ".join(reversed_string[::-1])


s = input()
print(reverse_string(s))

#ex7

def has_33(nums):
    return len(nums) == 3

nums = list(map(int, input().split()))
res = has_33(nums)
print(res)

#ex8
def spy(n):
    s = [0, 0, 7]
    for num in n:
        if num == s[0]:
            s.pop(0)
        if not s:
            return True
    
    return False

a = list(map(int, input().split()))
res = spy(a)
print(res)

#ex9
def volume(rad):
    v = 4/3 * 3.14 * rad**3
    return v

r = int(input())
res = volume(r)
print(res)



#ex 10
def unique(lst):
    result = []
    length = len(lst)

    for i in range(length - 1):
        if lst[i] != lst[i + 1]:
            result.append(lst[i])

    if length > 0:
        result.append(lst[-1])

    return result

a = input().split()

res = unique(a)
print(res)
 
#ex12

def symbols(num, symb):
    for num in num:
        res = symb * num
        print(res)

num = list(map(int, input().split()))
symb = input()

symbols(num, symb)

#ex 13
import random

print("Hello! What is your name?")
n = input()

print("Well, " + n + ", I am thinking of a number between 1 and 20.")
rand = random.randint(1, 20)

guess_count = 0

while True:
    print("Take a guess.")
    num = int(input())
    guess_count += 1

    if num < rand:
        print("Your guess is too low.")
    elif num > rand:
        print("Your guess is too high.")
    else:
        print("Good job, " + n + "! You guessed my number in " + str(guess_count) + " guesses!")
        break









