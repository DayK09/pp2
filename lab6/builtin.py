
def aaa(n):
    num = 1
    for i in n:
        num *= i
    return num
print(aaa((1, 2, 3)))



def jd(s):
    count = 0
    cout1 = 0
    for x in s:
        if x.isupper():
            count += 1
        else:
            cout1 += 1

    return count, cout1
s = input()
print(jd(s))



def pall(s):
    cout = 0
    for x in range(len(s)//2):
        if s[x] != s[len(s) - x - 1]:
            return "Net"
    return"Da"  
s = input()
print(pall(s))


from time import sleep
import math

def sq(num, m):
    sleep(m/1000)
    x = math.sqrt(num)
    print(x)

num = int(input())
m = int(input())
sq(num, m)


def tr(s):
    return all(s)
print(tr(())) ####(True, True, True) -> True or (1, 0, 1) -> False

