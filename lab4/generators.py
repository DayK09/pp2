#ex1
def square_num(num):
   for i in range(num):
       yield i*i

n = int(input())
for i in square_num(n):
    print (i, end=' ')

#ex2
def even(n):
    for i in range(0, n):
        if i%2 == 0:
            yield i
        

n = int(input())
for i in even(n):
    print(i, end=' ')

#ex3
class div:
    def __init__(self,num):
        self.num = num

    def __iter__(self):
        return self
    
    def number(self):
        for i in range(0, self.num):
            if i%3 == 0 and i%4 == 0:
               print(i, end=' ')

n = int(input())
divv = div(n)
divv.number()


#ex4
def sq(a, b):
    for i in range(a, b+1):
        yield i*i

x = int(input())
y = int(input())
for i in sq(x, y):
    print(i, end =' ')


#ex5
def inverse(num):
    for i in range(num, -1, -1):
        yield i

number = int(input())
for i in inverse(number):
    print(i, end=' ')
              

    

